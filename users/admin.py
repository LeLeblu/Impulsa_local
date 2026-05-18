from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # 1. Columnas que se mostrarán en la lista principal del panel de administración
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    
    # 2. Filtros laterales para buscar rápidamente por rol o estado
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')
    
    # 3. Campos por los que se puede buscar en la barra superior
    search_fields = ('username', 'first_name', 'last_name', 'email', 'documento_identidad')
    
    # 4. Orden por defecto en la lista (los más recientes primero si usaras fecha, o por username)
    ordering = ('username',)

    # 5. Configuración de los formularios de edición dentro del admin para que incluyan tus campos personalizados
    # Fieldsets organiza los campos en secciones plegables/visuales
    fieldsets = UserAdmin.fieldsets + (
        ('Información de Control (Alcaldía)', {
            'fields': ('role', 'telefono', 'documento_identidad'),
        }),
    )
    
    # Campos que aparecen al crear un usuario directamente desde el panel de administración
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información de Control (Alcaldía)', {
            'fields': ('role', 'telefono', 'documento_identidad'),
        }),
    )

# Registrar el modelo User asociado a nuestra clase de configuración CustomUserAdmin
admin.site.register(User, CustomUserAdmin)