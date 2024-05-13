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
    WorkerDetailView
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
]

app_name = "board"
