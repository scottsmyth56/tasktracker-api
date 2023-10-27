from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions,status,generics,filters
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event
from django_filters.rest_framework import DjangoFilterBackend



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