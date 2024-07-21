from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип задачи")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "type"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name="Статус задачи")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "status"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Project(models.Model):
    date_started = models.DateField(verbose_name='Дата начала')
    date_ended = models.DateField(verbose_name='Дата окончания', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="Название проекта")
    description = models.TextField(max_length=1000, verbose_name="Описание проекта")

    def __str__(self):
        return f" {self.id} {self.name} {self.date_started} {self.date_ended}"

    class Meta:
        db_table = 'Project'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Task(models.Model):
    summary = models.CharField(max_length=50, verbose_name="Краткое описание")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Полное описание")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Статус")
    type = models.ManyToManyField(Type, verbose_name="Тип")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    added_date = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return f"{self.id} {self.summary} {self.status}"

    class Meta:
        db_table = "Task"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
