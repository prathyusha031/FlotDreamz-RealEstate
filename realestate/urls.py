from django.urls import path
from . import views

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

    # Authentication
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),

    # Profile
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),

    # Properties
    path('add-property/', views.add_property, name='add_property'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:pk>/', views.property_detail, name='property_detail'),

    # Agents
    path('agents/', views.agent_list, name='agent_list'),

    # Neighborhoods
    path('neighbourhoods/', views.neighbourhoods, name='neighbourhoods'),

    # Projects
    path('projects/', views.project_view, name='projects'),

    # Blogs
    path('blogs/', views.blog_list, name='blogs'),

    # Deals
    path('deals/', views.deal_list, name='deal_list'),

    # Cart
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]