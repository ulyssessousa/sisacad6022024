from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Departamento, Disciplina, Modalidade, Curso
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


# Create your views here.
class DepartamentoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    model = Departamento
    fields = ['nome', 'sigla']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('listar-departamento')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Novo Departamento"
        context['botao'] = "Cadastrar"
        return context

class DisciplinaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    model = Disciplina
    fields = ['nome', 'cargaHoraria', 'departamento']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('listar-disciplina')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Nova Disciplina"
        context['botao'] = "Cadastrar"
        return context

class DepartamentoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    model = Departamento
    fields = ['nome', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-departamento')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar dados de departamento"
        context['botao'] = "Confirmar Atualizações"
        return context


class DisciplinaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    model = Disciplina
    fields = ['nome', 'cargaHoraria', 'departamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-disciplina')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar dados de disciplina"
        context['botao'] = "Confirmar Atualizações"
        return context
    
class DepartamentoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    model = Departamento
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-departamento')
    login_url = reverse_lazy('login')

class DisciplinaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
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

class ModalidadeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    model = Modalidade
    fields = ['nome']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('listar-modalidade')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Nova Modalidade"
        context['botao'] = "Cadastrar"
        return context

class ModalidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    model = Modalidade
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modalidade')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar dados de modalidade"
        context['botao'] = "Confirmar Atualizações"
        return context
    
class ModalidadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    model = Modalidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modalidade')
    login_url = reverse_lazy('login')

class ModalidadeList(LoginRequiredMixin, ListView):
    model = Modalidade
    template_name = 'cadastros/lista/modalidade.html'
    login_url = reverse_lazy('login')

class CursoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    model = Curso
    fields = ['nome', 'cargaHoraria', 'presencial', 'departamento', 'modalidade']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('listar-curso')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Novo Curso"
        context['botao'] = "Cadastrar"
        return context

class CursoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    model = Curso
    fields = ['nome', 'cargaHoraria', 'presencial', 'departamento', 'modalidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-curso')
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar dados de curso"
        context['botao'] = "Confirmar Atualizações"
        return context
    
class CursoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    model = Curso
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-curso')
    login_url = reverse_lazy('login')

class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'cadastros/lista/curso.html'
    login_url = reverse_lazy('login')