from django.contrib import admin

from webapp.models import Task, Type, Status, Project


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['date_started', 'date_ended', 'name']
    # readonly_fields = ['added_date', 'updated_date']
    search_fields = ['id', 'name']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status']
    list_display_links = ['id', 'summary', 'status']
    list_filter = ['status', 'type']
    readonly_fields = ['added_date', 'updated_date']
    search_fields = ['id', 'summary', 'status']


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


admin.site.register(Task, TaskAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Project, ProjectAdmin)
