from django.shortcuts import render
from apps.ruta.models import Ruta,Tipo_ruta
from apps.ruta.forms import rutaForm,TiporutaForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from django.utils.decorators import method_decorator
from apps.home.decoradores_viaje import permiso_staff
from django.contrib.auth.models import User

# Create your views here.

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_staff,name='dispatch')
class crear_ruta(CreateView):
    model = Ruta
    form_class = rutaForm
    template_name = "rutas_templates/ruta_form.html"
    success_url = "/rutas"

@permiso_staff
def listar_rutas(request):

    nombre_exato_ruta = request.GET.get("dato")
    qs = Ruta.objects.all()

    if nombre_exato_ruta != "" and nombre_exato_ruta is not None:
        qs = qs.filter(nombre_ruta__icontains=nombre_exato_ruta)

    context = {
        "object_list": qs,
    }

    return render(request, "rutas_templates/listar_rutas.html", context)

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_staff,name='dispatch')
class editar_ruta(UpdateView):
    model = Ruta
    form_class = rutaForm
    template_name = "rutas_templates/ruta_form.html"
    success_url = "/rutas"

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_staff,name='dispatch')
class borrar_ruta(DeleteView):
    model = Ruta
    template_name = "rutas_templates/ruta_delete.html"
    success_url = "/rutas"




#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_staff,name='dispatch')
class crear_tipo_ruta(CreateView):
    model = Tipo_ruta
    form_class = TiporutaForm
    template_name = "rutas_templates/tipo_ruta_form.html"
    success_url = "/tipo_ruta"

@permiso_staff
def listar_tipo_rutas(request):

    nombre_exato_tipo_ruta = request.GET.get("dato")
    qs = Tipo_ruta.objects.all()

    if nombre_exato_tipo_ruta != "" and nombre_exato_tipo_ruta is not None:
        qs = qs.filter(nombre__icontains=nombre_exato_tipo_ruta)

    context = {
        "object_list": qs,
    }

    return render(request, "rutas_templates/listar_tipo_ruta.html", context)


#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_staff,name='dispatch')
class editar_tipo_ruta(UpdateView):
    model = Tipo_ruta
    form_class = TiporutaForm
    template_name = "rutas_templates/tipo_ruta_form.html"
    success_url = "/tipo_ruta"

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_staff,name='dispatch')
class borrar_tipo_ruta(DeleteView):
    model = Tipo_ruta
    template_name = "rutas_templates/tipo_ruta_delete.html"
    success_url = "/tipo_ruta"
