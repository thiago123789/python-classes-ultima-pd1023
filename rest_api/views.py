from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from base.models import ReservaModel, Petshop
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_api.serializers import ReservaModelSerializer, PetshopNestedSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello World {request.data["nome"]}'})

    return Response({'message': 'Hello World GET endpoint'})


class ReservaModelViewSet(viewsets.ModelViewSet):
    queryset = ReservaModel.objects.all()
    serializer_class = ReservaModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class PetshopModelViewSet(viewsets.ModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopNestedSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
