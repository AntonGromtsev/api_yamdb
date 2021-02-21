from rest_framework import serializers

from ..models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')


    class Meta:
        fields = '__all__'
        model = Review
