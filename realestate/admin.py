from django.contrib import admin
from .models import (
    LoginRecord,
    Profile,
    Property,
    Inquiry,
    Agent,
    Blog,
    Deal
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone_number")
    search_fields = ("user__username", "phone_number")


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "price", "property_type")
    search_fields = ("title", "location", "property_type")
    list_filter = ("property_type",)


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "property", "created_at")
    search_fields = ("name", "email")
    list_filter = ("created_at",)


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ("name", "contact")
    search_fields = ("name", "contact")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "author")


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ("title", "discount_percent", "valid_until")
    search_fields = ("title",)
    list_filter = ("valid_until",)


@admin.register(LoginRecord)
class LoginRecordAdmin(admin.ModelAdmin):
    list_display = ("user", "fullname", "email", "login_time")
    search_fields = ("fullname", "email")