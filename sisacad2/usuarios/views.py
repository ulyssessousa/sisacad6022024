from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import logout

from django.views.generic.edit import CreateView
from .forms import UsuarioForm
from django.urls import reverse_lazy

# Create your views here.
class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

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

