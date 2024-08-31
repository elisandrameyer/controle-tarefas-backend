from django.urls import path
# NOTE: Import the view function from the file where you saved it
from tarefas.views import cadastrar_tarefa, buscar_usuarios


urlpatterns = [
    # Register our view
    path('cadastrar-tarefa', cadastrar_tarefa, name='random-number'),
    path('buscar-usuarios', buscar_usuarios, name='buscar_usuarios'),

]