from rest_framework import routers, serializers, viewsets
from .models import Movie,Guest,Reservation

class MovieSerlizer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'


class GuestSelizer(serializers.ModelSerializer):
    class Meta:
        model=Guest
        fields = [ 'reservation', 'name', 'mobile']

class ReservationSelizer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'

       