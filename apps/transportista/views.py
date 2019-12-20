from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, View
from apps.transportista.models import Transportista
from apps.transportista.forms import TransportistaForm


from django.utils.decorators import method_decorator
from apps.home.decoradores_viaje import premiso_admin
from apps.account.models import Account 
from apps.account.forms import registro_usuario_form

# Create your views here.

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
#@method_decorator(premiso_admin,name='dispatch')
def crear_transportista(request):

    if request:

        form = TransportistaForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('transportistas')
    else:
        return redirect('home')
    return render(request, 'transportistas_templates/transportista_form.html',{'form':form})


 


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
