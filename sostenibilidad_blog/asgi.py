# sostenibilidad_blog/asgi.py

"""
Configuración ASGI para el proyecto 'sostenibilidad_blog'.

Este archivo expone la variable 'application' de nivel de módulo.
ASGI (Asynchronous Server Gateway Interface) es el estándar para aplicaciones web asíncronas en Python.
"""

import os
from django.core.asgi import get_asgi_application

# Establecer la variable de entorno con el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sostenibilidad_blog.settings')

# Obtener la aplicación ASGI
application = get_asgi_application()
