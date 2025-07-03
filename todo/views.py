from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    form = TaskForm()
    tasks = Task.objects.all()

    if request.method =="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    
    context = {"tasks": tasks, "TaskForm": form}
    return render(request, 'index.html', context)

def update(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method =="POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {"TaskForm": form}
    return render(request, 'update.html', context)

def delete(request, pk):
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context = {"task": task}
    return render(request, 'delete.html', context)    