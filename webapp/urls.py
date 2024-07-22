from django.urls import path

from webapp.views import TasksListView, AddTaskView, TaskDetailView, TaskUpdateView, TaskDeleteView
from webapp.views.project import ProjectListView, ProjectDetailView, ProjectUpdateView, ProjectCreateView, ProjectDeleteView

# , , \
#
urlpatterns = [
    path('tasks/', TasksListView.as_view(), name='tasks_list'),
    path('task/create', AddTaskView.as_view(), name='task_add'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_view'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
    path('', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('project/create', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete')

]
