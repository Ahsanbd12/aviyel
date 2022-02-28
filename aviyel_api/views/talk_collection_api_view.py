import imp
from turtle import pd
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from aviyel_api.serializers import TalkSerializer

from aviyel_api.models import Talk, Conference, User


class TalkCollectionAPIView(APIView):
    def get(self, request, **kwargs):
        conf = get_object_or_404(Conference, pk=kwargs["id"])
        talks = conf.talk_set.all()
        serializer = TalkSerializer(talks, many=True)
        return JsonResponse({"talks": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        try:
            conf = get_object_or_404(Conference, pk=kwargs["id"])
            users = request.data.pop('users', None)
            talk = Talk.objects.create(**request.data, conference=conf)
            if users:
                user_set = User.objects.filter(id__in=users)
                talk.users.set(user_set)
            serializer = TalkSerializer(talk)
            response = {"talk": serializer.data}
            response_status = status.HTTP_201_CREATED
        except ValidationError as err:
            response = {"message": err.message_dict}
            response_status = status.HTTP_400_BAD_REQUEST
        return JsonResponse(response, safe=False, status=response_status)

