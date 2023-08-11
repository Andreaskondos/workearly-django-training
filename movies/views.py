from django.shortcuts import render
from .models import Movie

# Create your views here.
def movie_detail_view(request, id = None):
    movie = None
    if id is not None:
     movie = Movie.objects.get(id=id)
     content = {
        "object": movie
    }
     
    return render(request, "movies/details.html", context=content)

def movie_search_view(request):
   query_dict = request.GET
   query = query_dict.get("query")
   
   try:
       query = int(query_dict.get("query"))
   except:
       query = None  
   movie = None
   if query is not None and query != 0:
       movie = Movie.objects.get(id=query)
       
   content = {
           "object": movie
       }
   return render(request, "movies/search.html", context=content)