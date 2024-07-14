from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name','nickname','number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name','nickname', 'number', 'password1', 'password2'),
        }),
    )
    list_display = ('first_name', 'last_name', 'number', 'email', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'number')
    ordering = ('email',)

admin.site.register(CustomUser, UserAdmin)