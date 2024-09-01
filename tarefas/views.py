from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TarefaSerializer, UserSerializer




@api_view(['POST'])
def cadastrar_tarefa(request):
    serializer = TarefaSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def buscar_usuarios(request):
    if request.method == 'GET':
        usuarios = User.objects.all()
        print(usuarios)
        serializer = UserSerializer(usuarios, context={'request': request})
        return Response(serializer.data)  
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listar_scripts(request):
    if request.method == 'GET':
        scripts = Script.objects.all()  # Get all objects in User's database (It returns a queryset)

        serializer = ScriptsSerializer(scripts,
                                       many=True)  # Serialize the object data into json (Has a 'many' parameter cause it's a queryset)

        return Response(serializer.data)  # Return the serialized data

    return Response(status=status.HTTP_400_BAD_REQUEST)