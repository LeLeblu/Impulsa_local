from django.urls import path
from django.views.generic import RedirectView
from .views import EmprendedorRegisterView, CustomLoginView, CustomLogoutView

urlpatterns = [
    # Si alguien entra a la raíz, lo redirige automáticamente a /login/
    path('', RedirectView.as_view(url='login/', permanent=False)),
    
    path('register/', EmprendedorRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]