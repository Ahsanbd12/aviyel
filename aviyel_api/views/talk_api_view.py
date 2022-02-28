from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from aviyel_api.serializers import TalkSerializer

from aviyel_api.models import Talk, User

class TalkAPIView(APIView):
    def get(self, request, **kwargs):
        talk = get_object_or_404(Talk, pk=kwargs["t_id"])
        serializer = TalkSerializer(talk)
        return JsonResponse({"talk": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, **kwargs):
        talk = get_object_or_404(Talk, pk=kwargs["t_id"])
        user_list = request.data.get("users", None)
        if user_list:
            users = User.objects.filter(id__in=request.data.get("users"))
            talk.users.set(users)
        elif user_list == []:
            talk.users.clear()
        serializer = TalkSerializer(talk, data=request.data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        serializer.save()
        return JsonResponse(
            {"talk": serializer.data}, safe=False, status=status.HTTP_200_OK
        )