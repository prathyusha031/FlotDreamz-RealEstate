from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LoginView
from .views import send_otp, verify_otp


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('main/', views.main, name='main'),
    path('contact/', views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),
    path('refund_policy/', views.refund_policy, name='refund_policy'),
    path('customer_support/', views.customer_support, name='customer_support'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path("send-email-otp/", views.send_email_otp, name="send_email_otp"),
    path('verify-email-otp/', views.verify_email_otp, name='verify_email_otp'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('profile/', views.profile, name='profile'),  # Profile page
    path('update-profile/', views.update_profile, name='update_profile'),  # Add this line
    path('loginwithotp/', views.loginwithotp, name='loginwithotp'),
    path("send_otp/", send_otp, name="send_otp"),
    path("verify_otp/", verify_otp, name="verify_otp"),
    path("otp_mobile/", verify_otp, name="otp_mobile"),
    path('add-property/', views.add_property, name='add_property'),
     path('properties/', views.property_list, name='property_list'),
    path('properties/<int:pk>/', views.property_detail, name='property_detail'),
    path('agents/', views.agent_list, name='agent_list'),
    path('neighbourhoods/', views.neighbourhoods, name='neighbourhoods'),
    path('projects/', views.project_view, name='projects'),
    path('blogs/', views.blog_list, name='blogs'),
    path('deals/', views.deal_list, name='deal_list'),

]


