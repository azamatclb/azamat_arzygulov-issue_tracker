from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView

from webapp.forms.task import TaskForm
from webapp.models import Task, Project


class TasksListView(ListView):
    model = Task
    template_name = "task_templates/task_list.html"
    ordering = "-added_date"
    context_object_name = "tasks"
    paginate_by = 5


class AddTaskView(CreateView):
    template_name = "task_templates/task_add.html"
    model = Task
    form_class = TaskForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['project_pk'] = self.kwargs.get('pk')
        return kwargs

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:task_view', kwargs={"pk": self.object.pk})


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_templates/task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        context['task'] = task
        return context


class TaskUpdateView(UpdateView):
    template_name = 'task_templates/task_update.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('webapp:task_view', kwargs={"pk": self.object.pk})


class TaskDeleteView(DeleteView):
    template_name = 'task_templates/task_delete.html'
    model = Task
    success_url = reverse_lazy('webapp:project_list')
