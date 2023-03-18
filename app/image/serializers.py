from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Image
from PIL import Image as ImagePIL


class ImageSerializer(ModelSerializer):
    """Serializer for uploading images."""

    class Meta:
        model = Image
        fields = ['id', 'image', 'thumb_image_1']
        read_only_fields = ['id', 'thumb_image_1']
        extra_kwargs = {'image': {'required': 'True'}}
