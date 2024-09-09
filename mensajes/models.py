from django.db import models


class Mensaje(models.Model):
    textoMensaje = models.TextField()
    remitente = models.CharField(max_length=15)
    destinatario = models.CharField(max_length=15)
    fechaEnvio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.remitente} -> {self.destinatario}: {self.textoMensaje[:200]}"
    