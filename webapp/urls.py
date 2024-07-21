from django.urls import path

from webapp.views import TasksListView, AddTaskView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    # path('', TaskListView.as_view(), name='tasks_list'),
    path('', TasksListView.as_view(), name='tasks_list'),
    path('task/create', AddTaskView.as_view(), name='task_add'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_view'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete')
]
