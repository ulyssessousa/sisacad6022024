from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Departamento, Disciplina
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class DepartamentoCreate(LoginRequiredMixin, CreateView):
    model = Departamento
    fields = ['nome', 'sigla']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('listar-departamento')
    login_url = reverse_lazy('login')

class DisciplinaCreate(CreateView):
    model = Disciplina
    fields = ['nome', 'cargaHoraria', 'departamento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('listar-disciplina')

class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-departamento')

class DisciplinaUpdate(UpdateView):
    model = Disciplina
    fields = ['nome', 'cargaHoraria', 'departamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-disciplina')

class DepartamentoDelete(DeleteView):
    model = Departamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-departamento')

class DisciplinaDelete(DeleteView):
    model = Disciplina
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-disciplina')

class DepartamentoList(ListView):
    model = Departamento
    template_name = 'cadastros/lista/departamento.html'

class DisciplinaList(ListView):
    model = Disciplina
    template_name = 'cadastros/lista/disciplina.html'