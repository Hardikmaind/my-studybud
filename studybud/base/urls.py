#  this urls.py in this app is going to be for this base app
from
from . import views     #this is importing the views.py file from the base app
urlpatterns = [
    path('', views.home),   #when the user goes to the home page, the home function is called
]
