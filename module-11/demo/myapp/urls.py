#Brett Fuller
#12/16/2024
#CSD 325  – Assignment 11.2

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.homeTemplate, name="home"),
    path("todos/", views.todos, name="Todos")
]