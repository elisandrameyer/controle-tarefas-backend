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
from rest_framework.exceptions import NotFound


@api_view(['POST'])
def cadastrar_tarefa(request):
    atribuicoes = request.data['atribuicoes']
    if 0 in atribuicoes:
        serializer_todos = TarefaTodosSerializer(data=request.data)
        request.data['atribuicoes'].remove(0)
        if serializer_todos.is_valid():
            serializer_todos.save()
        else:
            return Response(serializer_todos.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = TarefaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)


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
            tarefas = Tarefa.objects.filter(atribuicoes=user, status=True)
            serializer = TarefaSerializer(tarefas, many=True) 
        except Token.DoesNotExist:
            return Response({'error': 'Token inválido'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def buscar_tarefas_concluidas_usuario(request):
    if request.method == 'GET':
        token_key = request.headers.get('Authorization', '').replace('Token ', '')
        try:
            token = Token.objects.get(key=token_key)
            user = token.user
            tarefas = Tarefa.objects.filter(atribuicoes=user, status=False)
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

@api_view(['GET'])
def buscar_tarefas_concluidas_todos(request):
    if request.method == 'GET':
        tarefas = TarefaTodos.objects.filter(status=False)
        serializer = TarefaTodosSerializer(tarefas, many=True) 
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def concluir_tarefa(request):
    if request.method == 'POST':
        id_tarefa = request.data['id']
        tipo = request.data['tipo'] 

        try:
            if tipo == 'todos':
                tarefa = TarefaTodos.objects.get(id=id_tarefa)
                tarefa.status = False
                tarefa.save()
                serializer = TarefaTodosSerializer(tarefa)
            else:
                tarefa = Tarefa.objects.get(id=id_tarefa)
                tarefa.status = False
                tarefa.save()
                serializer = TarefaSerializer(tarefa)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except TarefaTodos.DoesNotExist:
            raise NotFound("Tarefa não encontrada.")
        except Tarefa.DoesNotExist:
            raise NotFound("Tarefa não encontrada.")



@api_view(['POST'])
def logout(request):
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass
    if getattr(settings, 'REST_SESSION_LOGIN', True):
        django_logout(request)

    return Response(status=status.HTTP_200_OK)

