# sostenibilidad_blog/settings.py

"""
Archivo de configuración principal para el proyecto Django 'sostenibilidad_blog'.

Contiene ajustes predeterminados para bases de datos, aplicaciones instaladas,
ubicaciones de archivos estáticos, internacionalización, etc.
"""

import os
from pathlib import Path

# Ruta base del proyecto (equivalente a la carpeta 'sostenibilidad_blog')
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta para la aplicación. Úsala solo en desarrollo y reemplázala en producción.
SECRET_KEY = 'Jeshua'

# DEBUG controla si se muestran errores detallados (True) o no (False).
DEBUG = True

# Especifica los dominios/hosts desde donde se puede acceder a la aplicación.
ALLOWED_HOSTS = []

# Aplicaciones instaladas (apps nativas de Django y apps personalizadas)
INSTALLED_APPS = [
    # Apps de Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Ckeditor (si la usas)
    'ckeditor',

    # Tus aplicaciones
    'blog',         
    'pages',        # App para manejar páginas (modelo Page, etc.)
    'accounts',     # App para manejar usuarios, perfiles
    'messaging',    # App de mensajería
]

# Middlewares (procesan la request/response en cadena)
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL principal de la aplicación: se define en 'sostenibilidad_blog/urls.py'
ROOT_URLCONF = 'sostenibilidad_blog.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Directorios donde se buscarán las plantillas
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Procesadores de contexto por defecto
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application (para despliegue de la aplicación)
WSGI_APPLICATION = 'sostenibilidad_blog.wsgi.application'

# Configuración de base de datos (por defecto, SQLite3 local)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuración de validadores de contraseñas (según estándares de Django)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configuración de internacionalización y localización
LANGUAGE_CODE = 'es'  # Idioma principal
TIME_ZONE = 'UTC'     # Zona horaria
USE_I18N = True       # Internacionalización
USE_L10N = True       # Localización
USE_TZ = True         # Uso de zona horaria

# Rutas para archivos estáticos y medios
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
# En producción, normalmente se define STATIC_ROOT para collectstatic

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuración adicional
LOGIN_REDIRECT_URL = 'accounts:profile'
LOGOUT_REDIRECT_URL = 'accounts:profile'

# Intenta importar configuraciones locales si el archivo existe
try:
    from .local_settings import *
except ImportError:
    pass
