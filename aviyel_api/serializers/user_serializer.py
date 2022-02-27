from dataclasses import fields
from rest_framework import serializers

from aviyel_api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)

