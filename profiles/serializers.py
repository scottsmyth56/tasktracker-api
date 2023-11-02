from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    user_id = serializers.IntegerField(source='user.id')


    class Meta:
        model = Profile
        fields = ('user_id', 'username', 'firstName', 'lastName', 'email')
