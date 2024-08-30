from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    runtime = models.PositiveIntegerField()
    release_date = models.DateField()
    average_rating = models.FloatField(blank=True, null=True)
    @property
    def runtime_formatted(self):
        hours, minutes = divmod(self.runtime, 60)
        return f"{hours}:{minutes:02d}"
    
    @property
    def average_rating(self):
        return self.review.aggregate(models.Avg('rating'))['rating__avg']

    
class Reviews(models.Model):
    movie = models.ForeignKey('Movie', related_name='review', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    rating = models.IntegerField()