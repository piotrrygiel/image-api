import uuid
import os

from django.db import models
from django.conf import settings
from PIL import Image as ImagePIL
from django.contrib.auth.models import AbstractUser


def image_file_path(instance, filename):
    """Generate file path for new image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'images', filename)


class Tier(models.Model):
    tier_name = models.CharField(max_length=255, unique=True)
    thumbnail_height = models.IntegerField()
    is_original_file_available = models.BooleanField(default=False)
    is_expiring_link_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.tier_name


class User(AbstractUser):
    acc_tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True)


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(null=True, upload_to=image_file_path)

    def save(self, *args, **kwargs):
        super().save()
        img = ImagePIL.open(self.image.path)
        new_img = (img.width, self.user.acc_tier.thumbnail_height)
        img.thumbnail(new_img)
        img.save(self.image.path)
