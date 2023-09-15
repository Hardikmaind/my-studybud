from django.db import models


# here all the tables are created
# Create your models here.

class Room(models.Model):
    #host
    #topic
    name=models.CharField( max_length=200)  #here null is set to false by default. this means is ..the database cannot have the instance of this model without having this value something in it
    description=models.TextField(null=True ,blank=True)      #edar bydefault null ki value false rehti isliye aoan ne specify kiya hain ki null ki value true rahe. here it means that null is allowed
    #here blank true means hum jab form banate tab hum blank  use send kar sakte. when we run the save method,like we submit a form..that form  can also be empty.Here it makes sure that this description value cannot be left blank

    #partiipants=
    updated=models.DateTimeField(auto_now=True)   #this is gonna take the snapshot of any time,this model instace was updated,so any time we run teh save mehod to update this model or this specifi table or item...this is going to take a time stamp. here we want the date and the time field it happend. here auto_now =true means that every time the save method is called this is going to take tha sanpshot automatically  

    created=models.DateTimeField(auto_now_add=True)
    #diff between autonow and autonnowadd is auto noew add only takes snapshot when we first create or save this instant..if we save the instance multiple time ..this value will never change ...where as autonow will take snapchot every single time 

    def _str_(self):          #created a string representation of our room
        return self.name
        # return str(self.name)       #here self has to be string ...if not then we have to type cast it


#after we add a new model...we have to again do the migration with the command "python manage.py makemigrations"  then press enter. after this then i hace to do "python manage.py migrate"..before this command it is like a staging area...we have to this everytime. after apply both the commands. this will go into the latest migrations .after applyig this migrations theis migrations are in the database



