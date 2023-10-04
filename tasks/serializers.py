from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner_username = serializers.SerializerMethodField()
    shared_users_usernames = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'created_at',
            'due_date',
            'priority',
            'category',
            'status',
            'attachments',
            'owner_username',  
            'shared_users_usernames',
        ]
    
    def get_owner_username(self, obj):
        return obj.owner.username

    def get_shared_users_usernames(self, obj):
        return [user.username for user in obj.shared_users.all()]