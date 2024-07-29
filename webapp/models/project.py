from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Project(models.Model):
    date_started = models.DateField(verbose_name='Дата начала')
    date_ended = models.DateField(verbose_name='Дата окончания', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="Название проекта")
    description = models.TextField(max_length=1000, verbose_name="Описание проекта")

    author = models.ForeignKey(get_user_model(), related_name="project", on_delete=models.SET_DEFAULT, default=1 )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'Project'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def get_absolute_url(self):
        return reverse("webapp:project_detail", kwargs={'pk': self.pk})
