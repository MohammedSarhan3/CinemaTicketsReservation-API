from django.urls import path
from .views import no_rest_no_model,norestfrommodel
urlpatterns = [
path('no_rest_no_model/',no_rest_no_model),
path('norestfrommodel/',norestfrommodel)    
]