from django.contrib import admin
from .models import Position, Worker, TaskType, Task


class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class WorkerAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "position")
    search_fields = ("username", "email", "position__name")
    list_filter = ("position",)


class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "deadline", "is_completed", "priority", "task_type")
    search_fields = ("name", "description", "task_type__name")
    list_filter = ("is_completed", "priority", "task_type")
    filter_horizontal = ("assignees",)


admin.site.register(Position, PositionAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(TaskType, TaskTypeAdmin)
admin.site.register(Task, TaskAdmin)
