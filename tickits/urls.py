from django.urls import path,include
from .views import no_rest_no_model,norestfrommodel,FBV_List,FBV_PK,CBV_List,CBV_pk,generics_list
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('no_rest_no_model/',no_rest_no_model),
    path('norestfrommodel/',norestfrommodel),
    path('FBV_List/',FBV_List),
    path('FBV_PK/<int:pk>',FBV_PK),
    path('CBV_List',CBV_List.as_view()),
    path('CBV_pk/<int:pk>',CBV_pk.as_view()),
    path('generics_list',generics_list.as_view()),

    path('api-auth',include('rest_framework.urls')),
    path('api-token',obtain_auth_token),


]