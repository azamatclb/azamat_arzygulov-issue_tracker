from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Type, Status, Task


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TaskForm(forms.ModelForm):
    summary = forms.CharField(max_length=50, label="Краткое описание")
    description = forms.CharField(max_length=3000, label="Полное описание", widget=forms.Textarea, required=False)

    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type']
        widgets = {'type': forms.CheckboxSelectMultiple()}

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description:
            if description:
                if len(description) < 5:
                    raise ValidationError('This field must contain at least 5 symbols')
                elif len(description) > 3000:
                    raise ValidationError('This field cant contain more then 3000 symbols')
        return description

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if summary:
            if len(summary) > 50:
                raise ValidationError('This field cant contain more then 50 symbols')
            elif len(summary) < 3:
                raise ValidationError('This field must contain at least 3 symbols')
        return summary
