# blog/urls.py

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    InitialPostsView
)

app_name = 'blog'  

"""
En este archivo se definen las rutas (URLs) de la aplicación 'blog'.
Las vistas de clase (CBV) son importadas desde views.py.
"""

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('nuevo/', PostCreateView.as_view(), name='post_create'),
    path('editar/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('eliminar/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('', InitialPostsView.as_view(), name='home'),
]
