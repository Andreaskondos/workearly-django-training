from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.TextField()
    content = models.TextField()

class Actor(models.Model):
    name = models.TextField()
    surname = models.TextField()
