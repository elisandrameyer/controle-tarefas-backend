from django.urls import path
# NOTE: Import the view function from the file where you saved it
from tarefas.views import cadastrar_tarefa, buscar_usuarios, buscar_tarefas_usuario, logout, buscar_tarefas_todos, concluir_tarefa, buscar_tarefas_concluidas_usuario, buscar_tarefas_concluidas_todos
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.exceptions import NotFound




urlpatterns = [
    # Register our view
    path('cadastrar-tarefa', cadastrar_tarefa, name='random-number'),
    path('buscar-usuarios', buscar_usuarios, name='buscar_usuarios'),
    path('buscar-tarefas-usuario', buscar_tarefas_usuario, name='buscar_tarefas_usuario'),
    path('buscar-tarefas-concluidas-usuario', buscar_tarefas_concluidas_usuario, name='buscar_tarefas_concluidas_usuario'),
    path('buscar-tarefas-todos', buscar_tarefas_todos, name='buscar_tarefas_todos'),
    path('buscar-tarefas-concluidas-todos', buscar_tarefas_concluidas_todos, name='buscar_tarefas_concluidas_todos'),
    path('concluir-tarefa', concluir_tarefa, name='concluir_tarefa'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('logout', logout, name='logout'),
    path('admin/', admin.site.urls),


]