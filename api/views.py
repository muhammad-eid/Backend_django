
from datetime import datetime
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .encrypt import decrypt
import json


from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

def connect(request):
    return JsonResponse({'status': 'online', 'date': datetime.now()})

@api_view(['POST'])
def activate(request):

    # print(json.loads(request.body))
    # return Response({'status': 'online', 'date': datetime.now()})
    data = decrypt(json.loads(request.body))
    # res = encrypt.encrypt()
    # encrypt.encrypt(res)
    return Response({'status': 'online', 'date': datetime.now(), 'data': data})
    return Response({'status': 'online'})


@api_view(['POST'])
def check(request):
    print(request.POST['data'])
    return JsonResponse({'status': 'online', 'date': datetime.now()})
    # data = encrypt.decrypt()
    # res = 'encrypt.encrypt()'
    # return JsonResponse({'status': 'online', 'date': datetime.now(), 'data': encrypt.encrypt(res)})