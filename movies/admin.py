from django.contrib import admin
from .models import Movie, Actor
# Register your models here.
class movieAdmin(admin.ModelAdmin):
    list_display=["title","id"]
    search_fields=["title", "content"]
admin.site.register(Movie, movieAdmin)
# admin.site.register(Actor)