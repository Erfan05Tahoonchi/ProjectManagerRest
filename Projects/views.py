from .models import Project, Task, SubTask
from rest_framework import generics
from .permissions import permissions, CanUpdateDestroyProject, CanUpdateDestroyTask, CanUpdateDestroySubTask
from .serializers import ProjectSerializers, TaskSerializers, SubTaskSerializers
from rest_framework.response import Response
from rest_framework import status

class ProjectListCreateViews(generics.ListCreateAPIView):
    """
    this view creates and show list of projects
    """
    serializer_class = ProjectSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)


class ProjectListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    this view updates and deletes projects
    """
    serializer_class = ProjectSerializers
    permission_classes = [permissions.IsAuthenticated, CanUpdateDestroyProject]
    queryset = Project
    lookup_field = 'pk'

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class TaskListCreateViews(generics.ListCreateAPIView):
    """
    this view creates and show list of tasks
    """
    serializer_class = TaskSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Task.objects.filter(project__user=self.request.user, project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        project = Project.objects.get(id=project_id, user=self.request.user)
        if serializer.is_valid():
            serializer.save(project=project)


class TaskListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    this view updates and deletes tasks
    """
    serializer_class = TaskSerializers
    permission_classes = [permissions.IsAuthenticated, CanUpdateDestroyTask]
    queryset = Task
    lookup_field = 'pk'

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class SubTaskListCreateViews(generics.ListCreateAPIView):
    """
    this view creates and show list of subtasks
    """
    serializer_class = SubTaskSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        task_id = self.kwargs.get('task_pk')
        return SubTask.objects.filter(task__project__user=self.request.user, task_id=task_id)

    def perform_create(self, serializer):
        task_id = self.kwargs.get('task_pk')
        task = Task.objects.get(id=task_id, project__user=self.request.user)
        if serializer.is_valid():
            serializer.save(task=task)


class SubTaskListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    this view updates and deletes SubTasks
    """
    serializer_class = SubTaskSerializers
    permission_classes = [permissions.IsAuthenticated, CanUpdateDestroySubTask]
    queryset = SubTask
    lookup_field = 'pk'

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
