from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Text Area',
            {
                'fields': (
                    'bio',
                )
            }
        )
    )


admin.site.register(User, CustomUserAdmin)
