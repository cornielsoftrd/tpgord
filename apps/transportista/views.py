from django.shortcuts import render,redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView,DeleteView
from apps.transportista.models import Transportista
from apps.transportista.forms import TransportistaForm


from django.utils.decorators import method_decorator
from apps.home.decoradores_viaje import permiso_staff
from django.contrib.auth.models import User

# Create your views here.

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_staff,name='dispatch')
class crear_transportista(FormView):
    model = Transportista
    form_class = TransportistaForm
    template_name = "transportistas_templates/transportista_form.html"
    success_url = 'home'

    def post(self,request):
        form = TransportistaForm(request.POST)
        if form.is_valid():
            form.save()

            #form2 = TransportistaForm(request.POST)

            #estos datos se usan para rellenar el formulario de registro de usuario para crear el usuario del Transportista
            context = {
                "email":request.POST.get('email'),
                "username":request.POST.get('codigo_transportista'),
                "first_name":request.POST.get('nombre'),
                "last_name":request.POST.get('apellido'),
                "phone":request.POST.get('telefono'),
                
                
            }
            return render(request,'registration/registro_usuarios.html',context)
        
        else:
            form = TransportistaForm()
        return render(request, 'registration/registro_usuarios.html',{'form':form})

@permiso_staff
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
@method_decorator(permiso_staff,name='dispatch')
class editar_transportista(UpdateView):
    model = Transportista
    form_class = TransportistaForm
    template_name = "transportistas_templates/transportista_form.html"
    success_url = "/transportistas"

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_staff,name='dispatch')
class borrar_transportista(DeleteView):
    model = Transportista
    template_name = "transportistas_templates/transportista_delete.html"
    success_url = "/transportistas"
