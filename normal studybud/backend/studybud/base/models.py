from django.db import models

from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # ManyToManyField this below states the field
    # now since the user modal is already connected to the room modal in host. so here we need to specify the related name we can do this regardless,but in this case because we have it we need to specify it anmd that just means that we cant reference a user because we already have a  'User' in the room modal(in hose)
    participants = models.ManyToManyField(User,related_name='participants', blank=True)

    updated = models.DateTimeField(auto_now=True)

    created = models.DateTimeField(auto_now_add=True)

    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)


    class Meta:

        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
