from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from aviyel_api.serializers import ConferenceSerializer

from aviyel_api.models import Conference


class ConferenceAPIView(APIView):
    def get(self, request, **kwargs): #show
        conf = get_object_or_404(Conference, pk=kwargs["id"])
        serializer = ConferenceSerializer(conf)
        return JsonResponse({"conference": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, **kwargs): #update
        conf = get_object_or_404(Conference, pk=kwargs["id"])
        serializer = ConferenceSerializer(conf, data=request.data, partial=True)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        serializer.save()
        return JsonResponse(
            {"conference": serializer.data}, safe=False, status=status.HTTP_200_OK
        )

    def delete(self, request, **kwargs): #destroy
        conf = get_object_or_404(Conference, pk=kwargs["id"])
        conf.delete()
        return JsonResponse(
            {"message": "Object deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
