from django.shortcuts import render, redirect
from .models import Persona
import logging
import re


logger = logging.getLogger('security')


def index(request):
    return render(request, "index.html")

def listar(request):
    personas = Persona.objects.all()
    return render(request, "listar.html", {"personas": personas})


def is_suspicious(text):
    patterns = [r"('|--|;|OR|AND)", r"<script>"]
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def insertar(request):
    logger.info("Inicio de inserción de persona")
    
    endpoint = request.path 
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")
        ip = request.META.get('REMOTE_ADDR')

        if is_suspicious(nombre) or is_suspicious(email):
            logger.warning(f"Intento de inyección detectado | IP={ip} | nombre={nombre} | endpoint={endpoint} | resultado=blocked")

            return render(request, "insertar.html", {
                "error": "Entrada inválida detectada"
            })

        try:
            persona = Persona.objects.create(
                nombre=nombre,
                email=email,
                telefono=telefono
            )

            logger.info(f"Persona creada correctamente | ID={persona.id} | IP={ip} | endpoint={endpoint} | resultado=success")

            return redirect("listar")

        except Exception as e:
            logger.error(f"Error al insertar persona | Error={str(e)} | IP={ip} | endpoint={endpoint} | resultado=error")

    return render(request, "insertar.html")


def detalles(request, id):
    endpoint = request.path 
    ip = request.META.get('REMOTE_ADDR')

    logger.info(f"Acceso a detalles | ID={id} | IP={ip} | endpoint={endpoint} | resultado=success")

    try:
        persona = Persona.objects.get(id=id)
    except Persona.DoesNotExist:
        logger.warning(f"Detalle no encontrado | ID={id} | IP={ip} | endpoint={endpoint} | resultado=not_found")
        persona = None

    return render(request, "detalles.html", {"persona": persona})


def borrar(request, id):
    endpoint = request.path 
    ip = request.META.get('REMOTE_ADDR')

    logger.warning(f"Intento de eliminación | ID={id} | IP={ip} | endpoint={endpoint} | resultado=attempt")

    try:
        persona = Persona.objects.get(id=id)
        persona.delete()

        logger.info(f"Persona eliminada | ID={id} | IP={ip} | endpoint={endpoint} | resultado=success")

    except Persona.DoesNotExist:
        logger.error(f"Persona no encontrada | ID={id} | IP={ip} | endpoint={endpoint} | resultado=not_found")

    return redirect("listar")


def actualizar(request, id):
    endpoint = request.path 
    logger.info(f"Inicio de actualización | ID={id} | endpoint={endpoint} | resultado=attempt")

    ip = request.META.get('REMOTE_ADDR')

    try:
        persona = Persona.objects.get(id=id)
    except Persona.DoesNotExist:
        logger.error(f"Persona no encontrada | ID={id} | endpoint={endpoint} | resultado=not_found")
        return redirect("listar")

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")

        if is_suspicious(nombre) or is_suspicious(email):
            logger.warning(f"Intento sospechoso en actualización | ID={id} | IP={ip} | endpoint={endpoint} | resultado=blocked")

            return render(request, "actualizar.html", {
                "persona": persona,
                "persona_id": id,
                "error": "Entrada inválida detectada"
            })

        try:
            persona.nombre = nombre
            persona.email = email
            persona.telefono = request.POST.get("telefono")
            persona.save()

            logger.info(f"Persona actualizada correctamente | ID={id} | endpoint={endpoint} | resultado=success")

            return redirect("listar")

        except Exception as e:
            logger.error(f"Error al actualizar | ID={id} | Error={str(e)} | endpoint={endpoint} | resultado=error")

    return render(request, "actualizar.html", {
        "persona": persona,
        "persona_id": id
    })
