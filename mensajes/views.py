from django.shortcuts import render
from django.views import View
from .models import Mensaje
from django.http import HttpRequest, HttpResponse




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



class MensajeView(View):
    def post(self, request):
        remitente = request.POST.get('remitente')
        destinatario = request.POST.get('destinatario')
        textoMensaje = request.POST.get('textoMensaje')
        
        if Mensaje:
            mensaje = Mensaje(remitente=remitente, destinatario=destinatario, textoMensaje=textoMensaje)
            mensaje.save()
            return HttpResponse('El mensaje fue guardado', status = 201)
        else:
            return HttpResponse('Los datos en el mensaje son incorrectos', status = 400)    
  
        
def home_view(request):
    return render(request, 'home.html')

def mensajes_view(request):
    return render(request, 'mensaje_recibido_enviado.html')

def crear_view(request):
    return render(request, 'crear_mensaje.html')

def eliminar_view(request):
    return render(request, 'eliminar_mensaje.html')