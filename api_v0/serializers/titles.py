from rest_framework import serializers

from ..models.categories import Category
from ..models.genres import Genre
from ..models.titles import Title

from .genres import GenreSerializer
from .categories import CategorySerializer


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    genre = GenreSerializer()

    class Meta:
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre', 'category',)
