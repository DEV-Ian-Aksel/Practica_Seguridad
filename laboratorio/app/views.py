from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib.auth.models import User


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
    return HttpResponse("Panel seguro. Estás autenticado.")
