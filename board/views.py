from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from board.forms import WorkerCreationForm, TaskCreationForm, WorkerUpdateForm
from board.models import Worker, Position, TaskType, Task
from board.forms import TaskTypeForm


class PositionListView(generic.ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "board/position_list.html"


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("board:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("board:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("board:position-list")


class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "board/worker_list.html"


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("board:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("board:worker-list")


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class TaskTypeListCreateView(LoginRequiredMixin, View):
    def get(self, request):
        task_types = TaskType.objects.all()
        form = TaskTypeForm()
        return render(request, 'board/tasktype_list.html', {'form': form, 'task_type_list': task_types})

    def post(self, request):
        form = TaskTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board:task-type-list-create')
        return render(request, 'board/tasktype_list.html', {'form': form, 'task_type_list': TaskType.objects.all()})


class TaskTypeDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        task_type = get_object_or_404(TaskType, pk=pk)
        form = TaskTypeForm(instance=task_type)
        return render(request, 'board/tasktype_detail.html', {'form': form, 'task_type': task_type})

    def post(self, request, pk):
        task_type = get_object_or_404(TaskType, pk=pk)

        if request.POST.get("delete") == "true":
            task_type.delete()
            return redirect("board:task-type-list-create")

        form = TaskTypeForm(request.POST, instance=task_type)
        if form.is_valid():
            form.save()
            return redirect('board:task-type-list-create')
        return render(request, 'board/tasktype_detail.html', {'form': form, 'task_type': task_type})


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "board/task_list.html"


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreationForm


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("board:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("board:task-list")


class IndexView(generic.TemplateView):
    template_name = "board/index.html"
