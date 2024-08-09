from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from board.models import Worker, Task, TaskType


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "position",
        )


class TaskCreationForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Task
        fields = (
            "name",
            "description",
            "deadline",
            "is_completed",
            "priority",
            "task_type",
            "assignees",
        )
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local", }),
        }


class TaskTypeForm(forms.ModelForm):
    class Meta:
        model = TaskType
        fields = '__all__'
