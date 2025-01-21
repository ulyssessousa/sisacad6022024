from django.urls import path
from .views import DepartamentoCreate, DisciplinaCreate, DepartamentoUpdate, DisciplinaUpdate, DepartamentoDelete, DisciplinaDelete, DepartamentoList, DisciplinaList

urlpatterns = [
     path('cadastros/departamento/', 
         DepartamentoCreate.as_view(),
         name='cadastrar-departamento'),
    
     path('cadastros/disciplina/',
         DisciplinaCreate.as_view(),
         name='cadastrar-disciplina'),
     
     path('editar/departamento/<int:pk>/',
          DepartamentoUpdate.as_view(),
          name='editar-departamento'),
     
     path('editar/disciplina/<int:pk>/',
          DisciplinaUpdate.as_view(),
          name='editar-disciplina'),

     path('excluir/departamento/<int:pk>/',
          DepartamentoDelete.as_view(),
          name='excluir-departamento'),
     
     path('excluir/disciplina/<int:pk>/',
          DisciplinaDelete.as_view(),
          name='excluir-disciplina'),
     
     path('listar/departamento/',
          DepartamentoList.as_view(),
          name='listar-departamento'),
     
     path('listar/disciplina/',
          DisciplinaList.as_view(),
          name='listar-disciplina'),
     
]