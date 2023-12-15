from django.shortcuts import render
from .models import Task

def home(request):
    todo_tasks = Task.objects.filter(is_completed=False)
    context = {'todo_tasks': todo_tasks}
    return render(request, "home.html", context)
