from django.http import JsonResponse

def getRoutes(request):
    # below routes is a list
    routes=[
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    
    # this below JsonResponse will return routes in the json format it will convert it into the json format...also sage=False neans..this will convert the above python list into json..means it is not strict
    return JsonResponse(routes,safe=False)