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
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    IndexView,
    TaskTypeListCreateView,
    TaskTypeDetailView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
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
    path("board/task/", TaskListView.as_view(), name="task-list"),
    path("board/task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("board/task/create/", TaskCreateView.as_view(), name="task-create"),
    path("board/task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("board/task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path('task-type/', TaskTypeListCreateView.as_view(), name='task-type-list-create'),
    path('task-type/<int:pk>/', TaskTypeDetailView.as_view(), name='task-type-detail'),
]

app_name = "board"
