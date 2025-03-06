# pages/views.py

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Page
from .forms import PageForm
from django.db.models import Q

"""
Vistas para la aplicación 'pages'.
"""

class PageListView(ListView):
    """
    Lista todas las páginas creadas.
    Si no hay páginas, en la plantilla puedes mostrar 'No hay páginas aún'.
    """
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'
    ordering = ['-created_at']
    paginate_by = 5 

class PageDetailView(DetailView):
    """
    Muestra el detalle de una página específica.
    """
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'

class PageCreateView(LoginRequiredMixin, CreateView):
    """
    Permite crear una nueva página. Requiere que el usuario esté autenticado.
    """
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:page_list')

    def form_valid(self, form):
        """
        Asigna el usuario actual como autor antes de guardar el formulario.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    """
    Permite editar una página existente. Requiere autenticación.
    """
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'

    def get_success_url(self):
        return reverse_lazy('pages:page_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        """
        Verifica que el usuario sea el autor de la página o un superusuario, si no, redirige.
        """
        post = self.get_object()
        if post.author != request.user and not request.user.is_superuser:
            return redirect('blog:page_list')
        return super().dispatch(request, *args, **kwargs)
    
class PageDeleteView(LoginRequiredMixin, DeleteView):
    """
    Permite eliminar una página existente. Requiere autenticación.
    """
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages:page_list')

    def dispatch(self, request, *args, **kwargs):
        """
        Verifica que el usuario sea el autor de la page o un superusuario, si no, redirige.
        """
        post = self.get_object()
        if post.author != request.user and not request.user.is_superuser:
            return redirect('blog:page_list')
        return super().dispatch(request, *args, **kwargs)

class HomeView(ListView):
    model = Page
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 5

class InitialPagesView(ListView):
    model = Page
    template_name = 'pages/initial_pages.html'
    context_object_name = 'pages'
    ordering = ['-created_at']

class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        return queryset