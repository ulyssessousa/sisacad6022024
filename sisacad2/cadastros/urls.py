from django.urls import path
from .views import *

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
     
     path('cadastros/modalidade/',
         ModalidadeCreate.as_view(),
         name='cadastrar-modalidade'),
     
     path('editar/modalidade/<int:pk>/',
          ModalidadeUpdate.as_view(),
          name='editar-modalidade'),
     
     path('excluir/modalidade/<int:pk>/',
          ModalidadeDelete.as_view(),
          name='excluir-modalidade'),
     
     path('listar/modalidade/',
          ModalidadeList.as_view(),
          name='listar-modalidade'),

     path('cadastros/curso/',
         CursoCreate.as_view(),
         name='cadastrar-curso'),
     
     path('editar/curso/<int:pk>/',
          CursoUpdate.as_view(),
          name='editar-curso'),
     
     path('excluir/curso/<int:pk>/',
          CursoDelete.as_view(),
          name='excluir-curso'),
     
     path('listar/curso/',
          CursoList.as_view(),
          name='listar-curso'),
]