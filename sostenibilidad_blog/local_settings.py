# sostenibilidad_blog/local_settings.py

"""
Archivo de configuración local para sobreescribir valores sensibles y no 
compartirlos en repositorios (se incluye en .gitignore).
"""

from .settings import BASE_DIR

# Clave secreta real en desarrollo local
SECRET_KEY = 'Jeshua'

# DEBUG = False en producción o controlar según tu entorno
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_local.sqlite3',
    }
}

# Configurar hosts permitidos para trabajos en desarrollo en la IP local
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
