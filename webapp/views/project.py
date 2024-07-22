from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, DetailView, UpdateView, CreateView, DeleteView

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


class ProjectUpdateView(UpdateView):
    template_name = 'project_templates/project_update.html'
    form_class = ProjectForm
    model = Project


class ProjectCreateView(CreateView):
    template_name = 'project_templates/project_create.html'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project_list')
