import logging
import uuid
import json
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
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

logger = logging.getLogger('app')

def generate_request_id():
    return str(uuid.uuid4())

def validate_login_data(data):
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return False, "Faltan credenciales (username o password requeridos).", None, None
    return True, None, username, password

@csrf_protect
def login_view(request):
    req_id = generate_request_id()
    
    # 1. Mostrar el formulario visual HTML
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})
        
    # 2. Procesar los datos que mande el frontend HTML
    elif request.method == 'POST':
        logger.info(f"[{req_id}] Inicio de proceso de login (Vía Interfaz Web)")
        
        try:
            # 1/0 #probar para el log Error
            # En web tradicional, los datos vienen en request.POST
            data = request.POST
            is_valid, error_msg, username, password = validate_login_data(data)
            
            if not is_valid:
                logger.warning(f"[{req_id}] Login fallido: {error_msg}")
                form = AuthenticationForm(request, data)
                # Recargamos la pag indicando error
                return render(request, 'registration/login.html', {'form': form, 'error': error_msg})

            logger.info(f"[{req_id}] Intentando autenticar al usuario username={username}")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                logger.info(f"[{req_id}] Login exitoso para el usuario username={username}, user_id={user.id}")
                return redirect('panel')
            else:
                logger.warning(f"[{req_id}] Login fallido: Credenciales incorrectas para username={username}")
                form = AuthenticationForm(request, data)
                form.add_error(None, 'Credenciales inválidas.')
                return render(request, 'registration/login.html', {'form': form})
                
        except Exception as e:
            logger.error(f"[{req_id}] Excepción inesperada durante el login: {str(e)}")
            form = AuthenticationForm()
            return render(request, 'registration/login.html', {'form': form, 'error': "Error interno del servidor."})
