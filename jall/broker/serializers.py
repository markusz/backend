from rest_framework import serializers
from .models import Token, Accounting


class TokenSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Token
        fields = ('id', 'token_type', 'media_type', 'duration', 'is_active')


class AccountingSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Accounting
        fields = ('media_type', 'limits')