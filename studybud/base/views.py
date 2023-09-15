from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from .models import Room        #first we import the model that we want to query

# now to call the home function, we need to import it into the urls.py file
# rooms=[
#     {'id':1,'name':'Lets Learn Python'},
#     {'id':2,'name':'Lets play Django'},
#     {'id':3,'name':'lets play guitar'},
# ]

def home(request):
    # .object blow is the modal manager in django
    # this below works after quring db because by dafault we have ids genrated for them from 1
    rooms=Room.objects.all()    #this is how we query the database. we are getting all the objects from the Room model. we are storing it in a variable called rooms. this is a list of objects. we can iterate through this list and get the objects one by one.               
    context={'rooms':rooms} #this is a context dictionary....now here the rooms will be from the database and not from the above rooms list.
    return render(request,'base/home.html',context)             #base/home.html is the path to the home.html file. we dont need to add the template folder as django knows that it is in the template folder automatically. 
def room(request,pk):           #pk parameter is for dynamic routing
        room =Room.objects.get(id=pk)        #now we need to get this by unique value ..becaule if we have two value with same value like name,it gonna throw an erroe

        context={'room':room}
        return render(request,'base/room.html',context) #now since this file is in the base folder in template, we need to add base/room.html. we dont need to add the template folder as django knows that it is in the template folder automatically.