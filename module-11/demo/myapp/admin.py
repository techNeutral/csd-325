#Brett Fuller
#12/16/2024
#CSD 325  – Assignment 11.2

from django.contrib import admin
from .models import TodoItem

# registered todo list model.
admin.site.register(TodoItem)