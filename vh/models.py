from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=10)
    address = models.TextField()
