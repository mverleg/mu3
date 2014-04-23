
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import MuUser


class CustomUserAdmin(UserAdmin):
    
    fieldsets = UserAdmin.fieldsets
    fieldsets[0][1]['fields'] += ()


admin.site.register(MuUser, CustomUserAdmin)


