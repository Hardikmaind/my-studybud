#  this urls.py in this app is going to be for this base app
from django.urls import path
from . import views     #this is importing the views.py file from the base app
urlpatterns = [
    path('', views.home,name="home"),   #when the user goes to the home page, the home function is called
    path('room/', views.room,name="room"),   #when the user goes to the home page, the home function is called 
]
