from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import logout

# Create your views here.
class EncerrarSessaoView(TemplateView):
    
    def user_logout(request):
        #if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)
        return redirect('login')
