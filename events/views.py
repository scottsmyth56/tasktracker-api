from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions,status,generics
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event

# class TaskListAPIView(APIView):
#     serializer_class = EventSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
#     def get(self, request):
#         events =  Event.objects.all()
#         serializer = self.serializer_class(events, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class EventListAPIView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
    
    
class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]