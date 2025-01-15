from django.urls import path
from .views import DepartamentoCreate, DisciplinaCreate

urlpatterns = [
    path('cadastros/departamento/', 
         DepartamentoCreate.as_view(),
         name='cadastrar-departamento'),
    
    path('cadastros/disciplina/',
         DisciplinaCreate.as_view(),
         name='cadastrar-disciplina'),
]