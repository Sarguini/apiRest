from django.db import models

# Create your models here.

class Meteor(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField(max_length=7)
    image = models.CharField(max_length=255)
    price = models.FloatField(max_length=10)