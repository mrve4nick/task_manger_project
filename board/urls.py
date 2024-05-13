from django.contrib import admin
from django.urls import path

from board.views import (
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    WorkerListView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    WorkerDetailView,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("board/positions/", PositionListView.as_view(), name="position-list"),
    path("board/positions/create/", PositionCreateView.as_view(), name="position-create"),
    path("board/positions/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("board/positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
    path("board/workers/", WorkerListView.as_view(), name="worker-list"),
    path("board/workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("board/workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("board/workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("board/workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("board/task-type/", TaskTypeListView.as_view(), name="task-type-list"),
    path("board/task-type/create/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path("board/task-type/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-type-update"),
    path("board/task-type/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task-type-delete"),
    path("board/task/", TaskListView.as_view(), name="task-list"),
    path("board/task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("board/task/create/", TaskCreateView.as_view(), name="task-create"),
    path("board/task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("board/task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
]

app_name = "board"
