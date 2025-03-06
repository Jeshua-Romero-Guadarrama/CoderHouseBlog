# blog/views.py

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm


"""
Vistas para la aplicación 'blog'. 
Ejemplo con vistas basadas en clases (Class-Based Views) de Django.
"""

class PostListView(ListView):
    """
    Muestra una lista de publicaciones (posts).
    """
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5  # Paginación: 5 elementos por página


class PostDetailView(DetailView):
    """
    Muestra el detalle de una publicación específica.
    """
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Permite crear una nueva publicación. Requiere que el usuario esté autenticado.
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        """
        Asigna el usuario actual como autor antes de guardar el formulario.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    Permite editar una publicación existente. Requiere login.
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        """
        Verifica que el usuario sea el autor del post o un superusuario, si no, redirige.
        """
        post = self.get_object()
        if post.author != request.user and not request.user.is_superuser:
            return redirect('blog:post_list')
        return super().dispatch(request, *args, **kwargs)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    Permite eliminar una publicación. Requiere login.
    """
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def dispatch(self, request, *args, **kwargs):
        """
        Verifica que el usuario sea el autor del post o un superusuario, si no, redirige.
        """
        post = self.get_object()
        if post.author != request.user and not request.user.is_superuser:
            return redirect('blog:post_list')
        return super().dispatch(request, *args, **kwargs)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 5  
