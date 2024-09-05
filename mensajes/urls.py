from django.urls import path
from mensajes import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('mensajes/', views.mensajes_view, name="mensajes"),
    path('crear/', views.crear_view, name="crear"),
    path('eliminar/', views.eliminar_view, name='eliminar'),
]
