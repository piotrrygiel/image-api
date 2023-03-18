from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

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
        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new image."""
        serializer.save(user=self.request.user)
