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


# Create your views here.


class crear_vendor(CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = "vendor_templates/vendor_form.html"
    success_url = "/vendor"


def listar_vendor(request):

    nombre_exato_vendor = request.GET.get("dato")
    qs = Vendor.objects.all()

    if nombre_exato_vendor != "" and nombre_exato_vendor is not None:
        qs = qs.filter(nombre_site__icontains=nombre_exato_vendor)

    context = {
        "object_list": qs,
    }

    return render(request, "vendor_templates/listar_vendor.html", context)


class editar_vendor(UpdateView):
    model = Vendor
    form_class = VendorForm
    template_name = "vendor_templates/vendor_form.html"
    success_url = "/vendor"


class borrar_vendor(DeleteView):
    model = Vendor
    template_name = "vendor_templates/vendor_delete.html"
    success_url = "/vendor"
