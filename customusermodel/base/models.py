# Import the necessary modules from Django
from django.db import models  # Import the models module for defining database models
from django.contrib.auth.models import AbstractUser  # Import the AbstractUser class for custom user model


#  a Django model class named User that inherits from AbstractUser. This code is a common way to extend Django's built-in authentication system to create a custom user model with additional fields or functionality.



# Define a custom user model that inherits from AbstractUser
class User(AbstractUser):
    pass  # "pass" is a placeholder and indicates that no additional custom fields or methods are added
