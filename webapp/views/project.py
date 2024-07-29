from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from webapp.forms import SearchForm, ProjectForm
from webapp.models import Project


class ProjectListView(ListView):
    template_name = 'project_templates/project_list.html'
    model = Project
    context_object_name = 'projects'
    ordering = "-date_started"
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value)
            )
        return queryset

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        context['search_value'] = self.search_value
        return context

    def get_search_value(self):
        form = self.form
        if form.is_valid():
            return form.cleaned_data['search']
        return form


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_templates/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        context['tasks'] = project.tasks.all()
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'project_templates/project_create.html'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('webapp:project_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'project_templates/project_update.html'
    form_class = ProjectForm
    model = Project
    permission_required = 'webapp.change_project'

    def has_permission(self):
        project = self.get_object()
        user = self.request.user
        return user.groups.filter(name='manager').exists() or user == project.author


class ProjectDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'project_templates/project_delete.html'
    model = Project
    success_url = reverse_lazy('webapp:project_list')
    permission_required = 'webapp.delete_project'

    def has_permission(self):
        project = self.get_object()
        user = self.request.user
        return user.groups.filter(name='manager').exists() or user == project.author
