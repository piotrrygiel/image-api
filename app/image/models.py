from django.db import models
from django.conf import settings
# from django.contrib.auth.models import (
#     AbstractBaseUser,
#     BaseUserManager,
#     PermissionsMixin,
# )
from django.contrib.auth.models import AbstractUser


class Tier(models.Model):
    tier_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tier_name


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    # image = models.ImageField(null=True, upload_to=recipe_image_file_path)


class User(AbstractUser):
    acc_tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True)
