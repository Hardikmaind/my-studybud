from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse

# now to call the home function, we need to import it into the urls.py file

def home(request):
    return render(request,'home.html')
def room(request):
    return render(request,'room.html')