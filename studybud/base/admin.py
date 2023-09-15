from django.contrib import admin

# Register your models here.
# also after creating the room table we cant see it in admin panel...to see it.. we need to do below

from .models import Room
admin.site.register(Room)