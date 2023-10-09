from django.contrib import admin

# Register your models here.
# also after creating the room table we cant see it in admin panel...to see it.. we need to do below

from .models import Room, Message, Topic
# since the user model is already registered in the admin panel by default  ..we dont need to register it again
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)
