#  this urls.py in this app is going to be for this base app
from django.urls import path
from . import views     #this is importing the views.py file from the base app
urlpatterns = [
    path('', views.home,name="home"),   #when the user goes to the home page, the home function is called..which is in the views.py file


      #pk parameter is for dynamic routing.it is a primary key
    path('room/<str:pk>', views.room,name="room"),   #when the user goes to the home page, the home function is called 



    # people pass it int into url. abov ei have passed the pk as a string
    #     path('room/<slug:pk>', views.room,name="room"), 
]
