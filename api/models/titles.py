from django.db import models
from .genres import Genre
from .categories import Category

from django.core.validators import MinValueValidator
from .utils import current_year, max_value_current_year


class Title(models.Model):
    name = models.CharField(max_length=300, blank=False)
    year = models.PositiveIntegerField(default=current_year(),
                                       verbose_name='Год',
                                       validators=[MinValueValidator(1700),
                                                   max_value_current_year],
                                       db_index=True)
    description = models.CharField(max_length=1000, blank=True)
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Категория'
    )
