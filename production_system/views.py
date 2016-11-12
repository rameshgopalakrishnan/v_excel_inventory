from rest_framework import viewsets

from production_system.models import Task
from production_system.serializers import TaskSerializer


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
