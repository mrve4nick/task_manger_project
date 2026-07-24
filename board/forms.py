from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.password_validation import validate_password
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


class WorkerUpdateForm(forms.ModelForm):
    password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput,
        required=False,
    )
    password2 = forms.CharField(
        label="Confirm new password",
        widget=forms.PasswordInput,
        required=False,
    )

    class Meta:
        model = Worker
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "position",
            "password1",
            "password2",
        )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 or password2:
            if password1 != password2:
                raise ValidationError("Passwords don't match")

            validate_password(password1, self.instance)

        return cleaned_data

    def save(self, commit=True):
        worker = super.save(commit=False)
        password = self.cleaned_data.get("password1")

        if password:
            worker.set_password(password)

        if commit:
            worker.save()

        return worker


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
