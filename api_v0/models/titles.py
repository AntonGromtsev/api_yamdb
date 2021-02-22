from django.db import models
from .genres import Genre
from .categories import Category


class Title(models.Model):
    name = models.CharField(max_length=300, blank=False)
    year = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    rating = models.IntegerField(null=True)
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        blank=True, null=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        blank=True, null=True, verbose_name='Категория'
    )
