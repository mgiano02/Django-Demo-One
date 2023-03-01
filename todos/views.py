from django.shortcuts import render
from todos.models import TodoList


# Create your views here.
def todo_list_list(request):
    todo_list = TodoList.objects.all()
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todos/list.html", context)
