from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Group, WaitGroup

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     fields = ['user', 'choices']


class ProfileAdmin(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# admin.site.unregister(User)
# @admin.register(User)
    
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileAdmin]
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register([Group, WaitGroup])