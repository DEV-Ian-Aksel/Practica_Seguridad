# Practica_Seguridad

Práctica de seguridad web desarrollada con **Django** y **FastAPI**, organizada en tres módulos independientes que demuestran distintos mecanismos de seguridad aplicados en aplicaciones web.

---

## Estructura del Proyecto

```
Practica_Seguridad/
├── carpeta/           # API REST con FastAPI y autenticación por token JWT
├── laboratorio/       # Aplicación Django con roles, CSRF, formularios y sesiones
└── sesiones_seguras/  # Aplicación Django enfocada en configuración segura de sesiones
```

---

## 1. Autenticación (Login)

El proyecto implementa autenticación en dos enfoques distintos:

- **Django (sesiones):** Se utiliza el sistema de autenticación integrado de Django, que provee un formulario de inicio de sesión listo para usar.

- **FastAPI (tokens JWT):** Se expone un endpoint `POST /login` que valida las credenciales del usuario, verifica la contraseña almacenada en formato seguro y devuelve un token de acceso firmado digitalmente con una fecha de expiración.

---

## 2. Roles con Permisos Distintos

Se definen dos roles con niveles de acceso diferenciados:

| Rol | Acceso permitido |
|--------|-----------------|
| **Usuario** | Panel general (cualquier usuario autenticado) |
| **Administrador** | Panel de administración (grupo Admin o superusuario) |

El acceso a las vistas está protegido mediante decoradores de Django que verifican si el usuario está autenticado y si pertenece al rol requerido. Los usuarios sin los permisos necesarios son redirigidos automáticamente.

---

## 3. Formulario con Validación de Datos

Se implementa un formulario para la creación de recursos (cursos) con las siguientes validaciones:

