from django.shortcuts import render


from django.views.generic import CreateView
from apps.lectorQR.models import LectorQr
from apps.lectorQR.forms import lectorForm


# Create your views here.


class leer_qr(CreateView):
    model = LectorQr
    form_class = lectorForm
    template_name = "leer_qr.html"
