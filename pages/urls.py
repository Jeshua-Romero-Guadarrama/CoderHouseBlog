# pages/urls.py

from django.urls import path
from .views import (
    PageListView,
    PageDetailView,
    PageCreateView,
    PageUpdateView,
    PageDeleteView,
    InitialPagesView
)

app_name = 'pages'

"""
Rutas (URLs) de la aplicación 'pages'.
Se utilizan vistas basadas en clases (CBV).
"""

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('initial/', InitialPagesView.as_view(), name='initial_pages'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('create/', PageCreateView.as_view(), name='page_create'),
    path('update/<int:pk>/', PageUpdateView.as_view(), name='page_update'),
    path('delete/<int:pk>/', PageDeleteView.as_view(), name='page_delete'),
]