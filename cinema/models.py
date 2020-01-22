from django.db import models


# Create your models here.
class Customer(models.Model):
    titel = models.CharField(max_length=3)
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
