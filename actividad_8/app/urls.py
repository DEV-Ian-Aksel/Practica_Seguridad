from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar, name='listar'),
    path('insertar/', views.insertar, name='insertar'),
    path('actualizar/<str:id>/', views.actualizar, name='actualizar'),
    path('borrar/<str:id>/', views.borrar, name='borrar'),
    path('detalles/<str:id>/', views.detalles, name='detalles'),
]
