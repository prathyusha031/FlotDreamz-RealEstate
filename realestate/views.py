from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.utils import timezone
from .models import LoginRecord  # Fixed invalid space issue
from random import randint
from django.contrib import messages
from django.contrib.auth import login as auth_login
from .models import Profile


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def main(request):
    return render(request, 'main.html')

def contact(request):
    return render(request, 'contact.html')

def faqs(request):
    return render(request, 'faqs.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_conditions(request):
    return render(request, 'terms_conditions.html')

def refund_policy(request):
    return render(request, 'refund_policy.html')

def customer_support(request):
    return render(request, 'customer_support.html')

def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        if not email or not password:
            return render(request, "login.html", {"error": "Email and Password are required!"})

        try:
            user_obj = User.objects.get(email=email)  
        except User.DoesNotExist:
            return render(request, "login.html", {"error": "Invalid email or password!"})

        user = authenticate(request, username=user_obj.username, password=password)  
        print(user)
        if user is not None:
            auth_login(request, user)  

            # Track login time
            login_record, created = LoginRecord.objects.get_or_create(user=user)
            login_record.login_time = timezone.now()
            login_record.save()

            return redirect("profile")  
        else:
            return render(request, "login.html", {"error": "Invalid email or password!"})

    return render(request, "login.html")

# realestate/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
import random

# Store OTPs temporarily (for production, use Redis/DB)
otp_storage = {}

def signup(request):
    if request.method == 'POST':
        if 'send_otp' in request.POST:
            # Step 1: Send OTP
            email = request.POST.get('email')
            if not email:
                messages.error(request, "Please enter your email.")
                return render(request, 'signup.html')

            otp = str(random.randint(100000, 999999))
            otp_storage[email] = otp  # Save OTP against email

            # Send OTP to email
            send_mail(
                'Your OTP for Flot Dreamz Signup',
                f'Your OTP is: {otp}',
                'bailapudiprathyusha@gmail.com',  # Replace with your email
                [email],
                fail_silently=False,
            )
            messages.success(request, f'OTP has been sent to {email}')
            return render(request, 'signup.html', {'email_sent': True, 'email_value': email})

        elif 'signup' in request.POST:
            # Step 2: Register after OTP verification
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            otp_input = request.POST.get('otp')
            mobile = request.POST.get('mobile')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if not all([full_name, email, otp_input, mobile, password, confirm_password]):
                messages.error(request, "All fields are required.")
                return render(request, 'signup.html')

            if email not in otp_storage or otp_input != otp_storage[email]:
                messages.error(request, "Invalid or expired OTP.")
                return render(request, 'signup.html', {'email_value': email})

            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return render(request, 'signup.html', {'email_value': email})

            if User.objects.filter(username=email).exists():
                messages.error(request, "User already exists.")
                return render(request, 'signup.html')

            # Create user
            user = User.objects.create_user(username=email, email=email, password=password, first_name=full_name)
            user.save()

            # Cleanup
            otp_storage.pop(email, None)
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')

    return render(request, 'signup.html')

# realestate/views.py

from django.http import JsonResponse
from django.core.mail import send_mail
import random

def send_email_otp(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if not email:
            return JsonResponse({"status": "fail", "message": "Email is required"}, status=400)

        otp = str(random.randint(100000, 999999))
        request.session["email_otp"] = otp
        request.session["otp_email"] = email

        subject = "Your OTP for Email Verification"
        message = f"Your OTP for verifying your email is: {otp}"
        from_email = None
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            return JsonResponse({"status": "success", "message": "OTP sent successfully"})
        except Exception as e:
            return JsonResponse({"status": "fail", "message": str(e)}, status=500)

    return JsonResponse({"status": "fail", "message": "Invalid request method"}, status=405)

from django.http import JsonResponse

def verify_email_otp(request):
    if request.method == "POST":
        user_otp = request.POST.get("otp")
        session_otp = request.session.get("email_otp")

        if not session_otp:
            return JsonResponse({"status": "error", "message": "No OTP found. Please request a new one."})

        if user_otp == session_otp:
            request.session["email_verified"] = True  # Optional: Set flag for further checks
            return JsonResponse({"status": "success", "message": "OTP verified successfully!"})
        else:
            return JsonResponse({"status": "error", "message": "Invalid OTP. Please try again."})

    return JsonResponse({"status": "error", "message": "Invalid request method."})

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def profile(request):
    return render(request, 'profile.html')


def update_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)

        # Update phone number if you have a Profile model
        if hasattr(user, 'profile'):
            user.profile.phone_number = request.POST.get('phone', user.profile.phone_number)
            user.profile.save()
        
        user.save()
        return redirect('profile')  # Redirect back to the profile page

    return redirect('profile') 

def loginwithotp(request):
    return render(request, 'loginwithotp.html')


from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from twilio.rest import Client
import os

# Correct usage of environment variable names
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_SERVICE_SID = os.getenv("TWILIO_VERIFY_SERVICE_SID")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def otp_mobile(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        country_code = request.POST.get('country_code', '+91')  
        full_mobile = country_code + mobile  

        if not mobile:
            messages.error(request, 'Please enter a mobile number.')
            return render(request, 'otp_mobile.html')

        try:
            verification = client.verify.v2.services(TWILIO_SERVICE_SID) \
                .verifications.create(to=full_mobile, channel="sms")
            
            if verification.status == "pending":
                request.session['mobile'] = full_mobile
                messages.success(request, 'OTP sent successfully!')
                return redirect('verify_otp')
            else:
                messages.error(request, 'Failed to send OTP.')
        except Exception as e:
            messages.error(request, f"Error: {e}")

    return render(request, 'otp_mobile.html')


def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        mobile = request.session.get('mobile')

        if not mobile:
            messages.error(request, "Session expired! Please request a new OTP.")
            return redirect('otp_mobile')

        try:
            verification_check = client.verify.v2.services(TWILIO_SERVICE_SID) \
                .verification_checks.create(to=mobile, code=entered_otp)

            if verification_check.status == "approved":
                messages.success(request, 'OTP Verified successfully!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid OTP!')
                return redirect('verify_otp')

        except Exception as e:
            messages.error(request, f"Error: {e}")

    return render(request, 'verify_otp.html')

from django.shortcuts import redirect

def send_otp(request):
    return redirect('otp_mobile')  # Or whatever makes sense for your flow


def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.posted_by = request.user
            property.save()
            return redirect('property_list')  # or your homepage
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})

