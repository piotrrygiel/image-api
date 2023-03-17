from rest_framework import (
    viewsets,
    status,
)
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from .models import Image


class ImageViewSet(viewsets.ModelViewSet):
    """View for manage image API."""
    serializer_class = serializers.ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        if self.action == 'upload_image':
            return serializers.ImageSerializer
        return serializers.ImageSerializer

    def perform_create(self, serializer):
        """Create a new image."""
        serializer.save(user=self.request.user)
