from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from . forms import TaskForm
from . models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all().order_by('-id')
    return render(request, 'tasks/index.html', {'tasks' : tasks})

def add_task(request):
    if request.method != 'POST':
        form = TaskForm()
        return render(request, 'tasks/add_task.html', {'form': form})
    
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('index')

def drop_task(request, pk):
    Task.objects.filter(id=pk).delete()
    return redirect('index')

def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            #messages.success(request, "Contato alterado com sucesso!")
            return redirect('index')
        else:
            #messages.error(request, 'Erro ao editar contato, tente novamente.')
            return render(request, 'tasks/edit_task.html', {'form': form, 'task' : task})
    else: 
        return render(request, 'tasks/edit_task.html', {'form': form, 'task' : task})