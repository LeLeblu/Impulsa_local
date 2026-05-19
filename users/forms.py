from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


# Formulario de registro personalizado para Emprendedores, heredando de UserCreationForm 
class EmprendedorRegistrationForm(UserCreationForm):
    # Campos adicionales obligatorios para el registro del emprendedor
    email = forms.EmailField(required=True)
    documento_identidad = forms.CharField(required=True, max_length=20)
    telefono = forms.CharField(required=True, max_length=15)
    ubicación = forms.CharField(required=True, max_length=15)
    actividad_economica = forms.CharField(required=True, max_length=20)

# Meta clase para definir el modelo y los campos a usar en el formulario
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'documento_identidad', 'telefono']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Roles.EMPRENDEDOR  
        if commit:
            user.save()
        return user

# Formulario de login personalizado para aplicar la regla de negocio de la Alcaldía
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'johndoe'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': '********'}))

    def clean(self):
        # 1. Ejecuta la validación nativa de Django (verifica que el usuario y clave existan y sean correctos)
        cleaned_data = super().clean()
        user = self.user_cache  # Django guarda el usuario autenticado aquí temporalmente

        # 2. Si el usuario es correcto ingresa a la siguiente pantalla
        if user is not None:
            # Si tiene el estado de Staff (Admin) o su rol no es Emprendedor, sale advertencia
            if user.is_staff or user.role == User.Roles.ADMIN_ALCALDIA:
                raise forms.ValidationError(
                    "Acceso denegado. Este formulario es exclusivo para Emprendedores. "
                    "Si eres funcionario, usa el enlace de la parte inferior.",
                    code='invalid_login',
                )
        
        return cleaned_data