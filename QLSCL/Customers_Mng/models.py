from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=225)
    gender = models.BooleanField()
    phone = models.CharField(max_length=255)
    
