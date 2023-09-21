from django.forms import ModelForm
from .models import Room
# we will import this below form in our view 

# Defining a new form class called RoomForm that inherits from ModelForm
class RoomForm(ModelForm):
        # Creating an inner class Meta to provide additional information about the form
    class Meta:
                # Specifying that this form is associated with the Room model
        model=Room          #this is the model that we want to create a form for..jo model hai uska form banana hai
        fields='__all__'   #this will give us all the fields in the form...present in modal Room like host ,topic,name etc  just udated and creatd will not be shown since those re not editable fields  
        # if we want the oarticular fields then we can do like this 
        # fields=['name','topic','body','votes_to_skip'] 