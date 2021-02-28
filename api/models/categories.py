from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300, verbose_name='Категория')
    slug = models.SlugField(unique=True, verbose_name='Адрес')
