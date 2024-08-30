from rest_framework.generics import ListCreateAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer

class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.order_by("id")
    serializer_class = MovieSerializer

    def filter_by_runtime(self):
        queryset = super().filter_by_runtime()
        runtime_filter = self.request.query_params.get('runtime')
        if runtime_filter:
            if runtime_filter.startswith('>'):
                queryset = queryset.filter(runtime__gt=int(runtime_filter[1:]))
            elif runtime_filter.startswith('<'):
                queryset = queryset.filter(runtime__lt=int(runtime_filter[1:]))
        return queryset