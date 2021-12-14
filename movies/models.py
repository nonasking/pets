from django.db import models

# Create your models here.

class Actors(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    movies = models.ManyToManyField('Movies', related_name='movies')
    class Meta:
        db_table = 'actors'

class Movies(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    running_time = models.DecimalField(max_digits=4, decimal_places=0)
    class Meta:
        db_table = 'movies'
