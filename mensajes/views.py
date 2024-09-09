from django.shortcuts import render, redirect
from .models import Mensaje
from django.http import HttpRequest, HttpResponse
from .forms import MensajeForm




def ver_mensajes(request):
    remitente_filtro = request.GET.get('remitente_filtro')
    destinatario_filtro = request.GET.get('destinatario_filtro')

    mensajes = Mensaje.objects.all()

    if remitente_filtro:
        mensajes = mensajes.filter(remitente=remitente_filtro)
    if destinatario_filtro:
        mensajes = mensajes.filter(destinatario=destinatario_filtro)

    # Obtener mediante tuplas los valores, y quita los repetidos mediante el método .disctinct
    # Método flat para convertir la tupla en listas "simples", y mejorar el filtrador dinámico
    remitentes = Mensaje.objects.values_list('remitente', flat=True).distinct()             
    destinatarios = Mensaje.objects.values_list('destinatario', flat=True).distinct()

    return render(request, 'mensaje_recibido_enviado.html',
        {'mensajes': mensajes,
        'remitentes': remitentes,
        'destinatarios': destinatarios,})



def crear_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save()           #Si el formulario es válido, lo guarda
            return redirect('mensajes')         #redirección a los mensajes enviados/recibidos
    else:
        form = MensajeForm()
    return render(request, 'crear_mensaje.html', {'form': form})    #sino, devuelve la misma página/formulario
        
     
def eliminar_mensajes(request):
    if request.method == 'POST':
        mensaje_id = request.POST.getlist('seleccionar')
        Mensaje.objects.filter(id__in=mensaje_id).delete()  #selecciona y elimina mediante "id" los mensajes
        return redirect('mensajes')         #redirección a los mensajes enviados/recibidos
    else:
        mensajes = Mensaje.objects.all()
        return render(request, 'eliminar_mensaje.html', {'mensajes': mensajes}) #sino, devuelve la lista entera
     
       
        
def home_view(request):
    return render(request, 'home.html')

