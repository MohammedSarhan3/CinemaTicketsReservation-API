from django.urls import path
from .views import no_rest_no_model,norestfrommodel,FBV_List,FBV_PK
urlpatterns = [
path('no_rest_no_model/',no_rest_no_model),
path('norestfrommodel/',norestfrommodel),
path('FBV_List/',FBV_List),
path('FBV_PK/<int:pk>',FBV_PK),
]