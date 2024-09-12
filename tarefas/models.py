from django.db import models
from django.conf import settings


# Create your models here.


class Tarefa(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    atribuicao = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    status = models.BooleanField(blank=True, default=True)
    
class TarefaTodos(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    status = models.BooleanField(blank=True, default=True)


