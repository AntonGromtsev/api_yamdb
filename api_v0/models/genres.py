from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
