from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=300,
        verbose_name='Жанр',
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
        verbose_name='Адрес',
    )
