from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.pasajero.models import Pasajero, Cuenta
from apps.pasajero.forms import PasajeroForm, CuentaForm



from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator

from django.utils.decorators import method_decorator
from apps.home.decoradores_viaje import premiso_admin
from django.contrib.auth.models import User


# importacion necesaria para Generar el QR
import qrcode
from PIL import Image


 
#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(premiso_admin,name='dispatch')
class crear_pasajero(CreateView):
    model = Pasajero
    template_name = "pasajeros_templates/pasajero_form.html"
    form_class = PasajeroForm
    success_url = "/pasajeros"

    # creacion del codigo QR al crear un pasajesor
    datos = ["carro", "bicicleta"]
    imagen = qrcode.make(datos)
    archivo_imagen = open("model.get", "wb")
    imagen.save(archivo_imagen)
    archivo_imagen.close()

@premiso_admin
def listar_pasajeros(request):

    id_exacto_pasajero = request.GET.get("dato")
    qs = Pasajero.objects.all()

    if id_exacto_pasajero != "" and id_exacto_pasajero is not None:
        qs = qs.filter(id_pasajero__icontains=id_exacto_pasajero)

    context = {
        "object_list": qs,
    }

    return render(request, "pasajeros_templates/listar_pasajeros.html", context)

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(premiso_admin,name='dispatch')
class editar_pasajero(UpdateView):
    model = Pasajero
    form_class = PasajeroForm
    template_name = "pasajeros_templates/pasajero_form.html"
    success_url = "/pasajeros"

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(premiso_admin,name='dispatch')
class borrar_pasajeros(DeleteView):
    model = Pasajero
    form_class = PasajeroForm
    template_name = "pasajeros_templates/pasajero_delete.html"
    success_url = "/pasajeros"

    # CUENTAS

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(premiso_admin,name='dispatch')
class crear_cuenta(CreateView):
    model = Cuenta
    template_name = "cuentas_templates/cuenta_form.html"
    form_class = CuentaForm
    success_url = "/cuentas"

@premiso_admin
def listar_cuentas(request):

    nombre_exacto_cuenta = request.GET.get("dato")
    qs = Cuenta.objects.all()

    if nombre_exacto_cuenta != "" and nombre_exacto_cuenta is not None:
        qs = qs.filter(nombre_cuenta__icontains=nombre_exacto_cuenta)

    context = {
        "object_list": qs,
    }

    return render(request, "cuentas_templates/listar_cuentas.html", context)

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(premiso_admin,name='dispatch')
class editar_cuenta(UpdateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = "cuentas_templates/cuenta_form.html"
    success_url = "/cuentas"

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(premiso_admin,name='dispatch')
class borrar_cuenta(DeleteView):
    model = Cuenta
    template_name = "cuentas_templates/cuenta_delete.html"
    success_url = "/cuentas"
