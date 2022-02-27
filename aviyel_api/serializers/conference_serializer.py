from dataclasses import fields
from rest_framework import serializers
from .talk_serializer import TalkSerializer

from aviyel_api.models import Conference


class ConferenceSerializer(serializers.ModelSerializer):
    talks = TalkSerializer(source="talk_set", many=True)

    class Meta:
        model = Conference
        fields = ("id", "title", "description", "start_date", "end_date", "talks")

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
