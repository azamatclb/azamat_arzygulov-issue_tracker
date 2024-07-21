from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, FormView, ListView

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


class TaskUpdateView(FormView):
    template_name = 'task_templates/task_update.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, request, *args, **kwargs):
        return get_object_or_404(Task, pk=self.kwargs.get('pk'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def form_valid(self, form):
        form.save()
        return redirect('task_view', pk=self.task.pk)


class TaskDeleteView(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        return render(request, "task_templates/task_delete.html", {'task': task})

    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('tasks_list')
