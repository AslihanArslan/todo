from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["item", "completed"]


def index(request):

        todos = Todo.objects.order_by('completed','created_at')
        return render(request, 'base.html', {'todos': todos})

def addItem(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)

        if form.is_valid():
            form.save()
            todos = Todo.objects.all
            messages.success(request, ('Item has been added to the list.'))
            return redirect('/')
        else:
            return render(request, 'addItem.html', {'error_msg': "Empty item"})

    else:
        todos = Todo.objects.all
        return render(request, 'addItem.html', {'todos': todos})

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.warning(request, 'Item has been deleted.')
    return redirect('/')


def todo_not_completed(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = False
    todo.save()
    return redirect('/')


def todo_completed(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('/')