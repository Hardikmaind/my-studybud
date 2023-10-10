from django.contrib import admin

# Register your models here.
# also after creating the room table we cant see it in admin panel...to see it.. we need to do below

# here below i have imported the user model whichexterds the abstracted user model

from .models import Room, Message, Topic,User
# since the user model is already registered in the admin panel by default  ..we dont need to register it again

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)
