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
    return render(request,'home.html',context)
def room(request):
    return render(request,'room.html')