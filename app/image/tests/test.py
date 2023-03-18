# from decimal import Decimal
import tempfile
import os

from PIL import Image as ImagePIL
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework import status
from rest_framework.test import APIClient

from ..models import User, Image, Tier


IMAGES_URL = reverse('image:image-list')


class PublicImageAPITests(TestCase):
    """Test unauthorized API requests."""
    def setUp(self):
        self.client = APIClient()

    def test_permission_required(self):
        """Test permission is required to call API."""
        res = self.client.get(IMAGES_URL)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class ModelTests(TestCase):
    """Test models."""

    def test_create_tier(self):
        """Test creating a tier is successful."""
        tier = Tier.objects.create(
            tier_name='Test tier name',
            thumbnail_height=50,
        )

        self.assertEqual(str(tier), tier.tier_name)

    def test_create_user(self):
        """Test creating a user is successful."""
        username = 'testusername'
        password = 'testpass123'

        user = User.objects.create(username=username, password=password)

        self.assertEqual(user.username, username)

    def test_create_user_with_tier(self):
        """Test creating a user with custom tier is successful."""
        tier = Tier.objects.create(
            tier_name='Test tier name',
            thumbnail_height=50,
        )
        username = 'testusername'

        user = User.objects.create(username=username, password='testpass123', acc_tier=tier)

        self.assertEqual(user.username, username)
        self.assertEqual(tier.thumbnail_height, user.acc_tier.thumbnail_height)


class ImageAPITests(TestCase):
    """Tests for image API."""
    def setUp(self):
        self.client = APIClient()
        self.tier = Tier.objects.create(
            tier_name='Test tier name',
            thumbnail_height=50,
        )
        self.user = User.objects.create(username='testuname', password='testpass123', acc_tier=self.tier)
        self.client.force_authenticate(self.user)

    def test_upload_image(self):
        """Test uploading image via API."""
        with tempfile.NamedTemporaryFile(suffix='.jpg') as image_file:
            img = ImagePIL.new('RGB', (10, 10))
            img.save(image_file, format='JPEG')
            image_file.seek(0)
            payload = {'image': image_file}
            res = self.client.post(IMAGES_URL, payload, format='multipart')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn('image', res.data)

    def test_upload_image_bad_request(self):
        """Test uploading invalid image."""
        payload = {'image': 'notanimage'}
        res = self.client.post(IMAGES_URL, payload, format='multipart')

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
