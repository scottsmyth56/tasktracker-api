from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    owner_username = serializers.SerializerMethodField()
    shared_users_usernames = serializers.ListField(
        child=serializers.CharField(), required=False
    )

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "due_date",
            "priority",
            "category",
            "status",
            "image",
            "owner_username",
            "shared_users_usernames",
        ]

    def update(self, instance, validated_data):
        shared_users_usernames = validated_data.pop("shared_users_usernames", None)

        if shared_users_usernames is not None:
            for username in shared_users_usernames:
                try:
                    user = User.objects.get(username=username)
                    instance.shared_users.add(user)
                except User.DoesNotExist:
                    print(f"User with username {username} does not exist.")

        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super(TaskSerializer, self).to_representation(instance)
        representation["shared_users_usernames"] = self.get_shared_users_usernames(
            instance
        )
        return representation

    def get_owner_username(self, obj):
        return obj.owner.username

    def get_shared_users_usernames(self, obj):
        return [user.username for user in obj.shared_users.all()]
