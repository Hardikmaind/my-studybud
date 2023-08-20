from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse/

# now to call the home function, we need to import it into the urls.py file

def home(request):
    return HttpResponse('Hello, World!')
def room(request):
    return HttpResponse('this is room')