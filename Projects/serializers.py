from rest_framework import serializers
from .models import Project, Task, SubTask


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'pk',
            'title',
            'user',
            'description',
            'color',
            'image',
            'start_date',
            'end_date',
            'status',
            'budget',

        )
        extra_kwargs = {
            'user': {'read_only': True},
        }


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'pk',
            'project',
            'title',
            'description',
            'color',
            'image',
            'start_date',
            'end_date',
            'status',
            'budget',

        )
        extra_kwargs = {
            'project': {'read_only': True},
        }


class SubTaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = (
            'pk',
            'task',
            'title',
            'description',
            'color',
            'image',
            'start_date',
            'end_date',
            'status',
            'budget',

        )
        extra_kwargs = {
            'task': {'read_only': True},
        }
