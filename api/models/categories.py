from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300, verbose_name='Категория')
    slug = models.SlugField(verbose_name='Адрес', unique=True)
