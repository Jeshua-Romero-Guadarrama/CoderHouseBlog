from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm
from .models import Profile

"""
Vistas para la aplicación 'accounts'.

Incluye:
  - Registro de nuevos usuarios (redirige a perfil si ya están autenticados).
  - Visualización y actualización del perfil.
  - Logout personalizado: cierra sesión solo a usuarios no administradores.
  - Login personalizado: redirige a /admin/ para administradores, de lo contrario usa el comportamiento predeterminado.
"""

def register_view(request):
    """
    Permite el registro de un nuevo usuario.
    Si el usuario ya está autenticado, se redirige a su perfil.
    """
    if request.user.is_authenticated:
        return redirect('accounts:profile')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile_view(request):
    """
    Muestra el perfil del usuario autenticado.
    Se crea automáticamente si no existe.
    """
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})


@login_required
def profile_update_view(request):
    """
    Permite actualizar los datos del perfil del usuario autenticado.
    """
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_update.html', {'form': form})


class CustomLogoutView(LogoutView):
    """
    Vista de logout personalizada.

    Si el usuario es administrador (staff o superuser), se redirige a su perfil sin cerrar la sesión.
    Para usuarios normales se ejecuta el proceso de logout (lo que pone user.is_authenticated en False)
    y se redirige a la página de inicio.
    """
    http_method_names = ['get', 'post']
    next_page = reverse_lazy('home')

class CustomLoginView(LoginView):
    """
    Vista de login personalizada.

    Utiliza el template 'accounts/login.html'. Si el usuario es administrador (staff o superuser),
    se redirige al panel de administración; de lo contrario, se usa el comportamiento predeterminado.
    """
    template_name = 'accounts/login.html'

    def get_success_url(self):
        if (self.request.user.is_authenticated and
                (self.request.user.is_staff or self.request.user.is_superuser)):
            return reverse_lazy('admin:index')
        return super().get_success_url()
