from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse

# now to call the home function, we need to import it into the urls.py file
rooms=[
    {'id':1,'name':'Lets Learn Python'},
    {'id':2,'name':'Lets play Django'},
    {'id':3,'name':'lets play guitar'},
]

def home(request):
    context={'rooms':rooms} #this is a context dictionary
    return render(request,'base/home.html',context)             #base/home.html is the path to the home.html file. we dont need to add the template folder as django knows that it is in the template folder automatically. 
def room(request,pk):           #pk parameter is for dynamic routing
    room=None
    for i in rooms:
        if i['id']==int(pk):        #pk is a string so we need to convert it into an integer. and then we are comparing it with the id of the room dictionary. in dictionary, the id is an integer. this is how we access the id of the dictionary
            room=i

    context={'room':room}
    return render(request,'base/room.html',context) #now since this file is in the base folder in template, we need to add base/room.html. we dont need to add the template folder as django knows that it is in the template folder automatically.