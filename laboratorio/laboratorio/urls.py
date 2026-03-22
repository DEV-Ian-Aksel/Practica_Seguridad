from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from app.views import panel
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Redirecciones por conveniencia
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('accounts/login/', RedirectView.as_view(url='/login/', permanent=False)),
    path('login/', app.views.login_view, name='custom_login'),

    # rutas de login/logout que ya trae Django
    path('accounts/', include('django.contrib.auth.urls')),
    path('panel/', panel, name='panel'),
    path('panel_admin/', app.views.panel_admin, name='panel_admin'),
    path('crear_curso/', app.views.crear_curso, name='crear_curso'),
]
