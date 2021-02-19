from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)

    #надо ли сюда Meta?
    
