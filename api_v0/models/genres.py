from django.db import models


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Жанр',
        max_length=300,
    )
    slug = models.SlugField(
        verbose_name='Адрес',
        unique=True,
        blank=True,
        null=True
    )
