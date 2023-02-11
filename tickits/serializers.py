from rest_framework import routers, serializers, viewsets
from .models import Movie,Guest,Reservation

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guest
        fields = [ 'reservation', 'name', 'mobile']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'

       