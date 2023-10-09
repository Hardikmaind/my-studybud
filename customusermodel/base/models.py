# Import the necessary modules from Django
from django.db import models  
from django.contrib.auth.models import AbstractUser  # Import the AbstractUser class for custom user model





# Define a custom user model that inherits from AbstractUser
class User(AbstractUser):
    # u can see the name bio and email field int the admin panel
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(unique=True)
    bio=models.TextField(null=True)
    
    # now we will be saying the django that the username and the password field
    USERNAME_FIELD='email'      #this will be the username field which will be used for the login
    REQUIRED_FIELDS=[]          #this will be required field which will be compulsory
    
    # after creating the aboce make migrations

    # now typically we dont have to register our user with the admin panel but because we created our own user model we do need to go into the admin.py and...follow further their 