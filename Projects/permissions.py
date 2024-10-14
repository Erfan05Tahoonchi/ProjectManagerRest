from rest_framework import permissions
from django.contrib.auth.models import User
from .models import Project, Task, SubTask
from django.shortcuts import get_object_or_404


class CanUpdateDestroyProject(permissions.BasePermission):
    """
    custom permision to check if the user can update or delete project
    """

    def has_permission(self, request, view):
        user = request.user
        project_id = view.kwargs.get('pk')
        project = get_object_or_404(Project, id=project_id)

        try:
            if user == project.user:
                return True
        except user.DoesNotExist or project.DoesNotExist:
            pass
        return False


class CanUpdateDestroyTask(permissions.BasePermission):
    """
    Custom permission to check if the user can update or delete a task
    """

    def has_permission(self, request, view):
        user = request.user
        task_id = view.kwargs.get('pk')
        task = get_object_or_404(Task, id=task_id)

        try:
            if user == task.project.user:
                return True
        except user.DoesNotExist or task.DoesNotExist or task.project.DoesNotExist:
            pass
        return False


class CanUpdateDestroySubTask(permissions.BasePermission):
    """
    Custom permission to check if the user can update or delete a subtask
    """

    def has_permission(self, request, view):
        user = request.user
        subtask_id = view.kwargs.get('pk')
        subtask = get_object_or_404(SubTask, id=subtask_id)

        try:
            if user == subtask.task.project.user:
                return True
        except user.DoesNotExist or subtask.DoesNotExist or subtask.task.DoesNotExist or subtask.task.project.DoesNotExist:
            pass
        return False
