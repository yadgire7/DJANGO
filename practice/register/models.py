from django.db import models

# Create your models here.
class register(models.Model):
    fName=models.TextField()
    lName=models.TextField()
    email=models.EmailField()