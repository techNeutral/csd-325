#Brett Fuller
#12/16/2024
#CSD 325  – Assignment 11.2

from django.db import models

# models from tutorlial

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)