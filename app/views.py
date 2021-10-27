from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required
from .models import *


@login_required
def index(request):

    context = {
        'mensajes': Mensaje.objects.all(),
        'comentarios': Comentario.objects.all(),

    }
    return render(request, 'index.html', context)


@login_required
def crear_mensaje(request):
    print(request.POST)

    errors = Mensaje.objects.validador_mensaje(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        mensaje_creado = request.POST['mensaje']
        user_id_creador = request.session['usuario']['id']

        mensaje = Mensaje.objects.create(
            mensaje=mensaje_creado,
            user=User.objects.get(id=user_id_creador),
        )
        messages.success(request, "Mensaje agregado")

        return redirect(f"/")


@login_required
def crear_comentario(request):
    print(request.POST)

    errors = Comentario.objects.validador_comentario(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        comentario_creado = request.POST['comentario']
        id_mensaje = request.POST['id_mensaje_comentario']
        comentario_user_id = request.session['usuario']['id']

        comentario = Comentario.objects.create(
            comentario=comentario_creado,
            user=User.objects.get(id=comentario_user_id),
            mensaje=Mensaje.objects.get(id=id_mensaje),
        )
        messages.success(request, "Comentario agregado")

        return redirect(f"/")


@login_required
def eliminar_comentario(request, val):
    print(request.GET)
    eliminar = Comentario.objects.get(id=val)
    print("Aqui se va elimina el comentario ID=", val)
    eliminar.delete()

    return redirect("/")

