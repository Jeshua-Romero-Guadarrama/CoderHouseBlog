# messaging/views.py

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message
from .forms import MessageForm

"""
Vistas para la aplicación 'messaging':
- Inbox (lista de mensajes recibidos)
- Detalle de mensaje
- Creación de un nuevo mensaje
"""

class InboxView(LoginRequiredMixin, ListView):
    """
    Muestra la lista de mensajes que el usuario logueado ha recibido.
    """
    model = Message
    template_name = 'messaging/inbox.html'
    context_object_name = 'messages'

    def get_queryset(self):
        """
        Retorna solo los mensajes cuyo destinatario es el usuario actual.
        """
        return Message.objects.filter(to_user=self.request.user).order_by('-created_at')


class MessageDetailView(LoginRequiredMixin, DetailView):
    """
    Muestra el contenido de un mensaje.
    """
    model = Message
    template_name = 'messaging/message_detail.html'
    context_object_name = 'message'

    def get_queryset(self):
        """
        Restringe la vista solo a mensajes donde el usuario sea
        el remitente o el destinatario.
        """
        return Message.objects.filter(to_user=self.request.user) | Message.objects.filter(from_user=self.request.user)

    def get_object(self, queryset=None):
        """
        Marca el mensaje como leído si el usuario es el destinatario.
        """
        message = super().get_object(queryset)
        if message.to_user == self.request.user and not message.is_read:
            message.is_read = True
            message.save()
        return message


class MessageCreateView(LoginRequiredMixin, CreateView):
    """
    Permite al usuario enviar un nuevo mensaje.
    """
    model = Message
    form_class = MessageForm
    template_name = 'messaging/message_form.html'
    success_url = reverse_lazy('messaging:inbox')

    def form_valid(self, form):
        """
        Asigna el usuario actual como remitente antes de guardar.
        """
        form.instance.from_user = self.request.user
        return super().form_valid(form)
