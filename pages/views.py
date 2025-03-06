# pages/views.py

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Page
from .forms import PageForm

"""
Vistas para la aplicación 'pages'.
Incluye vistas basadas en clases para listar, detallar, crear, editar y borrar páginas.
"""

class PageListView(ListView):
    """
    Lista todas las páginas creadas.
    Si no hay páginas, en la plantilla puedes mostrar 'No hay páginas aún'.
    """
    model = Page
    template_name = 'pages/pages_list.html'
    context_object_name = 'pages'
    ordering = ['-created_at']

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
    success_url = reverse_lazy('pages:list')

class PageUpdateView(LoginRequiredMixin, UpdateView):
    """
    Permite editar una página existente. Requiere autenticación.
    """
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'

    def get_success_url(self):
        return reverse_lazy('pages:detail', kwargs={'pk': self.object.pk})

class PageDeleteView(LoginRequiredMixin, DeleteView):
    """
    Permite eliminar una página existente. Requiere autenticación.
    """
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages:list')

class InitialPagesView(ListView):
    model = Page
    template_name = 'pages/initial_pages.html'
    context_object_name = 'pages'
    ordering = ['-created_at']