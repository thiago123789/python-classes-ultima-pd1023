from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello World {request.data["nome"]}'})

    return Response({'message': 'Hello World GET endpoint'})

