import imp
from turtle import pd
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from aviyel_api.serializers import ConferenceSerializer

from aviyel_api.models import Conference

class ConferenceCollectionAPIView(APIView):
    def get(self, request): #index
        conferences = Conference.objects.all()
        serializer = ConferenceSerializer(conferences, many=True)
        return JsonResponse({"conferences": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request): #create
        try:
            serializer = ConferenceSerializer(data=request.data)
            if not serializer.is_valid():
                raise ValidationError(serializer.errors)
            serializer.save()
            response = {"conference": serializer.data}
            response_status = status.HTTP_201_CREATED
        except ValidationError as err:
            response = {"message": err.message_dict}
            response_status = status.HTTP_400_BAD_REQUEST
        return JsonResponse(response, safe=False, status=response_status)


