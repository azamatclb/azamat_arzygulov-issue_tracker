from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView

from webapp.forms.task import TaskForm
from webapp.models import Task


class TasksListView(ListView):
    model = Task
    template_name = "task_templates/task_list.html"
    ordering = "-added_date"
    context_object_name = "tasks"
    paginate_by = 5


class AddTaskView(LoginRequiredMixin, CreateView):
    template_name = 'task_templates/task_add.html'
    model = Task
    form_class = TaskForm

    def form_valid(self, form):
        project = form.cleaned_data['project']
        if not self.request.user.groups.filter(name__in=['manager', 'captain', 'developer']).exists():
            raise PermissionDenied
        if not self.request.user.groups.filter(name='manager').exists() and self.request.user != project.author:
            raise PermissionDenied
        return super().form_valid(form)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_templates/task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        context['task'] = task
        return context


class TaskUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'task_templates/task_update.html'
    form_class = TaskForm
    model = Task
    permission_required = 'webapp.change_task'

    def has_permission(self):
        project = self.get_object()
        user = self.request.user
        return user.groups.filter(name='manager').exists() or user == project.author

    def get_success_url(self):
        return reverse('webapp:task_view', kwargs={"pk": self.object.pk})


class TaskDeleteView(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    template_name = 'task_templates/task_delete.html'
    model = Task
    success_url = reverse_lazy('webapp:project_list')
    permission_required = 'webapp.delete_task'

    def has_permission(self):
        project = self.get_object()
        user = self.request.user
        return user.groups.filter(name='manager').exists() or user == project.author
