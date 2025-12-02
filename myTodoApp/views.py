from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# from .models import todo
# Create your views here.
def home(request):
    return render(request, 'home.html')

def taskView(request):
    tasks = Task.objects.filter(isCompleted = False).order_by('-updatedAt')

    completed_tasks = Task.objects.filter(isCompleted = True)
    context = {
        "tasks":tasks,
        "completed_tasks":completed_tasks
               }
    return render(request, 'home.html', context)

# def completed(request):
#     tasks = Task.objects.filter(isCompleted = False)
#     tasks.iscompleted = True
#     return redirect('home')  

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect("home")

def markAsDone(request, pk):
    task  = get_object_or_404(Task, pk = pk)
    task.isCompleted = True
    task.save()
    return redirect('home')

def delete(request, pk):
    tasks  = get_object_or_404(Task, pk = pk)
    tasks.delete()
    return redirect('home')

def undone(request, pk):
    tasks = get_object_or_404(Task, pk = pk)
    tasks.isCompleted = False
    tasks.save()
    return redirect('home')

def edit(request, pk):
    getTask = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        newtask = request.POST['task']
        getTask.task = newtask
        getTask.save()
        return redirect('home')
    else:
        context = {
            "getTask":getTask,
        }
    return render(request, 'edit.html', context)