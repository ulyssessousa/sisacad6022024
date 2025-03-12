from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404

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
    template_name = 'cadastros/lista/curso2.html'
    login_url = reverse_lazy('login')
    paginate_by = 5

    def get_queryset(self):
        cursos = Curso.objects.all()
        nome = self.request.GET.get('nome')
        departamento_id = self.request.GET.get('departamentoSelect')
        modalidade_id = self.request.GET.get('modalidadeSelect')

        if nome:
            cursos = cursos.filter(nome__icontains=nome)
        if departamento_id:
            cursos = cursos.filter(departamento_id=departamento_id)
        if modalidade_id:
            cursos = cursos.filter(modalidade_id=modalidade_id)
        return cursos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_option'] = self.request.GET.get('departamentoSelect')
        context['departamentoSelect'] = self.request.GET.get('departamentoSelect')
        context['departamentos'] = Departamento.objects.all()
        context['modalidades'] = Modalidade.objects.all()
        return context

class InscricaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"Administrador", u"Aluno"]
    model = Inscricao
    fields = ['semestre', 'disciplinas']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('listar-inscricao')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Realizar Nova Inscrição"
        context['botao'] = "Realizar Inscrição"
        return context

class InscricaoList(LoginRequiredMixin, ListView):
    model = Inscricao
    template_name = 'cadastros/lista/inscricao.html'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        self.object_list = Inscricao.objects.filter(
                            usuario = self.request.user)
        return self.object_list

class InscricaoUpdate(LoginRequiredMixin, UpdateView):
    model = Inscricao
    fields = ['semestre', 'disciplinas']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-inscricao')
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Inscricao,
                                        pk=self.kwargs['pk'],
                                        usuario = self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar dados da inscrição"
        context['botao'] = "Confirmar Atualizações"
        return context

class InscricaoDelete(LoginRequiredMixin, DeleteView):
    model = Inscricao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-inscricao')
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Inscricao,
                                        pk=self.kwargs['pk'],
                                        usuario = self.request.user)
        return self.object

def consultar_cursos(request):
    cursos = Curso.objects.all()
    departamentos = Departamento.objects.all()
    modalidades = Modalidade.objects.all()

    nome = request.GET.get('nome')
    departamento_id = request.GET.get('departamento')
    modalidade_id = request.GET.get('modalidade')

    if nome:
        cursos = cursos.filter(nome__icontains=nome)
    if departamento_id:
        cursos = cursos.filter(departamento_id=departamento_id)
    if modalidade_id:
        cursos = cursos.filter(modalidade_id=modalidade_id)

    context = {
        'cursos': cursos,
        'departamentos': departamentos,
        'modalidades': modalidades,
    }
    return render(request, 'cadastros/lista/consultar_cursos.html', context)