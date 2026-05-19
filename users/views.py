from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import EmprendedorRegistrationForm, CustomLoginForm

class EmprendedorRegisterView(CreateView):
    form_class = EmprendedorRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')  # Redirige al login tras un registro exitoso

# Personalizamos las vistas de Login y Logout para usar nuestros formularios y redirecciones específicas
class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'users/login.html'
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Al cerrar sesión, vuelve al login