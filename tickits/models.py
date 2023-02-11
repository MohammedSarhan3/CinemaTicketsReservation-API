from django.db import models


class Movie(models.Model):
    hall = models.CharField(max_length=10,blank=True,null=True)
    movie = models.CharField(max_length=10,blank=True,null=True)
    date = models.DateField(blank=True,null=True)


