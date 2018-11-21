from django.db import models

# Create your models here.
class Employee(models.Model):
    E_NO=models.IntegerField()
    E_NAME=models.CharField(max_length=64)
    E_SAL=models.FloatField()
    E_ADDRESS=models.CharField(max_length=64)

