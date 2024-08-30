from rest_framework import serializers
from movies.models import Reviews

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('name', 'rating')