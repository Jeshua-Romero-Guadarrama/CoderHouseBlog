# sostenibilidad_blog/wsgi.py

"""
Configuración WSGI para el proyecto 'sostenibilidad_blog'.

Este archivo expone la variable 'application' de nivel de módulo.
WSGI (Web Server Gateway Interface) es el estándar para aplicaciones web en Python.
"""

import os
from django.core.wsgi import get_wsgi_application

# Establecer la variable de entorno con el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sostenibilidad_blog.settings')

# Obtener la aplicación WSGI
application = get_wsgi_application()
