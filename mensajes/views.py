from django.shortcuts import render, redirect
from django.views import View
from .models import Mensaje
from django.http import HttpRequest, HttpResponse
from .forms import MensajeForm




def ver_mensajes(request):
    mensajes_todos = Mensaje.objects.all()

    # Obtengo ambos valores para representarlos por separado
    remitente = request.GET.get('mensaje_remitente')
    destinatario = request.GET.get('mensaje_destinatario')

    # Decidir qué información envío según el filtro que utilice
    mensajes = mensajes_todos
    if remitente:
        mensajes = mensajes.filter(remitente=remitente)
    if destinatario:
        mensajes = mensajes.filter(destinatario=destinatario)

    return render(request, 'mensaje_recibido_enviado.html', {'mensajes': mensajes})


def crear_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eliminado')
    return render(request, 'eliminar_mensaje.html', {'form': form})
        
def home_view(request):
    return render(request, 'home.html')

def mensajes_view(request):
    return render(request, 'mensaje_recibido_enviado.html')

def crear_view(request):
    return render(request, 'crear_mensaje.html')

def eliminar_view(request):
    return render(request, 'eliminar_mensaje.html')