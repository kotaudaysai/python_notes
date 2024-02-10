from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    hotel = models.CharField(max_length=70)
    review = models.CharField(max_length=10000)
    result = models.CharField(max_length=20)
