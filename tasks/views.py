from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions,status
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


class TaskListAPIView(APIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        tasks =  Task.objects.all()
        serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)