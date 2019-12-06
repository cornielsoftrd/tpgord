from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.pasajero.models import Pasajero, Cuenta
from apps.pasajero.forms import PasajeroForm, CuentaForm


# importacion necesaria para Generar el QR
import qrcode
from PIL import Image

# Create your views here.


class crear_pasajero(CreateView):
    model = Pasajero
    template_name = "pasajero_form.html"
    form_class = PasajeroForm
    success_url = "/pasajeros"

    # creacion del codigo QR al crear un pasajesor
    datos = ["carro", "bicicleta"]
    imagen = qrcode.make(datos)
    archivo_imagen = open("model.get", "wb")
    imagen.save(archivo_imagen)
    archivo_imagen.close()


def listar_pasajeros(request):

    id_exacto_pasajero = request.GET.get("dato")
    qs = Pasajero.objects.all()

    if id_exacto_pasajero != "" and id_exacto_pasajero is not None:
        qs = qs.filter(id_pasajero__icontains=id_exacto_pasajero)

    context = {
        "object_list": qs,
    }

    return render(request, "listar_pasajeros.html", context)


class editar_pasajero(UpdateView):
    model = Pasajero
    form_class = PasajeroForm
    template_name = "pasajero_form.html"
    success_url = "/pasajeros"


class borrar_pasajeros(DeleteView):
    model = Pasajero
    form_class = PasajeroForm
    template_name = "pasajero_delete.html"
    success_url = "/pasajeros"

    # CUENTAS


class crear_cuenta(CreateView):
    model = Cuenta
    template_name = "cuenta_form.html"
    form_class = CuentaForm
    success_url = "/cuentas"


def listar_cuentas(request):

    nombre_exacto_cuenta = request.GET.get("dato")
    qs = Cuenta.objects.all()

    if nombre_exacto_cuenta != "" and nombre_exacto_cuenta is not None:
        qs = qs.filter(nombre_cuenta__icontains=nombre_exacto_cuenta)

    context = {
        "object_list": qs,
    }

    return render(request, "listar_cuentas.html", context)


class editar_cuenta(UpdateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = "cuenta_form.html"
    success_url = "/cuentas"


class borrar_cuenta(DeleteView):
    model = Cuenta
    template_name = "cuenta_delete.html"
    success_url = "/cuentas"
