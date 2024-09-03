from django.db import models
from movies.models.movie import Movie
class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    name = models.TextField()
    rating = models.IntegerField()
    

    class Meta:
        db_table = 'movies_review'