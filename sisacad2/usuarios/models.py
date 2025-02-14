from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    nome_completo = models.CharField(max_length=80, 
                                    null=True, 
                                    verbose_name='Nome completo')
    cpf = models.CharField(max_length=11, null=True,
                                    verbose_name="CPF")
    telefone = models.CharField(max_length=11, null=True)

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)