from django.urls import path
from django.contrib.auth import views as auth_views
from .views import EncerrarSessaoView, UsuarioCreate, PerfilUpdate

urlpatterns = [
    path('login/', 
         auth_views.LoginView.as_view(
             template_name = 'usuarios/login.html'
             ),
         name='login'
        ),
    path('logout/',
         EncerrarSessaoView.user_logout,
         name='logout'
        ),

    path('registrar/',
        UsuarioCreate.as_view(),
        name='registrar'
    ),

    path('atualizar-dados/',
         PerfilUpdate.as_view(),
         name='atualizar-dados'
    ),

]