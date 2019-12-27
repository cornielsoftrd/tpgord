from django.shortcuts import render
import qrcode
from PIL import Image
from django.views.generic import CreateView
from apps.manejadoqr.models import crear_qr
from apps.manejadoqr.forms import qrForm

# Create your views here.


class creneradorqr(CreateView):
    model = crear_qr
    form_class = qrForm
    template_name = "qr_form.html"
    success_url = "#"

    # creacion del codigo QR
    datos = ["carro", "bicicleta"]
    imagen = qrcode.make(datos)
    archivo_imagen = open("mapecode.png", "wb")
    imagen.save(archivo_imagen)
    archivo_imagen.close()
