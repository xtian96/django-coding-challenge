from rest_framework import serializers

from movies.models import Movie, Reviews


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'runtime', 'avg_rating']
    def get_runtime_formatted(self, obj):
        return obj.runtime_formatted()

    def get_avg_rating(self, obj):
        return obj.average_rating()