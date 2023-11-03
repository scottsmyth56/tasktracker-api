from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status, generics, filters
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import EventInvitationSerializer
from .models import EventInvitation
from django.contrib.auth.models import User


class EventListAPIView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]


class EventInvitationCreateAPIView(generics.ListCreateAPIView):
    queryset = EventInvitation.objects.all()
    serializer_class = EventInvitationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        event_id = request.data.get("event")
        recipient_user_id = request.data.get("recipient")
        # print(recipient_username)
        recipient = User.objects.get(id=recipient_user_id)

        if EventInvitation.objects.filter(
            event_id=event_id, recipient=recipient
        ).exists():
            return Response(
                {"message": "User already invited to this event."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        invitation = serializer.save(sender=self.request.user)
        event = invitation.event
        event.invited_users.add(invitation.recipient)
        # print(invitation.recipient.username)
        # print(event.invited_users.all())
        # print(self.request.user.username)
        event.save()
