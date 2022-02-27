from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from aviyel_api.serializers import TalkSerializer, UserSerializer

from aviyel_api.models import User


class UserCollectionAPIView(APIView):
    def get(self, request): 
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse({"users": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                raise ValidationError(serializer.errors)
            serializer.save()
        except ValidationError as err:
            return JsonResponse({"validation errors": err.message_dict}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

    