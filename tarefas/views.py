from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


@api_view(['POST'])
def cadastrar_tarefa(request):
    print(request)
    return Response({"message": "Hello, world!"})


@api_view(['GET'])
def buscar_usuarios(request):
    print(request)
    return Response({"message": "Hello, world!"})
