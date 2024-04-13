from django.contrib import admin
from .models import User, UserSMS

# Register your models here.

admin.site.register(User)
admin.site.register(UserSMS)