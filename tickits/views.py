from django.shortcuts import render
from .models import Guest
from django.http.response import JsonResponse


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

