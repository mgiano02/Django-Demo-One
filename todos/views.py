from django.shortcuts import render, redirect
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
            return redirect(todo_list_detail, id=list_item.id)
    else:
        form = TodoListForm()

    context = {
        "form": form,
    }

    return render(request, "todos/create.html", context)
