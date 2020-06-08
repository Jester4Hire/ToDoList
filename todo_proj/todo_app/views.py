from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

def index(request):

    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)


def delete_view(request, id):
    context = {}

    obj = get_object_or_404(GeeksModel, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)


def list_view(request):
   context = {}
   context["dataset"] = Todo.objects.all()

   return render(request, "list_view.html", context)


def detail_view(request, id):
    
    context = {}
    context["data"] = Todo.objects.get(id=id)

    return render(request, "detail_view.html", context)


def detail_view(request, id):
    context = {}
    context["data"] = Todo.objects.get(id=id)

    return render(request, "detail_view.html", context)


def update_view(request, id):
    context = {}
    obj = get_object_or_404(Todo, id=id)

    form = TodoForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    context["form"] = form

    return render(request, "update_view.html", context)
