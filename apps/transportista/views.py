from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView
from apps.transportista.models import Transportista
from apps.transportista.forms import TransportistaForm


from django.utils.decorators import method_decorator
from apps.home.decoradores_viaje import premiso_admin
from django.contrib.auth.models import User

# Create your views here.

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(premiso_admin,name='dispatch')
class crear_transportista(FormView):
    model = Transportista
    form_class = TransportistaForm
    template_name = "transportistas_templates/transportista_form.html"
    success_url = "/registrartr"
    def post(self, request):
        if request.method == 'POST':
        form = registro_usuario_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar')
       
        else:
            form = TransportistaForm()
        return render(request, 'registration/registro_susuarios.html',{'form':form})
@premiso_admin
def listar_transportistas(request):

    nombre_exato_Transportista = request.GET.get("dato")
    qs = Transportista.objects.all()

    if nombre_exato_Transportista != "" and nombre_exato_Transportista is not None:
        qs = qs.filter(codigo_transportista__icontains=nombre_exato_Transportista)

    context = {
        "object_list": qs,
    }

    return render(request, "transportistas_templates/listar_transportistas.html", context)

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(premiso_admin,name='dispatch')
class editar_transportista(UpdateView):
    model = Transportista
    form_class = TransportistaForm
    template_name = "transportistas_templates/transportista_form.html"
    success_url = "/transportistas"

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(premiso_admin,name='dispatch')
class borrar_transportista(DeleteView):
    model = Transportista
    template_name = "transportistas_templates/transportista_delete.html"
    success_url = "/transportistas"
