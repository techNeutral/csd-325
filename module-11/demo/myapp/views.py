from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return HttpResponse("Fuller Says Hello!")
    #return(render(request, "home.html"))

def homeTemplate(request):
    return(render(request, "home.html"))

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})
