# this urls .py is going to be for the entire project
from django.contrib import admin
from django.urls import path



# since our project is big, we are going to create an app called base and all the urls will be in the base app and the views will be in the base app

# from django.http.response import HttpResponse

# def home(request):
#     return HttpResponse('Hello, World!')
# def room(request):
#     return HttpResponse('this is room')

    #url triggers a function or view






urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),     #when the user goes to the home page, the home function is called
    path('room/', room),     #when the user goes to the home page, the home function is called
]
