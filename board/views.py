from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from board.forms import WorkerCreationForm
from board.models import Worker, Position


class PositionListView(generic.ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "board/position_list.html"


class PositionCreateView(generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("board:position-list")


class PositionUpdateView(generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("board:position-list")


class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("board:position-list")


class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "board/worker_list.html"


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm


class WorkerUpdateView(generic.UpdateView):
    model = Worker
    form_class = WorkerCreationForm


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("board:worker-list")