from .forms import PropertyForm

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_list')  # Make sure you have a URL named 'property_list'
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})

from django.shortcuts import render
from .models import Property

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

from django.shortcuts import render

def projects(request):
    return render(request, 'pages/projects.html')

def agents(request):
    return render(request, 'pages/agents.html')

def neighbourhoods(request):
    return render(request, 'pages/neighbourhoods.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Inquiry, Agent, Blog, Deal
from django.db.models import Q

def property_list(request):
    query = request.GET.get('q')
    property_type = request.GET.get('type')
    properties = Property.objects.all()
    if query:
        properties = properties.filter(Q(title__icontains=query) | Q(location__icontains=query))
    if property_type:
        properties = properties.filter(property_type=property_type)
    return render(request, 'property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Inquiry.objects.create(name=name, email=email, message=message, property=property)
        return redirect('property_detail', pk=pk)
    return render(request, 'property_detail.html', {'property': property})

def agent_list(request):
    agents = Agent.objects.all()
    return render(request, 'agents.html', {'agents': agents})

def neighbourhoods(request):
    return render(request, 'neighbourhoods.html')

def project_view(request):
    return render(request, 'projects.html')


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blogs.html', {'blogs': blogs})

def deal_list(request):
    deals = Deal.objects.all().order_by('valid_until')
    return render(request, 'deals.html', {'deals': deals})

