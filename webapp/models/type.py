from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип задачи")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "type"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"
