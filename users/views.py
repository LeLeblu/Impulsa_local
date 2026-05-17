from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import EmprendedorRegistrationForm, CustomLoginForm

class EmprendedorRegisterView(CreateView):
    form_class = EmprendedorRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')  # Redirige al login tras un registro exitoso

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'users/login.html'
    # El destino tras el login se puede configurar aquí o en settings.py via LOGIN_REDIRECT_URL

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Al cerrar sesión, vuelve al login