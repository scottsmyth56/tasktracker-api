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
from rest_framework.decorators import api_view


class EventListAPIView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventInvitationCreateAPIView(generics.ListCreateAPIView):
    queryset = EventInvitation.objects.all()
    serializer_class = EventInvitationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        event_id = request.data.get("event")
        recipient_user_id = request.data.get("recipient")
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
        event.save()

class EventInvitationUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventInvitation.objects.all()
    serializer_class = EventInvitationSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(["POST"])
def accept_invitation(request, pk):
    try:
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        invitation = EventInvitation.objects.get(pk=pk, recipient=request.user)

        if invitation.accepted:
            return Response(
                {"message": "This invitation has already been accepted."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        invitation.accepted = True
        invitation.save()
        event = invitation.event
        event.accepted_users.add(request.user)
        event.save()

        return Response(
            {"message": "Invitation accepted successfully!"}, status=status.HTTP_200_OK
        )

    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
