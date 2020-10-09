from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import *
# Create your views here.
def todoHome(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todo')
    return render(request,'todoHome.html',{'tasks':tasks, 'form':form})

def portfolio(request):
    return render(request,'portfolio.html')

def updateTask(request,pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('/todo')
    return render(request,'update_task.html',{'form':form})

def deleteTask(request,pk):
    item = Task.objects.get(id = pk)
    if request.method == "POST":
        item.delete()
        return redirect('/todo')
    return render(request,'delete_task.html',{'item':item})