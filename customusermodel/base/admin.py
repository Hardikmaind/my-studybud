from django.contrib import admin
from .models import User

# now typically we dont have to register our user with the admin panel but because we created our own user model we do need to go into the admin.py..and do this..


# here we have imported the User model which we have extendewd form the AbstractUser model which is inbuilt in python 

# isse apan ne jo bhi users banaye woh saare aajayenge..in the admin panl
# also notice that the  User groop insnt under the authenticaiton and authorization panel...but under the Base which we have created
admin.site.register(User)
