from django.urls import path
from . import views

urlpatterns = [
    path("buscar_usuario/", views.buscar_usuario),
]
