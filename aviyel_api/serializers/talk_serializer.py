from dataclasses import fields
from rest_framework import serializers
from .user_serializer import UserSerializer

from aviyel_api.models import Talk


class TalkSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Talk
        fields = ("id", "title", "description", "duration", "schedule_date", "conference", "users") 

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

