from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, ListView, UpdateView, DeleteView

from webapp.forms import TaskForm
from webapp.models import Task


class TasksListView(ListView):
    model = Task
    template_name = "task_templates/task_list.html"
    ordering = "-added_date"
    context_object_name = "tasks"
    paginate_by = 5


class AddTaskView(FormView):
    template_name = "task_templates/task_add.html"
    form_class = TaskForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        project_pk = self.kwargs.get('project_pk')
        kwargs['project_pk'] = project_pk
        return kwargs

    def form_valid(self, form):
        task = form.save()
        return redirect('task_view', pk=task.pk)


class TaskDetailView(TemplateView):
    template_name = 'task_templates/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        context['task'] = task
        return context


class TaskUpdateView(UpdateView):
    template_name = 'task_templates/task_update.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('task_view', kwargs={"pk": self.object.pk})


class TaskDeleteView(DeleteView):
    template_name = 'task_templates/task_delete.html'
    model = Task
    success_url = reverse_lazy('project_list')
