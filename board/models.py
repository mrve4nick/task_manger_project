from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="workers")


PRIORITY_CHOICES = (
    ("urgent", "URGENT PRIORITY"),
    ("high", "HIGH PRIORITY"),
    ("medium", "MEDIUM PRIORITY"),
    ("low", "LOW PRIORITY"),
)


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Task Types"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
        default="urgent",
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="assigned_tasks", blank=True)
