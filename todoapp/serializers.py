from rest_framework import serializers

from .models import TaskModel


class TaskSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = TaskModel
        fields = ['TaskId', 'title', 'description', 'status_display']


class TaskCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'status', 'user', 'due_date']
        extra_kwargs = {
            'status': {'required': False, 'default': 0}
        }


class TaskUpdationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'status']
