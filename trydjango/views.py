from django.http import HttpResponse
from django.template.loader import render_to_string
from movies.models import Movie, Actor
import random

name = "Bellamy"

def home_view(request):
    rand_int = random.randint(1,Movie.objects.count())
    movie = Movie.objects.get(id=rand_int)
    movie_queryset = Movie.objects.all()
    content = {
        "movie_list": movie_queryset,
        "id": rand_int,
        "title": movie.title,
        "description": movie.content,
    }
    HTML_STRING = render_to_string("home-view.html", context=content)
    return HttpResponse(HTML_STRING)
    
    
    