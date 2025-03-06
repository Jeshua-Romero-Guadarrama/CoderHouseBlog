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
    path('', PageListView.as_view(), name='list'),
    path('<int:pk>/', PageDetailView.as_view(), name='detail'),
    path('create/', PageCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PageDeleteView.as_view(), name='delete'),
    path('', InitialPagesView.as_view(), name='home'),
]
