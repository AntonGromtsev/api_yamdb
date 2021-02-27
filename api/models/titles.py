from django.db import models
from .genres import Genre
from .categories import Category

from django.core.validators import MinValueValidator
from .utils import current_year, max_value_current_year


class Title(models.Model):
    name = models.CharField(
        max_length=300,
        blank=False,
        verbose_name='Название',
    )
    year = models.PositiveIntegerField(
        default=current_year(),
        validators=[MinValueValidator(1700), max_value_current_year],
        db_index=True,
        verbose_name='Год',
    )
    description = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Описание',
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        null=True,
        verbose_name='Жанр',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Категория',
    )
