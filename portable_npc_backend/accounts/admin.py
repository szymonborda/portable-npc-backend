from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from portable_npc_backend.accounts.models import Account


class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(Account, CustomUserAdmin)
