import uuid
import os

from django.db import models
from django.conf import settings
# from django.contrib.auth.models import (
#     AbstractBaseUser,
#     BaseUserManager,
#     PermissionsMixin,
# )
from django.contrib.auth.models import AbstractUser


def image_file_path(instance, filename):
    """Generate file path for new image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'images', filename)


class Tier(models.Model):
    tier_name = models.CharField(max_length=255)
    thumbnail_height = models.IntegerField(default=200)
    is_original_file_available = models.BooleanField(default=False)
    is_expiring_link_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.tier_name


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(null=True, upload_to=image_file_path)

    # def __str__(self):
    #     return self.image


class User(AbstractUser):
    acc_tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True)
