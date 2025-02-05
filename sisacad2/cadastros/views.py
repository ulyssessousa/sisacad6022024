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

class DisciplinaCreate(LoginRequiredMixin, CreateView):
    model = Disciplina
    fields = ['nome', 'cargaHoraria', 'departamento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('listar-disciplina')
    login_url = reverse_lazy('login')

class DepartamentoUpdate(LoginRequiredMixin, UpdateView):
    model = Departamento
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-departamento')
    login_url = reverse_lazy('login')

class DisciplinaUpdate(LoginRequiredMixin, UpdateView):
    model = Disciplina
    fields = ['nome', 'cargaHoraria', 'departamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-disciplina')
    login_url = reverse_lazy('login')

class DepartamentoDelete(LoginRequiredMixin, DeleteView):
    model = Departamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-departamento')
    login_url = reverse_lazy('login')

class DisciplinaDelete(LoginRequiredMixin, DeleteView):
    model = Disciplina
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-disciplina')
    login_url = reverse_lazy('login')

class DepartamentoList(LoginRequiredMixin, ListView):
    model = Departamento
    template_name = 'cadastros/lista/departamento.html'
    login_url = reverse_lazy('login')

class DisciplinaList(LoginRequiredMixin, ListView):
    model = Disciplina
    template_name = 'cadastros/lista/disciplina.html'
    login_url = reverse_lazy('login')