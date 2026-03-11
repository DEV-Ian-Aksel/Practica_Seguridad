import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laboratorio.settings")
django.setup()

from django.contrib.auth.models import User, Group

# Crear grupo admin
admin_group, created = Group.objects.get_or_create(name='Admin')

# Crear superuser
if not User.objects.filter(username='admin').exists():
    su = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    su.groups.add(admin_group)
    print("Usuario admin creado.")
else:
    print("Usuario admin ya existe.")

# Crear usuario normal
if not User.objects.filter(username='usuario').exists():
    u = User.objects.create_user('usuario', 'usuario@example.com', 'usuario123')
    print("Usuario normal creado.")
else:
    print("Usuario normal ya existe.")
