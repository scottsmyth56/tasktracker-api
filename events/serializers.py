from rest_framework import serializers
from .models import Event
from .models import EventInvitation


class EventSerializer(serializers.ModelSerializer):
    invited_users = serializers.SerializerMethodField()
    accepted_users = serializers.SerializerMethodField()
    owner_username = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "date",
            "time",
            "location",
            "invited_users",
            "accepted_users",
            "owner_username",
        ]

    def get_owner_username(self, obj):
        return obj.owner.username

    def get_invited_users(self, obj):
        return [user.username for user in obj.invited_users.all()]

    def get_accepted_users(self, obj):
        return [user.username for user in obj.accepted_users.all()]


class EventInvitationSerializer(serializers.ModelSerializer):
    sender_username = serializers.SerializerMethodField()
    recipient_username = serializers.SerializerMethodField()
    event_title = serializers.SerializerMethodField()

    class Meta:
        model = EventInvitation
        fields = [
            "id",
            "event",
            "sender",
            "recipient",
            "accepted",
            "sender_username",
            "recipient_username",
            "event_title",
        ]

    def get_sender_username(self, obj):
        return obj.sender.username

    def get_recipient_username(self, obj):
        return obj.recipient.username

    def get_event_title(self, obj):
        return obj.event.title
