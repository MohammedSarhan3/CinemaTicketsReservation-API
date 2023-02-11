from django.shortcuts import render
from .models import Guest
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins, viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

def no_rest_no_model(requset):
    gests=[
        {
            'id':1,
            "name":"mohammed",
            "number": '00125877',
        },
        {
            'id':2,
            "name":"ahmed",
            "number": '15988744',
        }
    ]

    return JsonResponse(gests,safe=False)
    

def norestfrommodel(request):
    data= Guest.objects.all()
    response={'guests':list(data.values('name','mobile'))}

    return JsonResponse(response)

@api_view(['GET','POST'])
def FBV_List(request):
    # GET
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = GuestSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def FBV_PK(request,pk):
    guests = Guest.objects.get(pk=pk)
    # GET
    if request.method == 'GET':
       
        serializer = GuestSerializer(guests)
        return Response(serializer.data)
    # POST
    elif request.method == 'PUT':
        serializer = GuestSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
     # DELETE
    if request.method == 'DELETE':
        guests.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)