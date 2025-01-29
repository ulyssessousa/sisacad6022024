from django.urls import path
from django.contrib.auth import views as auth_views
from .views import EncerrarSessaoView

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

]