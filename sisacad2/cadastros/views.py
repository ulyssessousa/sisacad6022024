from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Departamento, Disciplina
from django.urls import reverse_lazy


# Create your views here.
class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome', 'sigla']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('inicio')

class DisciplinaCreate(CreateView):
    model = Disciplina
    fields = ['nome', 'cargaHoraria', 'departamento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('inicio')

class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class DisciplinaUpdate(UpdateView):
    model = Disciplina
    fields = ['nome', 'cargaHoraria', 'departamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class DepartamentoDelete(DeleteView):
    model = Departamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('inicio')

class DisciplinaDelete(DeleteView):
    model = Disciplina
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('inicio')