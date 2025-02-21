from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=5)

    def __str__(self):
        return "{} ({})".format(self.sigla, self.nome)
    

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    cargaHoraria = models.IntegerField(verbose_name="Carga Horária")
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - CH: {}".format(self.nome, self.cargaHoraria)
    
class Modalidade(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return "{}".format(self.nome)

class Curso(models.Model):
    nome = models.CharField(max_length=50)
    cargaHoraria = models.IntegerField(verbose_name="Carga Horária")
    presencial = models.BooleanField()
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.nome, self.modalidade.nome)
    

class Inscricao(models.Model):
    semestre = models.CharField(max_length=10)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return "Semestre: {} (Usuário: {})".format(
                        self.semestre, self.usuario)
