from django.db import models

# Create your models here.

class curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()


