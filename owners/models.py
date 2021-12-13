from django.db import models

# Create your models here.

class Owners(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    age = models.DecimalField(max_digits=3, decimal_places=0)

    class Meta:
        db_table = 'owners'

class Dogs(models.Model):
    owner = models.ForeignKey('Owners', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.DecimalField(max_digits=3, decimal_places=0)

    class Meta:
        db_table = 'dogs'

