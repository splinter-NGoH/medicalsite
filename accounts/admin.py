from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin



class AccountAdmin(UserAdmin):

    list_display = (
        "email",
        "username",
        "last_login",
        "is_active",
        "date_joined",
    )
    list_display_links = (
        "email",
        "last_login",
        "is_active",
        "date_joined",
    )
    readonly_fields = ("last_login", "date_joined")
    ordering = ("-date_joined",)

    list_filter = ["email"]


admin.site.register(UserProfile, AccountAdmin)
