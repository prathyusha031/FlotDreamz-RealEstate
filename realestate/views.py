from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.utils import timezone
from .models import LoginRecord 
from django.contrib import messages
from django.contrib.auth import login as auth_login
from .models import Property, Inquiry, Agent, Blog, Deal


def home(request):
    properties = Property.objects.all()[:3]
    agents = Agent.objects.all()[:3]
    blogs = Blog.objects.all().order_by('-created_at')[:3]
    deals = Deal.objects.all()[:2]

    context = {
        'properties': properties,
        'agents': agents,
        'blogs': blogs,
        'deals': deals,
    }

    return render(request, 'home.html', context)

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

            login_record, created = LoginRecord.objects.get_or_create(
                user=user,
                defaults={
                 "fullname": user.first_name,
                   "email": user.email,
                }
            )

            login_record.login_time = timezone.now()
            login_record.save()

            return redirect("profile")  
        else:
            return render(request, "login.html", {"error": "Invalid email or password!"})

    return render(request, "login.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not all([full_name, email, password, confirm_password]):
            messages.error(request, "All fields are required.")
            return render(request, 'signup.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'signup.html')

        User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=full_name
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')

    return render(request, 'signup.html')

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


from django.shortcuts import render, redirect
from django.contrib import messages


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

