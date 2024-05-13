from django.contrib import admin
from django.urls import path

from board.views import (
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("board/positions/", PositionListView.as_view(), name="position-list"),
    path("board/positions/create", PositionCreateView.as_view(), name="position-create"),
    path("board/positions/<int:pk>/update", PositionUpdateView.as_view(), name="position-update"),
    path("board/positions/<int:pk>/delete", PositionDeleteView.as_view(), name="position-delete"),

]

app_name = "board"
