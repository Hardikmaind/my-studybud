from django.shortcuts import render,redirect

from .forms import RoomForm 

# Create your views here.
from django.http.response import HttpResponse
from .models import Room ,Topic     #first we import the model that we want to query

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
    
    
    topics=Topic.objects.all()  
    
               
    context={'rooms':rooms,'topics':topics} #this is a context dictionary....now here the rooms will be from the database and not from the above rooms list.
    return render(request,'base/home.html',context)             #base/home.html is the path to the home.html file. we dont need to add the template folder as django knows that it is in the template folder automatically. 



# Primary Keys
# Every table should have a primary key, so every model should have a primary key field. However, you do not have to do this manually if you do not want. By default, Django adds an id field to each model, which is used as the primary key for that model. You can create your own primary key field by adding the keyword arg primary_key=True to a field. If you add your own primary key field, the automatic one will not be added.

# class Garden(models.Model):
#     garden_id = models.IntegerField(primary_key=True)






def room(request,pk):           #pk parameter is for dynamic routing
    room =Room.objects.get(id=pk)        #now we need to get this by unique value ..becaule if we have two value with same value like name,it gonna throw an erroe

    context={'room':room}
    return render(request,'base/room.html',context) #now since this file is in the base folder in template, we need to add base/room.html. we dont need to add the template folder as django knows that it is in the template folder automatically.
 
def createRoom(request):
    form=RoomForm()     #yaha pe form laya hai form.py se
    if request.method=='POST':
        # print(request.POST) #this will print the data that we have submitted in the form in terminal

        # passing all the post data into the form
        form=RoomForm(request.POST) #this means that we are passing the data that we have submitted in the form to the RoomForm() class in forms.py. the RoomForm() class will validate the data and return it to us. the form knows what fields to expect because we have defined it in the RoomForm() class in forms.py.
        if form.is_valid(): #this will check if the form is valid or not
            form.save() #this will save the form in the database 
            return redirect('home') #this wcccill redirect us to the home page...we need to import redirect from django.shortcuts and in parenthesis i have access the url in this case 'home' by its name in urls.py


            # now afer submitting the form we will be redirected to the home page. and we will see the updated rooms there

    return render(request,'base/room_form.html',context={'form':form}) #yaha pe content se form pass kiya hai directly in room_form.html 




    # NOw we will do the crud operation ..for this lets create the views


    # we need to pass the request and pk parameter to the updateRoom function because we are gonna be updating the room with the id=pk
def updateRoom(request,pk):
    room=Room.objects.get(id=pk)        #now we need to get this by unique value ..becaule if we have two value with same value like name,it gonna throw an erroe
    form=RoomForm(instance=room)        #here we are passing the instance of the room to the RoomForm() class in forms.py. the RoomForm() class will validate the data and return it to us. the form knows what fields to expect because we have defined it in the RoomForm() class in forms.py.
    if(request.method=='POST'):
         form=RoomForm(request.POST,instance=room)   #here we are passing the request.post data which wuill replace the prefill form with data instance=room(wahtever that is in the database)
         if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context) #yaha pe content se form pass kiya hai directly in room_form.html


# this below methoid is for deleting the room directly from the home page
# created by me

# def deleteRoom(request,pk):
#     room=Room.objects.get(id=pk)
#     # if(request.method=='POST'):
#     room.delete() 
#     return redirect('home')
#     context={'object':room}
#     return render(request,'base/delete.html',context) #yaha pe content se form pass kiya hai directly in room_form.html


def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(request.POST)
    if(request.method=='POST'):
        room.delete()       #this will delete the room from the database
        return redirect('home')
    
    return render(request,'base/delete.html',context={'obj':room})
    
    # in this below way also can we return the form
    # return render(request=request,template_name='base/delete.html',context={'obj':room})