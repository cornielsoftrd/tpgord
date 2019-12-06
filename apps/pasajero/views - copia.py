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
    success_url = "/listar_pasajeros"

    # creacion del codigo QR al crear un pasajesor
    datos = ["carro", "bicicleta"]
    imagen = qrcode.make(datos)
    archivo_imagen = open("model.get", "wb")
    imagen.save(archivo_imagen)
    archivo_imagen.close()


class listar_pasajero(ListView):
    model = Pasajero
    template_name = "listar_pasajeros.html"


class editar_pasajero(UpdateView):
    model = Pasajero
    form_class = PasajeroForm
    template_name = "pasajero_form.html"
    success_url = "/listar_pasajeros"


class borrar_pasajeros(DeleteView):
    model = Pasajero
    form_class = PasajeroForm
    template_name = "pasajero_delete.html"
    success_url = "/listar_pasajeros"

    # CUENTAS


class crear_cuenta(CreateView):
    model = Cuenta
    template_name = "cuenta_form.html"
    form_class = CuentaForm
    success_url = "/listar_cuentas"


class editar_cuenta(UpdateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = "cuenta_form.html"
    success_url = "/listar_cuentas"


class borrar_cuenta(DeleteView):
    model = Cuenta
    template_name = "cuenta_delete.html"
    success_url = "/listar_cuentas"


def listar_cuentas(request):

    nombre_cuenta_exacto = request.GET.get("cuenta")
    qs = Cuenta.objects.all()

    if nombre_cuenta_exacto != "" and nombre_cuenta_exacto is not None:
        qs = qs.filter(nombre_cuenta__icontains=nombre_cuenta_exacto)

    context = {
        "object_list": qs,
    }

    return render(request, "listar_cuentas.html", context)
