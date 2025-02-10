from django.contrib import admin
from .models import Departamento, Disciplina, Modalidade, Curso

# Register your models here.
admin.site.register(Departamento)
admin.site.register(Disciplina)
admin.site.register(Modalidade)
admin.site.register(Curso)