Actúa como un desarrollador senior en Django especializado en seguridad, arquitectura y logging profesional.

Tengo un módulo de login en Django que ya funciona, pero necesito refactorizarlo para que tenga código más limpio, estructurado y con logging bien implementado siguiendo buenas prácticas reales de producción.

🎯 Objetivo:
Refactorizar el módulo de login aplicando buenas prácticas de código, seguridad y logging estructurado, dejándolo listo para escalar a otros módulos como CRUD y API.

🟦 Requisitos obligatorios:

1. Logging en puntos clave del flujo:

* Inicio del proceso de login
* Validaciones de datos de entrada
* Intento de autenticación
* Resultado (login exitoso o fallido)
* Manejo de errores y excepciones

2. Uso correcto de niveles de logging:

* INFO: flujo normal (inicio, intento, éxito)
* WARNING: credenciales incorrectas o datos faltantes
* ERROR: errores controlados o excepciones
* CRITICAL: fallas graves del sistema (dejar preparado aunque no siempre se use)

3. Seguridad en logs (muy importante):

* NO registrar contraseñas
* NO registrar tokens
* NO registrar datos sensibles
* NO registrar el request completo
* Solo usar identificadores como username, user_id o request_id

4. Estructura de logs:

* Mensajes claros, cortos y profesionales
* Incluir request_id para trazabilidad
* Formato consistente
* Ejemplo esperado:
  [INFO] [request_id] Inicio de login
  [WARNING] [request_id] Login fallido username=juan

5. Código limpio y profesional:

* Separar validaciones en funciones auxiliares
* Usar funciones propias de Django (authenticate, login)
* Manejo correcto de excepciones con try/catch
* Código legible y organizado
* Evitar duplicación

6. Preparado para escalar:

* Estructura que permita mover lógica a services después
* Uso de funciones reutilizables (ej: validaciones, request_id)
* Código compatible con futuros módulos:
  • CRUD (usuarios, productos)
  • API REST (GET, POST, PUT, DELETE)

7. Contexto técnico:

* Django (views.py)
* Puede usar function-based views
* Usar logging.getLogger('app')
* Usar JsonResponse
* Método POST obligatorio
* Incluir decoradores como @require_POST
* Puede usar @csrf_exempt (opcional)

📦 Salida esperada:

1. Código completo del módulo de login refactorizado
2. Código bien estructurado y listo para producción básica
3. Logging correctamente aplicado en todo el flujo
4. Funciones auxiliares (validación, request_id)
5. Preparado para escalar a otros módulos
6. Explicación breve de por qué se colocaron los logs

📌 Restricciones:

* No hacer el código innecesariamente complejo
* Mantenerlo entendible (nivel estudiante avanzado)
* No usar librerías externas innecesarias

Aquí está mi código actual:
[PEGA AQUÍ TU CÓDIGO]
