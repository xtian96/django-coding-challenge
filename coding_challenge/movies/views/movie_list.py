from django.views.generic import ListView
from django.shortcuts import redirect
from django.db.models import Avg
from movies.models.movie import Movie
from movies.models.review import Review
from movies.forms.review_form import ReviewForm

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'
    paginate_by = 10  # Number of movies per page

    def get_queryset(self):
        queryset = super().get_queryset()
        runtime_filter = self.request.GET.get('runtime')
        sort_by = self.request.GET.get('sort_by')

        if runtime_filter:
            if runtime_filter.startswith('>'):
                queryset = queryset.filter(runtime__gt=int(runtime_filter[1:]))
            elif runtime_filter.startswith('<'):
                queryset = queryset.filter(runtime__lt=int(runtime_filter[1:]))

        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for movie in context['movies']:
            movie.latest_reviews = list(movie.reviews.order_by('-id')[:5])  # Get the latest 5 reviews
            hours, minutes = divmod(movie.runtime, 60)
            movie.runtime_formatted = f"{hours}h {minutes:02d}m"
            movie.avg_rating = movie.reviews.aggregate(Avg('rating'))['rating__avg'] or 0
        context['review_form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('movies')  # Redirect to the movie list view after form submission