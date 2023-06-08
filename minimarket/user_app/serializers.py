from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source='phone_number', max_length=20)
    fullName = serializers.CharField(source='user.get_full_name', max_length=100)
    email = serializers.CharField(source='user.email', max_length=100)

    class Meta:
        model = Profile
        fields = ('fullName', 'email', 'phone', 'avatar')


class AccountSerializer(serializers.ModelSerializer):
    fullName = serializers.CharField(source='user.get_full_name', max_length=100)
    email = serializers.CharField(source='user.email', max_length=100)

    class Meta:
        model = Profile
        fields = ('fullName', 'email', 'avatar')


class AvatarSerializer(serializers.Serializer):
    pass


class PasswordSerializer(serializers.Serializer):
    pass
