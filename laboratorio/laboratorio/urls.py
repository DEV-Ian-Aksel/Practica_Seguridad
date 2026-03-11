from django.contrib import admin
from django.urls import path, include
from app.views import panel

urlpatterns = [
    path('admin/', admin.site.urls),

    # rutas de login/logout que ya trae Django
    path('accounts/', include('django.contrib.auth.urls')),
    path('panel/', panel, name='panel'),
]
