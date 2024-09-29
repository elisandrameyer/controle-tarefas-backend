from django.db import models
from django.conf import settings


# Create your models here.


class Tarefa(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, blank=True)
    atribuicoes = models.ManyToManyField(
        settings.AUTH_USER_MODEL
    )
    status = models.BooleanField(blank=True, default=True)
    
class TarefaTodos(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(blank=True, default=True)


