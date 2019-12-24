from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from apps.vendor.models import Vendor
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)

from apps.vendor.forms import VendorForm

from django.utils.decorators import method_decorator
from apps.home.decoradores_viaje import permiso_staff
from django.contrib.auth.models import User

# Create your views here.

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_staff,name='dispatch')
class crear_vendor(CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = "vendor_templates/vendor_form.html"
    success_url = "/vendor"

@permiso_staff
def listar_vendor(request):

    nombre_exato_vendor = request.GET.get("dato")
    qs = Vendor.objects.all()

    if nombre_exato_vendor != "" and nombre_exato_vendor is not None:
        qs = qs.filter(nombre_vendor__icontains=nombre_exato_vendor)

    context = {
        "object_list": qs,
    }

    return render(request, "vendor_templates/listar_vendor.html", context)

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_staff,name='dispatch')
class editar_vendor(UpdateView):
    model = Vendor
    form_class = VendorForm
    template_name = "vendor_templates/vendor_form.html"
    success_url = "/vendor"

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_staff,name='dispatch')
class borrar_vendor(DeleteView):
    model = Vendor
    template_name = "vendor_templates/vendor_delete.html"
    success_url = "/vendor"
