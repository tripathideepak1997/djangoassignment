from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def greetings(request,id):
    if id in range(6, 13):
        return HttpResponse('Good Morning')
    elif id in range(13, 19):
        return HttpResponse('Good Afternoon')
    elif id in range(19, 25):
        return HttpResponse('Good Evening')
    else:
        return HttpResponse('Go To Bed')
