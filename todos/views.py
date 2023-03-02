from django.shortcuts import render, redirect, get_object_or_404
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm


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


def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            list_item = form.save()
            return redirect("todo_list_detail", id=list_item.id)
    else:
        form = TodoListForm()

    context = {
        "form": form,
    }

    return render(request, "todos/create.html", context)


def todo_list_update(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            todo_list = form.save()
            return redirect("todo_list_detail", id=todo_list.id)
    else:
        form = TodoListForm(instance=todo_list)

    context = {
        "todo_list": todo_list,
        "form": form,
    }

    return render(request, "todos/update.html", context)
