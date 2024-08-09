from django.test import TestCase
from django.urls import reverse

from board.models import (
    Position,
    Worker,
    TaskType,
    Task,
)


class ModelsTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="testPosition")
        self.worker = Worker.objects.create(username="testWorker", position=self.position)
        self.task_type = TaskType.objects.create(name="testTaskType")
        self.task = Task.objects.create(name="testTask", description="test", deadline="2026-08-31 18:53:00", is_completed=False, priority="urgent", task_type=self.task_type)
        self.task.assignees.set([self.worker])

    def test_position_str(self):
        self.assertEqual(str(self.position), self.position.name)

    def test_worker_get_absolute_url(self):
        expected_url = reverse("board:worker-detail", kwargs={"pk": self.worker.pk})
        actual_url = self.worker.get_absolute_url()
        self.assertEqual(actual_url, expected_url)

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), self.task_type.name)

    def test_task_type_get_absolute_url(self):
        expected_url = reverse("board:task-detail", kwargs={"pk": self.task.pk})
        actual_url = self.task.get_absolute_url()
        self.assertEqual(actual_url, expected_url)
