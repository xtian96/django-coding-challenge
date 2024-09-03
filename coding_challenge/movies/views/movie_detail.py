from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.db.models import Avg
from movies.models.movie import Movie
from movies.models.review import Review

class MovieDetailView(View):
    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        reviews = movie.reviews.all()
        reviews_data = [{'rating': review.rating, 'name': review.name} for review in reviews]
        hours, minutes = divmod(movie.runtime, 60)
        runtime_formatted = f"{hours}:{minutes:02d}"
        avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
        data = {
            'id': movie.id,
            'title': movie.title,
            'release_date': movie.release_date,
            'runtime': movie.runtime,
            'runtime_formatted': runtime_formatted,
            'avg_rating': avg_rating,
            'reviews': reviews_data
        }
        return JsonResponse(data)

    def put(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.title = request.POST.get('title')
        movie.release_date = request.POST.get('release_date')
        movie.runtime = request.POST.get('runtime')
        movie.save()
        return JsonResponse({'message': 'Movie updated successfully'})

    def patch(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        if 'title' in request.POST:
            movie.title = request.POST.get('title')        
        if 'release_date' in request.POST:
            movie.release_date = request.POST.get('release_date')
        if 'runtime' in request.POST:
            movie.runtime = request.POST.get('runtime')
        movie.save()
        return JsonResponse({'message': 'Movie updated successfully'})

    def delete(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return JsonResponse({'message': 'Movie deleted successfully'})
