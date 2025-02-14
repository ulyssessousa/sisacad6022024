from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import logout

from django.views.generic.edit import CreateView
from .forms import UsuarioForm
from django.urls import reverse_lazy

from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

# Create your views here.
class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Aluno")
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"
        return context



class EncerrarSessaoView(TemplateView):
    
    def user_logout(request):
        #if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)
        return redirect('login')

