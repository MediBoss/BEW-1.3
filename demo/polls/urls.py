from django.urls import path # importing the path module 
from . import views # importing the views from the current directory

# URL configuration
urlpatterns = [ 
    # endpoint for home page
    path('', views.index, name="index"),
    # endpoint for question detail
    path('<int:question_id>/', views.detail, name='detail'),
    # endpoint for question resuts
    path('<int:question_id>/results/', views.results, name='results'),
    # endpoint for question votes
    path('<int:question_id>/vote/', views.vote, name='vote'),
]