import requests
from django.conf import settings
from django_rest_passwordreset.models import ResetPasswordToken
from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )


class UserSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

        BASE_URL = settings.BASE_URL
        r = requests.post(BASE_URL+'/api/password-reset/', data={'email':user.email})

        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user