from django.db import models
from django.contrib.auth.models import User

class LoginRecord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  
    login_time = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


    def __str__(self):
        return f"{self.fullname} - {self.email} - {self.login_time}"
    

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('Buy', 'Buy'),
        ('Sell', 'Sell'),
        ('Commercial', 'Commercial'),
        ('Luxury', 'Luxury Homes')
    ]

    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='property_images/')
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPE_CHOICES,
        default='Buy'
    )

    def __str__(self):
        return self.title
    
class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry by {self.name}"

class Agent(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='agent_photos/')

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Deal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    discount_percent = models.IntegerField()
    valid_until = models.DateField()

    def __str__(self):
        return self.title
