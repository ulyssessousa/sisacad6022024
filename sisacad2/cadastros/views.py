from django.views.generic.edit import CreateView
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

