from django.contrib import admin
from django.urls import path
from .views import ProjectListCreateViews, ProjectListUpdateDeleteView, TaskListCreateViews, TaskListUpdateDeleteView, SubTaskListCreateViews, SubTaskListUpdateDeleteView

app_name = 'projects'

urlpatterns = [
    #projects urls
    path('list/create/', ProjectListCreateViews.as_view(), name='project_list_create'),
    path('update/destroy/<int:pk>/', ProjectListUpdateDeleteView.as_view(), name='project_list_update_delete'),
    #tasks urls
    path('tasks/list/create/<int:project_pk>/', TaskListCreateViews.as_view(), name='task_list_create'),
    path('tasks/update/destroy/<int:pk>/', TaskListUpdateDeleteView.as_view(), name='task_list_update_delete'),
    # sub task urls
    path('subtasks/list/create/<int:task_pk>/', SubTaskListCreateViews.as_view(), name='subtask_list_create'),
    path('subtasks/update/destroy/<int:pk>/', SubTaskListUpdateDeleteView.as_view(), name='subtask_list_update_delete'),

]
