from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from Todo.utils import response_fun
from .serializers import *


class TodoViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'])
    def getAllTasks(self, request):
        query = TaskModel.objects.all()
        serializer = TaskSerializer(query, many=True)
        return response_fun(1, serializer.data)

    @action(detail=False, methods=['get'])
    def getTask(self, request):
        task_id = request.GET.get('task_id', None)
        if task_id is None:
            return response_fun(0, "No task id provided")
        task = TaskModel.objects.filter(pk=task_id).first()
        if task is None:
            return response_fun(0, "Task not found")
        else:
            serializer = TaskSerializer(task)
            return response_fun(1, serializer.data)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def addTask(self, request):
        data = request.data
        data = {
            **data,
            'user': request.user.pk
        }
        serializer = TaskCreationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response_fun(1, 'Task added')
        else:
            return response_fun(0, str(serializer.errors))

    @action(detail=False, methods=['patch'], permission_classes=[IsAuthenticated])
    def updateTask(self, request):
        data = request.data
        user = request.user
        task_id = data.get('TaskId', None)
        if task_id is None:
            return response_fun(0, "TaskId is required")

        obj = user.tasks.filter(pk=task_id).first()
        if not obj:
            return response_fun(0, "No Task found")

        serializer = TaskUpdationSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response_fun(1, "Task updated")
        else:
            return response_fun(0, serializer.errors)

    @action(detail=False, methods=['delete'], permission_classes=[IsAuthenticated])
    def deleteTask(self, request):
        user = request.user
        task_id = request.GET.get('task_id', None)
        if task_id is None:
            return response_fun(0, "No task id provided")

        obj = user.tasks.filter(pk=task_id).first()
        if not obj:
            return response_fun(0, "No Task found")

        obj.delete()
        return response_fun(1, "Task deleted")
