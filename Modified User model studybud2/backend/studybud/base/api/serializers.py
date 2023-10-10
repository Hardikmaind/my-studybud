# serializer are gonna be the classes that take a certain  model that we want to serailze or object and its gonna turn it into the json data. so its gonna basiaclly take our python object turn it into a json object and then we can return that.abs

# they work a lot like model form,we are gonna import a serializer ,we are gonna create a class, specify the model and the fields that we want to serailize and then that will be rendered out


from rest_framework.serializers import ModelSerializer
from base.models import Room
class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'