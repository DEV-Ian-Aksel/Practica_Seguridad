from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from .forms import CrearCursoForm



@csrf_protect
def buscar_usuario(request):
    email = request.GET.get("email", "").strip()

    usuario = User.objects.filter(email=email).first()

    return render(request, "resultado.html", {
        "usuario": usuario,
        "email_buscado": email
    })

@login_required
def panel(request):
    # Panel general para todos los autenticados (Usuario normal y admin)
    return render(request, "panel.html")

# Función que verifica si el usuario pertenece al grupo 'Admin' o es superuser
def es_admin(user):
    return user.groups.filter(name='Admin').exists() or user.is_superuser

@login_required
@user_passes_test(es_admin)
def panel_admin(request):
    return render(request, "panel_admin.html")

@login_required
def crear_curso(request):
    if request.method == 'POST':
        form = CrearCursoForm(request.POST) 
        if form.is_valid(): 
            # form.cleaned_data tiene los datos seguros y validados
            nombre_curso = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            # (...) Guardar en la base de datos (Ejemplo, por ahora solo mostramos exito)
            return HttpResponse(f"Curso '{nombre_curso}' creado exitosamente")
    else:
        form = CrearCursoForm()
    
    return render(request, 'crear_curso.html', {'form': form})
