from django.contrib import admin

# Register your models here.

from rest_framework.authtoken.models import Token

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')
    fields = ('user',)
    ordering = ('-created',)