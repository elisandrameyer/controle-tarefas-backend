from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TarefaSerializer, TarefaTodosSerializer
from .models import Tarefa, TarefaTodos
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import (
    logout as django_logout
)


@api_view(['POST'])
def cadastrar_tarefa(request):
    if request.data['atribuicao'] == 0:
        serializer = TarefaTodosSerializer(data=request.data)
    else:
        serializer = TarefaSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def buscar_usuarios(request):
    if request.method == 'GET':
        User = get_user_model()
        users = User.objects.all()
        print(users.all().values())
        usuarios = []
        for user in users:
            user_json = {
                "id": user.id,
                "usuario": user.username
            }
            usuarios.append(user_json)
            
        return JsonResponse(usuarios, safe=False)  
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def buscar_tarefas_usuario(request):
    if request.method == 'GET':
        token_key = request.headers.get('Authorization', '').replace('Token ', '')
        try:
            token = Token.objects.get(key=token_key)
            user = token.user
            tarefas = Tarefa.objects.filter(atribuicao_id=user.id, status=True)
            serializer = TarefaSerializer(tarefas, many=True) 
        except Token.DoesNotExist:
            return Response({'error': 'Token inválido'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def buscar_tarefas_todos(request):
    if request.method == 'GET':
        tarefas = TarefaTodos.objects.filter(status=True)
        serializer = TarefaTodosSerializer(tarefas, many=True) 
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout(request):
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass
    if getattr(settings, 'REST_SESSION_LOGIN', True):
        django_logout(request)

    return Response(status=status.HTTP_200_OK)

