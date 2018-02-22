from django.shortcuts import render
from .models import Movies

# Create your views here.
def home(request):
    movies = Movies()
    movies.updateMovies()
    return render(request, 'index.html')

def cinema(request):
    filmes = Movies.objects.all()
    return render(request, 'cinema.html', {'movies' : filmes} )
