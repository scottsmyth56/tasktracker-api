from django.shortcuts import render

from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated

class UserSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('username')
        if query:
            profiles = Profile.objects.filter(
                Q(user__username__icontains=query)
            )
            serializer = ProfileSerializer(profiles, many=True)
            return Response(serializer.data)
        return Response({"message": "invali search"}, status=status.HTTP_400_BAD_REQUEST)
