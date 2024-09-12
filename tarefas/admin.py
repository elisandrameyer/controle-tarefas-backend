from django.contrib import admin
from tarefas.models import Tarefa, TarefaTodos

# Register your models here.


admin.site.register(Tarefa)
admin.site.register(TarefaTodos)