import datetime

from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator

from ..models.review import Review
from ..models.titles import Title
from ..models.users import MyUser


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=MyUser.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    title = serializers.SlugRelatedField(
        queryset=Title.objects.all(),
        slug_field='id'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date', 'title')
        model = Review
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=['title', 'author'],
            )
        ]
