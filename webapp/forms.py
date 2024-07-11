from django import forms

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
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].widget = forms.CheckboxSelectMultiple()
        self.fields['type'].queryset = Type.objects.all()
