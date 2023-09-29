from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .forms import RoomForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Room, Topic,Message


def home(request):

    q = request.GET.get('query') if request.GET.get('query') != None else ''

    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(
        name__icontains=q) | Q(description__icontains=q))

    room_count = rooms.count()
    # when clicked on this ,this will give us the activity of the room we have selected 
    room_message=Message.objects.filter(Q(room__topic__name__icontains=q))

    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count,'room_message1':room_message}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    
    # 'order_by('-created')'  here this says that order the messages in descending order of their creation time...created is the arttribute i have create in the message modals
    # bewlow this says give us the set of messages that are related to this specific room
    room_message=room.message_set.all() #here we are querying the message model which is related to the room model.ie we can query the child model from the parent model(here room is the parent model and message is the child model). and we write the child model in Lower case like here i have written "Message" model in lower case and applied "_set.all()" method to it
    
    
    participants=room.participants.all()        #we use all() for many to many and _set.all() for many to one...yaha se apan ne saare participants ko nikal liya aur unko ek variable mein store kar liya jo hain participants and then this variable is passed in the context dictionary below..and then in the room.html we have applied for loop on this variable
    
    # here while sending the messge we want to set the user, room which he is in and also the body ie the message itself. we the the body(message) which is in the request.POST object
    if request.method=="POST":
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')           # here in get(' ')  i have put the name of the input there in this case it is body
        )
        
        # this has to be done before the redirect because we want to add the user to the room before we redirect to the room page
        room.participants.add(request.user)         # here we are adding the user to the room participants list...jo bhi naya user chatt karega room mein usko particiipants ke list mein add kiya...yaha pe request.user is the user who is sending the message
        
        # also we have a method like add()--> remove which can be used to remove the user
        
        
        # the reason why i am doing redirect is, technically i could just not do this , and its still gonna be on this page . the form will be there on the page and the page will refresh . BUt the issue is now this is technically gonna be the post req and this gonna mess some  functionality here so we actually want that the page to full reload in a sense to clear what is going on  and make sure that we are back on that page with a get req  
        return redirect('room',pk=room.id)
    
        
    
    context = {'room': room,'room_message1':room_message,'participants':participants}
    #  ismein jo room_message hain maine woh room_message1 mein likh diya and then in room.html i have  applied for loop on room_message1
    return render(request, 'base/room.html', context)
# this above line means that when the above view is triggerd then the base/room.html template is rendered and the context dictionary is passed in the template...this is imp




def userProfile(request,pk):
    user=User.objects.get(id=pk)
    # rooms = user.room_set.all(): Assuming that you have a related model named Room with a ForeignKey or a ManyToManyField to the User model, this line fetches all the rooms associated with the user. The room_set attribute is created by Django for reverse relationships.
    rooms=user.room_set.all() # we can get all the children of the specific object by setting the .._set.all() method
    context={'user':user,'rooms':rooms}
    return render(request, 'base/profile.html',context)
    


@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':

        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/room_form.html', context={'form': form})


@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here')

    if (request.method == 'POST'):
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)



@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('You are not allowed here')
    if (request.method == 'POST'):
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', context={'obj': room})


def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        userid = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:

            user = User.objects.get(username=userid)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=userid, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(
                request, 'An error occured during the  registration')

    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'base/login_register.html', context)


@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed here')
    if (request.method == 'POST'):
        message.delete()
        return redirect('home')

    return render(request, 'base/delete.html', context={'obj': message})