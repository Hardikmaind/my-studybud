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
from .models import Room, Topic


def home(request):

    q = request.GET.get('query') if request.GET.get('query') != None else ''

    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(
        name__icontains=q) | Q(description__icontains=q))

    room_count = rooms.count()

    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)

    context = {'room': room}
    return render(request, 'base/room.html', context)


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
    form = RoomForm(request.POST)
    if (request.method == 'POST'):
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', context={'obj': room})


def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        userid = request.POST.get('username').lower().lower()
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
