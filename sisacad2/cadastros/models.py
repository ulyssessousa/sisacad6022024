from django.db import models

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