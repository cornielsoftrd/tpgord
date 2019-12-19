from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.transportista.models import Transportista
from apps.transportista.forms import TransportistaForm

# Create your views here.
class crear_transportista(CreateView):
    model = Transportista
    form_class = TransportistaForm
    template_name = "transportistas_templates/transportista_form.html"
    success_url = "/transportistas"


def listar_transportistas(request):

    nombre_exato_Transportista = request.GET.get("dato")
    qs = Transportista.objects.all()

    if nombre_exato_Transportista != "" and nombre_exato_Transportista is not None:
        qs = qs.filter(codigo_transportista__icontains=nombre_exato_Transportista)

    context = {
        "object_list": qs,
    }

    return render(request, "transportistas_templates/listar_transportistas.html", context)


class editar_transportista(UpdateView):
    model = Transportista
    form_class = TransportistaForm
    template_name = "transportistas_templates/transportista_form.html"
    success_url = "/transportistas"


class borrar_transportista(DeleteView):
    model = Transportista
    template_name = "transportistas_templates/transportista_delete.html"
    success_url = "/transportistas"
