# sostenibilidad_blog/urls.py

"""
Archivo de configuración de URL raíz para el proyecto 'sostenibilidad_blog'.

Define el enrutamiento principal y enlaza las rutas de las aplicaciones instaladas.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from sostenibilidad_blog.views import home

urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),

    # Rutas de la app 'pages'
    path('pages/', include('pages.urls', namespace='pages')),

    # Rutas de la app 'accounts'
    path('accounts/', include('accounts.urls', namespace='accounts')),

    # Rutas de la app 'messaging'
    path('messaging/', include('messaging.urls', namespace='messaging')),
    
    # Rutas de la app 'blog'
    path('blog/', include('blog.urls', namespace='blog')),

    # Rutas de la app 'about'
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),

    path('', home, name='home'),
]

# En modo desarrollo, servir archivos de medios
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
