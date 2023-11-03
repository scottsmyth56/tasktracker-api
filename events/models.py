from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    invited_users = models.ManyToManyField(
        User, related_name="event_invitations", blank=True
    )
    accepted_users = models.ManyToManyField(
        User, related_name="accepted_events", blank=True
    )

    def __str__(self):
        return self.title


class EventInvitation(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_invitations"
    )
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_invitations"
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return (
            f"Invitation from {self.sender} to {self.recipient} for event: {self.event}"
        )
