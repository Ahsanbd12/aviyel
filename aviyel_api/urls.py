"""
API-level router
"""
from django.urls import path
from aviyel_api.views import ConferenceAPIView, ConferenceCollectionAPIView, TalkCollectionAPIView, TalkAPIView, UserCollectionAPIView

urlpatterns = [
    path("conferences", ConferenceCollectionAPIView.as_view(), name="conferences"),
    path("conferences/<int:id>", ConferenceAPIView.as_view(), name="conference"),
    path("conferences/<int:id>/talks", TalkCollectionAPIView.as_view(), name="conference_talks"),
    path("conferences/<int:id>/talks/<int:t_id>", TalkAPIView.as_view(), name="conference_talk"),
    path("users", UserCollectionAPIView.as_view(), name="users"),
]
