# Import the necessary modules from Django
from django.db import models  
from django.contrib.auth.models import AbstractUser  # Import the AbstractUser class for custom user model





# Define a custom user model that inherits from AbstractUser
class User(AbstractUser):
    pass  

    # now typically we dont have to register our user with the admin panel but because we created our own user model we do need to go into the admin.py and...follow further their