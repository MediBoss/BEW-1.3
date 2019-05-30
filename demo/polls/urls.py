from django.urls import path # importing the path module 
from . import views # importing the views from the current directory

# URL configuration
urlpatterns = [ 
    path('', views.index, name="index")
]