from django.db import models
import tmdbsimple as tmdb
# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    poster = models.TextField()
    description = models.TextField(default='descricao')
    original = models.CharField(max_length=50, default='original')


    def __str__(self):
        return self.name

    def updateMovies(self):
        Movies.objects.all().delete()
        tmdb.API_KEY = '6dda449109ac5a36f1c93aa3b3f12738'
        movies = tmdb.Movies()
        page = movies.now_playing(page=1, region='BR', language='pt-BR')['results']
        for item in page:
            movie = Movies(name=item['title'], rating=item['vote_average'], poster='https://image.tmdb.org/t/p/w300'+item['poster_path'], description=item['overview'], original=item['original_title'] )
            movie.save()
