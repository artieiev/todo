from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    context = {
        'title': 'ToDo',
        'tasks': tasks,
    }
    return render(request, 'main/index.html', context)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не валидна'
    form = TaskForm()
    context = {'title': 'ToDo', 'form': form, 'error': error}
    return render(request, 'main/create.html', context)


def task_del(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
