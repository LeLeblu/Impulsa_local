# Impulsa Local - Prototipo Alcaldía Ciudad Nueva

Este es el prototipo modular del proyecto 'Impulsa Local' desarrollado en Python y Django.

## Instrucciones para ejecutar el proyecto:

1. Ir al repositorio → botón verde <> Code → pestaña Codespaces → Create codespace on main
2. Crear y activar un nuevo entorno virtual:
   ```bash
   python -m venv env
   # En Windows:
   .\env\Scripts\activate

3. INSTALAR LAS DEPENDENCIAS
pip install -r requirements.txt

4. CONFIGURAR LAS VARIABLES DE ENTORNO 
-Crear un archivo .env en la raiz con el siguiente contenido

DEBUG=True
SECRET_KEY=clave-secreta-desarrollo-unad
ALLOWED_HOSTS=localhost,127.0.0.1

-Genera la SECRET KEY escribe el siguiente codigo en la terminal:

python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

5. CREAR EL USUARIO ADMINISTRADOR  
- Usa el siguiente codigo en la terminal para crearlo: 

python manage.py createsuperuser 

El sistema pedirá:

Username (nombre de usuario)
Email (puede dejarse vacío)
Password (y confirmación)

6. CORRER EL SERVIDOR

python manage.py runserver

El servidor quedará activo en: http://127.0.0.1:8000/



