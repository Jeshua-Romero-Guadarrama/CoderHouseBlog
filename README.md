# Proyecto "Sostenibilidad Blog"

Este proyecto consiste en un **blog de sostenibilidad** creado con **Django**. 
Incluye una aplicación para manejar páginas (`pages`), cuentas de usuario (`accounts`), 
mensajería interna (`messaging`) y cualquier otra funcionalidad adicional que se requiera.

## Requisitos y dependencias

- Python 3.9 o superior (recomendado)
- Django (versión especificada en el `requirements.txt`)
- Otros paquetes detallados en el `requirements.txt`

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/sostenibilidad_blog.git
   ```

2. **Crear y activar un entorno virtual** (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Realizar las migraciones** para configurar la base de datos:
   ```bash
   python manage.py migrate
   ```

5. **Crear un superusuario** (opcional, si deseas acceder al admin):
   ```bash
   python manage.py createsuperuser
   ```

6. **Cargar los fixtures** con los datos iniciales:
   ```bash
   python manage.py loaddata initial_pages_utf8.json
   python manage.py loaddata initial_posts_utf8.json
   ```

7. **Iniciar el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

8. **Abrir el proyecto** en tu navegador:
   ```
   http://127.0.0.1:8000/
   ```

## Usuario de prueba

```
Usuario: Abdeel
Correo: Abdeel@gmail.com
Contraseña: c.C]}!cL}%8_SvS

Usuario: Ingrid
Correo: Ingrid@gmail.com
Contraseña: c.C]}!cL}%8_SvS
```

## Usuario de administración

```
Usuario: Jeshua
Correo: Jeshua@gmail.com
Contraseña: Jeshua
```

## Uso

- Puedes crear, editar y borrar publicaciones (páginas) desde la interfaz web y/o desde el admin de Django.
- Permite registro, login, logout y actualización de perfil de usuarios.
- Incluye un módulo de mensajería interna para enviar y recibir mensajes entre usuarios.

## Estructura principal del proyecto

```
sostenibilidad_blog/
├── .gitignore
├── README.md
├── requirements.txt
├── manage.py
├── media/
├── static/
├── templates/
│   ├── base.html
│   ├── navbar.html
│   └── footer.html
├── sostenibilidad_blog/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── pages/
├── accounts/
└── messaging/
```