from rest_framework.serializers import ModelSerializer
from .models import Image


class ImageSerializer(ModelSerializer):
    """Serializer for uploading images."""

    class Meta:
        model = Image
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}
