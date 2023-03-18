from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Image, Tier


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['username', 'email', 'acc_tier']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'acc_tier')}),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            # 'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'is_active',
                'is_staff',
                'is_superuser',
                'acc_tier',
            )
        }),
    )


class ImageAdmin(admin.ModelAdmin):
    """Define the admin pages for images."""
    list_display = ['id', 'image', 'thumb_image_1', 'thumb_image_2']


admin.site.register(User, UserAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Tier)
