from django.db import models

# Create your models here.



class Camara(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    port = models.CharField(max_length=20,unique=True)