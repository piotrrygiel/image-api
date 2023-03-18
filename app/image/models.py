import uuid
import os

from django.db import models
from django.conf import settings
from PIL import Image as ImagePIL
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from io import BytesIO
from django.core.files import File


def image_file_path(instance, filename):
    """Generate file path for new image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'images', filename)


class Tier(models.Model):
    tier_name = models.CharField(max_length=255, unique=True)
    thumbnail_height = models.PositiveIntegerField(default=0,
                                                   validators=[MinValueValidator(0), MaxValueValidator(2000)])
    is_original_file_available = models.BooleanField(default=False)
    is_expiring_link_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.tier_name


class User(AbstractUser):
    acc_tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True)


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(null=True, upload_to=image_file_path)
    thumb_image_1 = models.ImageField(null=True, upload_to=os.path.join('uploads', 'images'))

    def save(self, *args, **kwargs):
        super().save()
        if self.user.acc_tier.thumbnail_height != 0 and not self.thumb_image_1.name:
            img = ImagePIL.open(self.image.path)
            new_img = (img.width, self.user.acc_tier.thumbnail_height)
            thumb_img = img.copy()
            thumb_img.thumbnail(new_img)
            blob = BytesIO()
            if self.image.path[-3:] == 'png':
                thumb_img.save(blob, 'PNG')
                self.thumb_image_1.save(f'{uuid.uuid4()}_thumb.png', File(blob))
            else:
                thumb_img.save(blob, 'JPEG')
                self.thumb_image_1.save(f'{uuid.uuid4()}_thumb.jpeg', File(blob))
        if not self.user.acc_tier.is_original_file_available:
            self.image.delete()
