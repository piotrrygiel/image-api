from rest_framework.serializers import ModelSerializer
from .models import Image


class ImageSerializer(ModelSerializer):
    """Serializer for uploading images."""

    class Meta:
        model = Image
        fields = ['id', 'image', 'thumb_image_1', 'thumb_image_2']
        read_only_fields = ['id', 'thumb_image_1', 'thumb_image_2']
        extra_kwargs = {'image': {'required': 'True'}}
