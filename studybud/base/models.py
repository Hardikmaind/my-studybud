from django.db import models
from django.contrib.auth.models import User     #here we are importing the user model from django.contrib.auth.models...later on we will customize it


# here all the tables are created
# Create your models here.



# Room is gonna be tha child of a topic...  i wanna specify a class above it..that is gonna be the parent class of this class
class Topic(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
        # now we wanna speciy the relation ship between the room and the topic...a topic can have multile rooms whereas a room can have only one topic





class Room(models.Model):
    name=models.CharField( max_length=200)  #here null is set to false by default. this means is ..the database cannot have the instance of this model without having this value something in it
    description=models.TextField(null=True ,blank=True)      #edar bydefault null ki value false rehti isliye aoan ne specify kiya hain ki null ki value true rahe. here it means that null is allowed
    #here blank true means hum jab form banate tab hum blank  use send kar sakte. when we run the save method,like we submit a form..that form  can also be empty.Here it makes sure that this description value cannot be left blank

    #partiipants=
    updated=models.DateTimeField(auto_now=True)   #this is gonna take the snapshot of any time,this model instace was updated,so any time we run teh save mehod to update this model or this specifi table or item...this is going to take a time stamp. here we want the date and the time field it happend. here auto_now =true means that every time the save method is called this is going to take tha sanpshot automatically  

    created=models.DateTimeField(auto_now_add=True)
    #diff between autonow and autonnowadd is auto noew add only takes snapshot when we first create or save this instant..if we save the instance multiple time ..this value will never change ...where as autonow will take snapchot every single time 

    #  dafault we have ids genrated for them from 1
    # id= we can override  the id field by creating our own id field with 


    # since topic class is placed below Room class in our CODE  we cann access it by putting like 'Topic'.(in quotes)..but if it would have been above  then we can aslo access it by putting just Topic
    topic=models.ForeignKey(Topic,null=True ,on_delete=models.SET_NULL)       #this is a one to many relationship...and in bracket there is the model we are relating to. i.e parent model topic . incase topic is deleted then the room will be set to null, idont want to delete the room..i just want to set it to null. and if this value is set to null then we have to allow in the database that this value can be null. so we have to specify null=True

    
    host=models.ForeignKey(User,null=True ,on_delete=models.SET_NULL)



    # The __str__ and __repr__ methods are two commonly used “dunder” (double underscore) methods that can be used to define how an object is represented as a string. Both methods, str and repr, generate a string representation of an object, but they serve different purposes and people use them in different contexts.2

    # When you call str(object) on an instance of your class, Python will look for the __str__ method in that class and use its return value as the string representation of the object.




    def __str__(self):          #created a string representation of our room
        return self.name
        # return str(self.name)       #here self has to be string ...if not then we have to type cast it


#after we add a new model...we have to again do the migration with the command "python manage.py makemigrations"  then press enter. after this then i hace to do "python manage.py migrate"..before this command it is like a staging area...we have to this everytime. after apply both the commands. this will go into the latest migrations .after applyig this migrations theis migrations are in the database



class Message(models.Model):  
    # django already builds the usermodel for us..we can use that or we can create our own user model  
    user=models.ForeignKey(User,on_delete=models.CASCADE)       #this is a one to many relationship...and in bracket there is the model we are relating to. i.e parent model user   
    room =models.ForeignKey(Room,on_delete=models.CASCADE)       #this is a one to many relationship...and in bracket there is the model we are relating to. i.e parent model room
    # on_delete=models.SET_NULL  means that if we delete the room..then the message will not be deleted..it will be set to null. all the instance of the children will be set to null  
    # on_delete=models.CASCADE  means that if we delete the room..then the message will also be deleted..it will be set to null. all the instance of the children will be set to null
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True) 
    created=models.DateTimeField(auto_now_add=True) 
     
    def __str__(self):          #created a string representation of our room
        return self.body[0:50 ]  #here we are returning the first 50 characters of the body of the message



