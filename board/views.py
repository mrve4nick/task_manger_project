from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from board.forms import WorkerCreationForm, TaskCreationForm
from board.models import Worker, Position, TaskType, Task
from board.forms import TaskTypeForm


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


class WorkerDetailView(generic.DetailView):
    model = Worker


class TaskTypeListCreateView(View):
    def get(self, request):
        task_types = TaskType.objects.all()
        return render(request, 'board/tasktype_list.html', {'task_type_list': task_types})

    def post(self, request):
        form = TaskTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board:task-type-list-create')
        return render(request, 'board/tasktype_list.html', {'form': form, 'task_type_list': TaskType.objects.all()})


class TaskTypeDetailView(View):
    def get(self, request, pk):
        task_type = get_object_or_404(TaskType, pk=pk)
        form = TaskTypeForm(instance=task_type)
        return render(request, 'board/tasktype_detail.html', {'form': form, 'task_type': task_type})

    def post(self, request, pk):
        task_type = get_object_or_404(TaskType, pk=pk)
        if 'delete' in request.POST:
            task_type.delete()
            return redirect('board:task-type-list-create')
        else:
            form = TaskTypeForm(request.POST, instance=task_type)
            if form.is_valid():
                form.save()
                return redirect('board:task-type-list-create')
            return render(request, 'board/tasktype_detail.html', {'form': form, 'task_type': task_type})


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "board/task_list.html"


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreationForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("board:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("board:task-list")


class IndexView(generic.TemplateView):
    template_name = "board/index.html"
