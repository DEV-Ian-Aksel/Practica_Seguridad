# productos/views.py
import logging
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

logger = logging.getLogger('productos')


# CREATE
def crear_producto(request):
    logger.info("Inicio de creación de un producto")

    if request.method == 'POST':
        form = ProductoForm(request.POST)

        if form.is_valid():
            try:
                producto = form.save()
                logger.info(f"Producto creado correctamente | ID={producto.id}")
                return redirect('lista_productos')

            except Exception as e:
                logger.error(f"Error al crear producto | Error={str(e)}")

        else:
            logger.warning("Validación fallida al crear producto")

    else:
        form = ProductoForm()

    return render(request, 'productos/crear.html', {'form': form})


# READ
def lista_productos(request):
    logger.info("Consulta de lista de productos")

    try:
        productos = Producto.objects.all()

        if not productos:
            logger.warning("Lista de productos vacía")

    except Exception as e:
        logger.error(f"Error al consultar productos | Error={str(e)}")
        productos = []

    return render(request, 'productos/lista.html', {'productos': productos})


# UPDATE
def actualizar_producto(request, id):
    logger.info(f"Inicio de actualización | Producto ID={id}")

    try:
        producto = Producto.objects.get(id=id)
    except Producto.DoesNotExist:
        logger.error(f"Producto no encontrado | ID={id}")
        return redirect('lista_productos')

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)

        if form.is_valid():
            form.save()
            logger.info(f"Producto actualizado | ID={id}")
            return redirect('lista_productos')
        else:
            logger.warning(f"Validación fallida al actualizar | ID={id}")

    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productos/editar.html', {'form': form})



# DELETE
def eliminar_producto(request, id):
    logger.info(f"Intento de eliminación | ID={id}")

    try:
        producto = Producto.objects.get(id=id)
    except Producto.DoesNotExist:
        logger.error(f"Producto no encontrado | ID={id}")
        return redirect('lista_productos')

    try:
        producto.delete()
        logger.info(f"Producto eliminado | ID={id}")
    except Exception as e:
        logger.error(f"Error al eliminar producto | ID={id} | Error={str(e)}")

    return redirect('lista_productos')
