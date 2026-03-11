# views.py
from django.http import HttpResponse
from django.db import connection

def buscar_usuario(request):

    email = request.GET.get("email")

    cursor = connection.cursor()

    query = f"SELECT * FROM users WHERE email = '{email}'"

    print(query)  # SOLO para evidencia

    cursor.execute(query)

    resultados = cursor.fetchall()

    return HttpResponse(str(resultados))
