from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class EmprendedorRegistrationForm(UserCreationForm):
    # Campos adicionales obligatorios para el registro del emprendedor
    email = forms.EmailField(required=True)
    documento_identidad = forms.CharField(required=True, max_length=20)
    telefono = forms.CharField(required=True, max_length=15)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'documento_identidad', 'telefono']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Roles.EMPRENDEDOR  # Aseguramos que se registre como Emprendedor
        if commit:
            user.save()
        return user


class CustomLoginForm(AuthenticationForm):
    # Formulario personalizado de login para añadir clases de estilo fácilmente
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))