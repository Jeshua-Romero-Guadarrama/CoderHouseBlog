# messaging/urls.py

from django.urls import path
from .views import (
    InboxView,
    MessageDetailView,
    MessageCreateView,
)

app_name = 'messaging'

"""
Rutas (URLs) para la aplicación 'messaging'.
"""

urlpatterns = [
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('create/', MessageCreateView.as_view(), name='message_create'),
]
