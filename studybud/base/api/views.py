from rest_framework.decorators import api_view
from rest_framework.response import Response
from  base.models import Room
from .serializers import RoomSerializer

# niche aopan ko api view mein req allow akrni hain apan woh dal sakte hain...abhi k liye sirf main 'GET' hi dalta hu
# @api_view(['GET','PUT','POSt'])

@api_view(['GET'])
def getRoutes(request):
    # below routes is a list
    routes=[
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    
    # niche apan ko safe vagare ki bhi koi jarurat nahi
    # return Response(routes)
    return Response(routes)


# now this below will give the error that ("Object of type Room is not JSON serializable") since first we were returning the reoutes which is dictionry and can be converted into the json..but now below thge room is coming from the Room(class/model/table) we first have to serialize it. serialize means (converting from class to json).
# from this is it also clear that the Response cannot returned the pyuthon objects(rooms). Objects cannot be converted automaticlly

# below i have only allowed the get request
@api_view(['GET'])
def getRooms(request):
    rooms=Room.objects.all()
    # here below many means that are there gonna be the multipe objects that we need to serialize or are we just serialiuzing one...in this case we are serializeing the query set. so many is gonna be set True, there are many objects
    serializer=RoomSerializer(rooms,many=True)
    # now after this the above serializer variable is now an object so in this case we will directly pass it in the reponse
    
    # return Response(serializer)
    
    # now since we dont want to return the object ...we want to return a data attribute inside it..so we will do it like below
    return Response(serializer.data)



@api_view(['GET'])
def getRoom(request, pk):
    # ismien saare room object nahi ayenge bas wohi junki id =pk hain wohi
    room=Room.objects.get(id=pk)
    # below many is gonna be false since we will be returning only the single object
    serializer=RoomSerializer(room,many=False)
    return Response(serializer.data)
    