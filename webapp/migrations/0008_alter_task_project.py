# Generated by Django 5.0.7 on 2024-07-22 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_task_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='tasks', to='webapp.project', verbose_name='Проект'),
        ),
    ]
