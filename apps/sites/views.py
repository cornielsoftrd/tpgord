from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from apps.sites.models import Site
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)

from apps.sites.forms import SiteForm

from django.utils.decorators import method_decorator
from apps.home.decoradores_viaje import premiso_admin
from django.contrib.auth.models import User

# Create your views here.

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(premiso_admin,name='dispatch')
class crear_site(CreateView):
    model = Site
    form_class = SiteForm
    template_name = "site_templates/site_form.html"
    success_url = "/sites"

@premiso_admin
def listar_sites(request):

    nombre_exato_site = request.GET.get("dato")
    qs = Site.objects.all()

    if nombre_exato_site != "" and nombre_exato_site is not None:
        qs = qs.filter(nombre_site__icontains=nombre_exato_site)

    context = {
        "object_list": qs,
    }

    return render(request, "site_templates/listar_sites.html", context)

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(premiso_admin,name='dispatch')
class editar_site(UpdateView):
    model = Site
    form_class = SiteForm
    template_name = "site_templates/site_form.html"
    success_url = "/sites"

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(premiso_admin,name='dispatch')
class borrar_site(DeleteView):
    model = Site
    template_name = "site_templates/site_delete.html"
    success_url = "/sites"
