from rest_framework import serializers
from .models import Token


class TokenSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Token
        fields = ('id', 'media_type', 'duration', 'is_active')