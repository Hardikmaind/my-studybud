from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q
from .forms import RoomForm 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Room ,Topic     #first we import the model that we want to query

# Create your views here.


# now to call the home function, we need to import it into the urls.py file
# rooms=[
#     {'id':1,'name':'Lets Learn Python'},
#     {'id':2,'name':'Lets play Django'},
#     {'id':3,'name':'lets play guitar'},
# ]


# Q() is used to create complex queries. It allows you to use | (OR) and & (AND) operators to combine conditions
# topic__name__icontains=q is a lookup expression. It means you're querying the Room model for objects where the related Topic's name contains (case-insensitive) the value of q.
# name__icontains=q is querying the Room model for objects where the name field contains (case-insensitive) the value of q.
# In simpler terms, this query is looking for rooms where either the related Topic's name contains the value of q or the room's own name field contains the value of q. The icontains is for case-insensitive matching.

# The double underscores are used to navigate relationships between models and perform field lookups, as explained in the previous message.


def home(request):
    # .object blow is the modal manager in django
    # this below works after quring db because by dafault we have ids genrated for them from 1

    # rooms=Room.objects.all()    #this is how we query the database. we are getting all the objects from the Room model. we are storing it in a variable called rooms. this is a list of objects. we can iterate through this list and get the objects one by one.    

    #"result = x if condition else y"    this is the ternary condition in python
    q=request.GET.get('query') if request.GET.get('query')!=None  else '' #ye "query" home.html mein hai..wwhen clicked on the href link it will send the query to the url and then we will get the query here....we are getting the query from the url and storing it in a variable called q 
    # now sometime we want to add the multiple parameter below..so to use "and" and "or" we need to import Q from django.db.models see above i have imported it. then i have to wrap the below in Q() and use the | and & operator..simple
    # rooms=Room.objects.filter(topic__name__icontains=q)
    
    
    # ismein apan ne room modal mein topic ko liye..then topic mein query upward in hte parent kiye..i.w name in topic model then checked whether it contains the query or not.
    rooms=Room.objects.filter(Q(topic__name__icontains=q) | Q (name__icontains=q)|Q(description__icontains=q))
    
    # in python we can get length of list by wrapping it inside len() .function  but .count(), is used to get the length of the query ...this is ,much faster
    room_count=rooms.count()    #this will count the number of rooms in the database 
    
    #this is how we filter the object data from the database. "topic__name__icontains"  filters the ojects which contains "q" in them  ..in this  "i" denotes case-sensitive ness...if i removed the i ..means it is case insensitive
    # 
    topics=Topic.objects.all()  
    
    #    yaha se apan ne context dict home.html mein bhejo hain ...jaha home.html mein apan ne loops ki help se waha rendere kiya hain
    context={'rooms':rooms,'topics':topics,'room_count':room_count} #this is a context dictionary....now here the rooms will be from the database and not from the above rooms list.
    return render(request,'base/home.html',context)             #base/home.html is the path to the home.html file. we dont need to add the template folder as django knows that it is in the template folder automatically. 


# Primary Keys
# Every table should have a primary key, so every model should have a primary key field. However, you do not have to do this manually if you do not want. By default, Django adds an id field to each model, which is used as the primary key for that model. You can create your own primary key field by adding the keyword arg primary_key=True to a field. If you add your own primary key field, the automatic one will not be added.

# class Garden(models.Model):
#     garden_id = models.IntegerField(primary_key=True)






def room(request,pk):           #pk parameter is for dynamic routing
    room =Room.objects.get(id=pk)        #now we need to get this by unique value ..becaule if we have two value with same value like name,it gonna throw an erroe

    context={'room':room}
    return render(request,'base/room.html',context) #now since this file is in the base folder in template, we need to add base/room.html. we dont need to add the template folder as django knows that it is in the template folder automatically.








# now i wanna restrict the user from accessing some pages based on the status of where the user is logged or logged out. for this we use mixins for classbased views and decorators for function based views. also middleware is used for this purpose

# now i am gonna restrict the create page

# @login_required() #this is a decorator..we just have to add this..but it will not work..we need to add the login_url parameter in it or this will throw an error "page not found 404"

@login_required(login_url='login') #this is a decorator. this will check if the user is logged in or not. if the user is not logged in then it will redirect the user to the login page. we need to import login_required from django.contrib.auth.decorators 
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
@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(request.POST)
    if(request.method=='POST'):
        room.delete()       #this will delete the room from the database
        return redirect('home')
    
    return render(request,'base/delete.html',context={'obj':room})
    
    # in this below way also can we return the form
    # return render(request=request,template_name='base/delete.html',context={'obj':room})

#dont use login as a function name as it is a inbuilt function in django which we will be using
def loginPage(request):
    
    if request.method=='POST':
        userid=request.POST.get('username')
        password=request.POST.get('password')
        try:
            # explainnation of the below line
            
#             User.objects is a manager for the User model. It provides an interface for querying the database and performing operations on the User model.

# .get() is a method provided by the manager. It's used for retrieving a single object from the database that matches the specified conditions.

# username=userid is specifying the condition for the query. It's saying, "Retrieve a user object where the username field is equal to the value stored in the variable userid."

# So, in essence, this line is trying to retrieve a user from the database whose username matches the one provided in the userid variable. If such a user exists, it will be stored in the variable user. If not, it will raise an exception (which you've handled with a try and except block).
            user=User.objects.get(username=userid)
        except:     # if te user does not exist below block  ..this is how we handle the error in django
            messages.error(request,'User does not exist')        #this is how i show message in django...we have writeen its statements in the main.html go see that
        #if the user does exist
        
        # used the authenticate function(inbuilt fun) to authenticate the user
        
        # this below authenticate function will return the user Object if the user is authenticated else it will return None
        user=authenticate(request,username=userid,password=password) #this will authenticate the user
        if user is not None:
            login(request,user) #login function is inbuilt in django, it will login the user and create a session for the user in the database and inside of our browser..then the suer will be officially logged in
            return redirect('home')
        else:
            messages.error(request,'Username or password is incorrect')
    context={}
    return render(request,'base/login_register.html',context)




# here i have directly logoiut the user from the home page and havent created any logout template


# In Django, the logout function requires the request object in order to log out the user associated with that specific request. The request object contains information about the current web request, including details about the user making the request. When you call logout(request), Django uses the information from the request object to identify which user is currently authenticated and logs them out.

# In summary, the request object is necessary for the logout function to perform the logout action on the correct user.


def logoutUser(request):
    logout(request)     #this willd delete the session of the user from the database and from the browser
    return redirect('home')


