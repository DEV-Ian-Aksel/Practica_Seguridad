# Practica_Seguridad

Práctica de seguridad web desarrollada con **Django** y **FastAPI**, organizada en tres módulos independientes que demuestran distintos mecanismos de seguridad aplicados en aplicaciones web.

---

## 📁 Estructura del Proyecto

```
Practica_Seguridad/
├── carpeta/           # API REST con FastAPI y autenticación por token JWT
├── laboratorio/       # Aplicación Django con roles, CSRF, formularios y sesiones
└── sesiones_seguras/  # Aplicación Django enfocada en configuración segura de sesiones
```

---

## 🔐 1. Autenticación (Login)

El proyecto implementa autenticación en dos enfoques distintos:

- **Django (sesiones):** Se utiliza el sistema de autenticación integrado de Django, que provee un formulario de inicio de sesión listo para usar. Tras autenticarse correctamente, el usuario es redirigido a su panel correspondiente.

- **FastAPI (tokens JWT):** Se expone un endpoint `POST /login` que valida las credenciales del usuario, verifica la contraseña almacenada en formato seguro y devuelve un token de acceso firmado digitalmente con una fecha de expiración.

---

## 👥 2. Roles con Permisos Distintos

Se definen dos roles con niveles de acceso diferenciados:

| Rol | Acceso permitido |
|--------|-----------------|
| **Usuario** | Panel general (cualquier usuario autenticado) |
| **Administrador** | Panel de administración (grupo Admin o superusuario) |

El acceso a las vistas está protegido mediante decoradores de Django que verifican si el usuario está autenticado y si pertenece al rol requerido. Los usuarios sin los permisos necesarios son redirigidos automáticamente.

---

## 📝 3. Formulario con Validación de Datos

Se implementa un formulario para la creación de recursos (cursos) con las siguientes validaciones:

- **Campos requeridos:** ningún campo puede enviarse vacío.
- **Longitud:** se establecen límites mínimos y máximos de caracteres por campo.
- **Validación personalizada:** se rechaza contenido con términos no permitidos, lanzando un mensaje de error descriptivo.

Los datos procesados siempre provienen de los datos ya validados y limpiados por Django, nunca directamente del `request.POST`, lo que evita el uso de datos sin sanitizar.

---

## 🛡️ 4. Protección CSRF en Operaciones POST

Todos los formularios y endpoints POST están protegidos contra ataques **Cross-Site Request Forgery (CSRF)**:

- Se activa el middleware de CSRF de Django a nivel global en la configuración del proyecto.
- Los formularios HTML incluyen un token CSRF generado automáticamente por Django.
- Algunas vistas utilizan además el decorador `@csrf_protect` de forma explícita como capa adicional.
- Las cookies CSRF están configuradas con atributos de seguridad (`HttpOnly`, `SameSite`).

---

## 🔒 5. Sesiones Configuradas de Forma Segura

Las sesiones de usuario se configuran con los siguientes atributos de seguridad:

| Atributo | Descripción |
|----------|-------------|
| **HttpOnly** | La cookie de sesión no es accesible desde JavaScript, mitigando ataques XSS |
| **Secure** | La cookie solo se transmite por conexiones HTTPS (habilitado en producción) |
| **SameSite** | Restringe el envío de cookies en peticiones cross-site, reduciendo el riesgo de CSRF |
| **Expiración** | La sesión caduca automáticamente tras un tiempo definido de inactividad |
| **Cierre en browser close** | La sesión finaliza al cerrar el navegador, sin persistencia |

---

## 🚀 Cómo Ejecutar

### Django (`laboratorio/` y `sesiones_seguras/`)

```bash
cd laboratorio/
pip install -r ../requirements.txt
python manage.py migrate
python manage.py runserver
```

### FastAPI (`carpeta/`)

```bash
cd carpeta/
pip install -r ../requirements.txt
uvicorn main:app --reload
# Documentación interactiva en: http://127.0.0.1:8000/docs
```