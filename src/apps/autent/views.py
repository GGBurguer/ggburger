from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario

# NOTA:
# A la aplicación le falta un algoritmo de encriptación para las contraseñas (FUNCIONAL)
# Conectar la base de datos y realizar las verificaciones de formulario contra la BD (FUNCIONAL)
# Implementar sistema de tokens de sesión (PENDIENTE)


# METODOS AUXILIARES #


# METODOS DE ACCESO A BD #
def cargar_usuario(request):
    msg = None
    nus = "pepe"
    cnt_us = "1122334455"
    cnt_us = make_password(cnt_us)
    print(cnt_us)
    usuario = Usuario(nombre_us=nus, contr_us=cnt_us)

    try:
        # Operación atomica
        with transaction.atomic():
            usuario.save()
            msg = "[EXITO] Entidad persistida..."
    except Exception as e:
        print(f"{e}")
        print("[ERROR] Fallo al persistir la entidad...")
        msg = "[ERROR] Fallo al persistir la entidad..."
    return HttpResponse(msg)


def buscar_usuario(usuario):
    try:
        us = Usuario.objects.get(nombre_us=usuario)
    except Exception as e:
        print(e)
        print("[ERROR] Usuario no encontrado...")
        return None
    return us


# METODOS DE VALIDACIÓN #
# Visualizar el formulario de inicio de sesion (PRUEBA)
def login_form_template(request):
    print("> Todo funcional!\n")
    return render(request, "autent_template.html")


# Metodo de inicio de sesion
def iniciar_sesion(request):
    if request.method != "POST":
        return HttpResponse("Acceso no permitido, metodo no aceptado!")

    # Usuario de prueba
    # usuario_x = {"us": "bbkmg", "contr": "12345"}
    usuario_x = buscar_usuario(request.POST["usuario_txt"])

    if usuario_x is None:
        return HttpResponse("Usuario o Contraseña incorrectos!")

    # if (
    #     request.POST["usuario_txt"] != usuario_x.nombre_us
    #     or request.POST["contr_txt"] != usuario_x.contr_us
    # ):
    #     return HttpResponse("Usuario o Contraseña incorrectos!")

    if request.POST["usuario_txt"] != usuario_x.nombre_us or not check_password(
        request.POST["contr_txt"], usuario_x.contr_us
    ):
        return HttpResponse("Usuario o Contraseña incorrectos!")

    return HttpResponse(f"Sesion iniciada, Bienvenido {usuario_x.nombre_us}!")
