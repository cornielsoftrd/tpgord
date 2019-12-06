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


# Create your views here.


class crear_site(CreateView):
    model = Site
    form_class = SiteForm
    template_name = "site_form.html"
    success_url = "/listar_site"


class listar_site(ListView):

    model = Site
    template_name = "listar_sites.html"


class editar_site(UpdateView):
    model = Site
    form_class = SiteForm
    template_name = "site_form.html"
    success_url = "/listar_site"


class borrar_site(DeleteView):
    model = Site
    template_name = "site_delete.html"
    success_url = "/listar_site"
