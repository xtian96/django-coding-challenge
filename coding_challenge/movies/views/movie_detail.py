from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
from movies.models import Movie, Reviews

class MovieDetailView(View):
    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        reviews = movie.reviews.all()
        data = {
            'id': movie.id,
            'title': movie.title,
            'director': movie.director,
            'release_date': movie.release_date,
            'runtime_formatted': movie.runtime_formatted(),
            'avg_rating': movie.avg_rating(),
            'reviews': [{'name': review.name, 'rating': review.rating} for review in reviews]
        }
        return JsonResponse(data)

    def put(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.title = request.POST.get('title')
        movie.director = request.POST.get('director')
        movie.release_date = request.POST.get('release_date')
        movie.runtime = request.POST.get('runtime')
        movie.save()
        return JsonResponse({'message': 'Movie updated successfully'})

    def patch(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        if 'title' in request.POST:
            movie.title = request.POST.get('title')
        if 'director' in request.POST:
            movie.director = request.POST.get('director')
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
