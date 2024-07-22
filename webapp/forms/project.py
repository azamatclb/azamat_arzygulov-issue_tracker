from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse

from webapp.models import Project


class ProjectForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label="Название проекта")
    description = forms.CharField(max_length=1000, label="Описание проекта", widget=forms.Textarea, required=False)

    class Meta:
        model = Project
        fields = ['name', 'description', 'date_started', "date_ended"]
        widgets = {
            'date_started': forms.DateInput(attrs={'type': 'date'}),
            'date_ended': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description:
            if description:
                if len(description) < 5:
                    raise ValidationError('This field must contain at least 5 symbols')
                elif len(description) > 1000:
                    raise ValidationError('This field cant contain more then 3000 symbols')
        return description

    def clean_summary(self):
        name = self.cleaned_data.get('name')
        if name:
            if len(name) > 50:
                raise ValidationError('This field cant contain more then 50 symbols')
            elif len(name) < 3:
                raise ValidationError('This field must contain at least 3 symbols')
        return name
