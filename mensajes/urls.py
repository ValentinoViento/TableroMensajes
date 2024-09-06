from django.urls import path
from mensajes import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('mensajes/', views.ver_mensajes, name="mensajes"),
    path('crear/', views.crear_mensaje, name="crear"),
    path('eliminar/', views.eliminar_mensajes, name='eliminar'),
]
