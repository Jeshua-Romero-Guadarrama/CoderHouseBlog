#!/usr/bin/env python
"""manage.py
Archivo que permite ejecutar los comandos de Django (migraciones, correr servidor, entre otros).
Script de utilidad para tareas de Django como migraciones, inicio del servidor de desarrollo, creación de usuarios, entre otros.
"""

import os
import sys

def main():
    """Punto de entrada principal para gestionar comandos de Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sostenibilidad_blog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django."
            "Asegúrate de que esté instalado y disponible en tu entorno virtual."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
