from django.contrib import admin
from .models import LoginRecord

class LoginRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_fullname', 'get_email', 'login_time')  # Use custom methods

    def get_fullname(self, obj):
        return obj.user.get_full_name()  # Fetch from User model
    get_fullname.short_description = "Full Name"

    def get_email(self, obj):
        return obj.user.email  # Fetch from User model
    get_email.short_description = "Email"

admin.site.register(LoginRecord, LoginRecordAdmin)

from django.contrib import admin
from .models import Property, Inquiry, Agent, Blog, Deal

admin.site.register(Property)
admin.site.register(Inquiry)
admin.site.register(Agent)
admin.site.register(Blog)
admin.site.register(Deal)

