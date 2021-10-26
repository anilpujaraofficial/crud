from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)