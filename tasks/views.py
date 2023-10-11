from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


class TaskListAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Task.objects.all()


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
