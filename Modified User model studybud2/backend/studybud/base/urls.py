#  this urls.py in this app is going to be for this base app
from django.urls import path
from . import views     #this is importing the views.py file from the base app
urlpatterns = [
    path('', views.home,name="home"),   #when the user goes to the home page, the home function is called..which is in the views.py file


      #pk parameter is for dynamic routing.it is a primary key
    path('room/<str:pk>', views.room,name="room"),   #when the user goes to the home page, the home function is called 

    path('profile/<str:pk>/', views.userProfile,name="user-profile"),

    # people pass it int into url. abov ei have passed the pk as a string
    #     path('room/<slug:pk>', views.room,name="room"), 

    path('create-room/', views.createRoom,name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom,name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage,name="delete-message"),
    path('update-user/', views.updateUser,name="update-user"),
    path('topics/', views.topicsPage,name="topics"),
    path('activity/', views.activityPage,name="activity"),
    path('login/', views.loginPage,name="login"),
    path('logout/', views.logoutUser,name="logout"),
    path('register/', views.registerPage,name="register"),
    path('profile/<str:pk>/', views.userProfile,name="user-profile"),
]


# path('logout/', views.logoutUser, name="logout"),


# 1  path('logout/'): This is a URL pattern that specifies the path that should trigger a certain view. In this case, when a user navigates to http://example.com/logout/, Django will use this pattern to determine which view function to call.

#2   views.logoutUser: This is the view function that should be called when the specified URL pattern is matched. In this case, it's calling a view function named logoutUser. This function would be defined in the views.py file of the Django application.

#3   name="logout": This is an optional parameter that gives a name to this URL pattern. This name is used to identify the URL pattern in the Django templates and views, which allows you to refer to it by name instead of using the actual URL path.

#  For example, in a Django template, you could use the {% url 'logout' %} template tag to generate the URL associated with the name "logout".

#  Overall, this line of code sets up a URL pattern that, when matched, will call the logoutUser view function. This view function is responsible for handling the logic associated with user logout in your Django application.