from django.db import models
from django.urls import reverse


class Task(models.Model):
    summary = models.CharField(max_length=50, verbose_name="Краткое описание")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Полное описание")
    status = models.ForeignKey('Status', on_delete=models.CASCADE, verbose_name="Статус")
    type = models.ManyToManyField('Type', verbose_name="Тип")
    project = models.ForeignKey('Project', on_delete=models.RESTRICT, verbose_name='Проект', related_name='tasks')
    added_date = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return f"{self.id} {self.summary} {self.status}"

    class Meta:
        db_table = "Task"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={'pk': self.pk})
