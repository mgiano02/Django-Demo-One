from django.shortcuts import render, redirect
from todos.models import TodoList, TodoItem


# Create your views here.
def todo_list_list(request):
    todo_list = TodoList.objects.all()
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    list_item = TodoList.objects.get(id=id)
    context = {
        "list_object": list_item,
    }
    return render(request, "todos/detail.html", context)
