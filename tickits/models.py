from django.db import models


class Movie(models.Model):
    hall = models.CharField(max_length=10,blank=True,null=True)
    movie = models.CharField(max_length=10,blank=True,null=True)
    date = models.DateField(blank=True,null=True)


class Guest(models.Model):
    name = models.CharField(max_length=10,blank=True,null=True)
    mobile = models.CharField(max_length=10,blank=True,null=True)


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name='reservation', on_delete=models.CASCADE,blank=True,null=True )
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE ,blank=True,null=True)
