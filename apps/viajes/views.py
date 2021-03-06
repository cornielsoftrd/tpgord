import imp
from time import time
from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, View, ListView, TemplateView, FormView, UpdateView, DeleteView
from django.core import serializers
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from apps.account.models import Account

import pytz

# from django.contrib.auth.models import User
# ya q creamos un modelo de usuario personalidado, debemos llamar a ese modelo envez de llamar al modelo del Framework
from apps.account.models import Account as User
from datetime import datetime,date

from django.utils.decorators import method_decorator



from apps.viajes.models import Viaje, ViajeAdministrativo,Excepciones
from apps.viajes.forms import viaje_form, viaje_admin_form
from apps.pasajero.models import Pasajero,Horario
from apps.ruta.models import Ruta
from apps.sites.models import Site
from apps.vendor.models import Vendor
from apps.transportista.models import Transportista
 
from datetime import datetime
import random


from apps.home.decoradores_viaje import permiso_staff, permiso_transportista, permiso_vendor


# numero_viaje: esta variable de se uililizara para crear el codigo de Viaje, este sera basado en la informacion del usuario y la fecha para asi generar un codigo unico
# el numero de viaje estara compuesto por "TPT-"+ 3 primeras letras de nombre de usuario usuario en mayuscula + dia + mes + año + hora actual al momento de hacer loguin + "-" + un numero random entre 100 y 10000 "
# se toman la hora actual y la fecha, esta se usara para crear la variable de sesion para el numero de viaje

fecha_tiempo = datetime.now()
hora_actual = str(fecha_tiempo.hour)
minuto_actual = str(fecha_tiempo.minute)
dia = str(fecha_tiempo.day)
mes = str(fecha_tiempo.month)
ano = str(fecha_tiempo.year)
numero_random = random.randint(100, 10000)

dia_actual=''
#obtener el dia actual para validad el horario filtrando por dia y pasajero en la tabla horarios
if datetime.date(datetime.today()).weekday()==0:
    dia_actual='lunes'
elif datetime.date(datetime.today()).weekday()==1:
    dia_actual='martes'
elif datetime.date(datetime.today()).weekday()==2:
    dia_actual='miercoles'
elif datetime.date(datetime.today()).weekday()==3:
    dia_actual='jueves'
elif datetime.date(datetime.today()).weekday()==4:
    dia_actual='viernes'
elif datetime.date(datetime.today()).weekday()==5:
    dia_actual='sabado'
elif datetime.date(datetime.today()).weekday()==6:
    dia_actual='domingo'



# aqui se crea el numero de viaje y se almacena en una variable de sesion, para posteriormente se urilizado
# este numero se usara para cosas como, indicar el numero de viaje en la base de datos, filtrar y organizar los viajes por numero de viajes
# mostrar los viajes de la sesion activa en el template listar_viaje_en_curso.html
@permiso_transportista
def generar_viaje(request):
    
    usuario_logueado = User.objects.get(username=request.user.username)
    
    tipo_viaje = request.POST["tipo_viaje"]
    hora_viaje = request.POST["hora_viaje"]

    # al general el viaje si no encuentra datos provinientes de la plantilla html, se asigna por defecto como transportista al usuario logueado
    #si el usuario logueado es admin, en la plantilla generar viaje se habilitara un dropdown para asignar el viaje al cualquier transportista registrado
    try:
        transportista_asignado=request.POST["transportista_asignado"]
    
    except:
        transportista_asignado=request.user.username
        
       
    
    try:
        nombre_usuario = request.user.username
        request.session["numero_viaje"] = (
            "TPG-"
            + str(nombre_usuario[:3]).upper()
            + dia
            + mes
            + ano
            + "-"
            + str(random.randint(1, 20000))
        )
        request.session["hora"] = hora_actual
        request.session["hora_viaje"] = hora_viaje
        request.session["tipo_viaje"] = tipo_viaje
        request.session["site_destino_origen"]=request.POST['site_destino_origen']
        request.session["transportista_asignado"]=transportista_asignado
        return redirect("crear_viaje")
    except Exception as e:
        messages.success(request, str(e)+' '+"Error al generar viaje")
        return redirect("crear_viaje")

@permiso_transportista
def finalizar_viaje(request):
    try:
        del request.session["hora"]
        del request.session["hora_viaje"]
        del request.session["tipo_viaje"] 
        del request.session["numero_viaje"]
        del  request.session["site_destino_origen"]
        del  request.session["transportista_asignado"]
        return redirect("crear_viaje")
    except Exception as e:
        messages.success(request, str(e)+"No se ha podido Terminar el viaje, Cierre sesion para Terminar")
        return redirect("crear_viaje")


#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_transportista,name='dispatch')
class agregar_viaje(CreateView):
    
    form_class = viaje_form
    template_name = "viajes_templates/viaje_form.html"

    
    def get(self, request, id_escaneado):
        
        usuario_logueado = User.objects.get(username=request.user.username)
        fecha_tiempo = datetime.now()

        # formatear hora a 12 horas
        hora_actual = fecha_tiempo.hour
        meridiano = fecha_tiempo.strftime("%p")

       

        # converir a formato de 12 horas logica

        # confirmar AM PM
        if hora_actual < 11 or hora_actual == 0:
            meridiano = "AM"
        else:
            meridiano = "PM"

        # pasajero_escaneado = serializers.serialize('json', Pasajero.objects.filter(id_pasajero=id_escaneado))

        # con el escaner se bueca el pasajero este Id es pasado por la URL, y capturado como parametro en la funcion agregar_viaje
        # luego este se usa para filtrar la lista de Pasajeros , ya q es una llave primaria deberia devolver solo un pasajero y este seria el 0, primero y unico
        # una vez se obtiene ese pasajero se puede acceder a cada atributo del pasajero y asignarle el valor a cada uno de los campos del modelo Viaje para agregar pasajeros a los viajes.
        try:
          
            horario=Horario.objects.filter(dia=dia_actual,pasajero=id_escaneado)#cargar el horario filtrando por el dia y id pasajero 
         
            pasajero_escaneado = Pasajero.objects.get(id_pasajero=id_escaneado)
            print('el pasajero')
            print(pasajero_escaneado.cuenta)


        

            id_pasajero = pasajero_escaneado
            nombre = pasajero_escaneado.nombre
            apellido = pasajero_escaneado.apellido
            direccion = pasajero_escaneado.direccion
            telefono = pasajero_escaneado.telefono
            ruta_pasajero = pasajero_escaneado.Ruta
            cuenta = pasajero_escaneado.cuenta
            site = pasajero_escaneado.site
            #hora_entrada = pasajero_escaneado[0].hora_entrada
            #hora_salida = pasajero_escaneado[0].hora_salida

            hora_entrada = horario[0].hora_entrada
            hora_salida = horario[0].hora_salida

        except (IndexError):
            messages.success(request, "No se encontro el pasajero, es posible que no exista o no tenga horario cargado para el dia de hoy")
            return redirect('crear_viaje')
        except Exception as e:
            messages.success(request, "error: "+ str(e))
            return redirect('crear_viaje')

        # para confirmar que el Pasajero esta dentro de su rango de hora para abordar el transporte
        # confirmamos que la hora actual sea igual a la hora de entrada, o que la hora actual sea igual a la hora de salida
        # de este modo la aplicacion crearia el viaje y dejaria abordar al pasajero en cualquiera de las dos horas

        if hora_actual == hora_entrada.hour or hora_actual == hora_salida.hour or hora_actual < hora_salida.hour:

            # se valida si el pasajero existe en el viaje actual, se toma el numero de viaje q es una variable de sesion y se toma el id escaneado
            # si se detecta el id_pasajero y el numero_viaje en el mismo objero del qeryset no se agrega el pasajero a viaje puesto que ese pasajero ya esta en ese viaje
            qs = Viaje.objects.filter(
                numero_viaje=request.session["numero_viaje"], id_pasajero=id_escaneado
            )
            if qs:
                messages.success(request, "El pasajero ya existe en este viaje")
                return redirect('crear_viaje')
                # print("ya Existe el pasajero")
            else:

                #se asigna el viaje a la cuenta de usuario del transportista, el id de esta cuenta es la misma que el Id de transportista 
                #esta cuenta se genera automaticamente al crear un nuevo transportista
                #de este modo, si en algun momento el transportista inicia sesion con su cuenta, podra ver todos los viajes que ha hecho, ya que estos se asignan a su cuenta
                codigo_transportista=request.session["transportista_asignado"]
                transportista_asignado=Account.objects.get(username=codigo_transportista)
              

                V = Viaje(
                    numero_viaje=request.session["numero_viaje"],
                    id_viaje=None,
                    transportista=transportista_asignado,
                    site_destino_origen=request.session["site_destino_origen"],
                    fecha_viaje=fecha_tiempo,
                    hora_viaje=request.session["hora_viaje"],
                    tipo_viaje=request.session["tipo_viaje"],
                    hora_entrada=hora_entrada,
                    hora_salida=hora_salida,
                    id_pasajero=id_pasajero,
                    nombre_pasajero=nombre,
                    apellido_pasajero=apellido,
                    campaña_pasajero=cuenta,
                    site_pasajero=site,
                    ruta_pasajero=ruta_pasajero,
                    direccion_pasajero=direccion,
                    # cantidad_pasajeros =5,
                    # precio_viaje =5,
                )
                if V:
                    V.save()
                    messages.success(request, "Se agrego el pasajero correctamente")
                    return redirect('crear_viaje')
        else:
            messages.success(
                request,
                "El Pasajero esta Fuera de su hora, si desea agregaro debe elegir la opcion manual",
            )
            return redirect('crear_viaje')
#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_transportista,name='dispatch')
class crear_viaje(View):
    model = Viaje
    form_class = viaje_form
    template_name = "viajes_templates/viaje_form.html"
    success_url = "listar_pasajeros"
    

    def get(self, request, *args, **kwargs):
        usuario_logueado = User.objects.get(username=request.user.username)

        lista_sites = Site.objects.all()
        lista_transportistas=Transportista.objects.all()
        transportista_logueado=Transportista.objects.all()

        context ={
        'lista_sites': lista_sites,
        'lista_transportistas': lista_transportistas,

        }
        return render(request, "viajes_templates/viaje_form.html", context)

    def post(self, request):
        
 
        # se valida si el pasajero existe en el viaje actual, se toma el numero de viaje q es una variable de sesion y se toma el id escaneado
        # si se detecta el id_pasajero y el numero_viaje en el mismo objero del qeryset no se agrega el pasajero a viaje puesto que ese pasajero ya esta en ese viaje
        usuario_logueado = User.objects.get(username=request.user.username)
        pasajero_escaneado = Pasajero.objects.get(id_pasajero=request.POST["id_pasajero"])
        ruta_pasajero=pasajero_escaneado.Ruta
        
        qs = Viaje.objects.filter(
            numero_viaje=request.session["numero_viaje"],
            id_pasajero=request.POST["id_pasajero"],
        )
        if qs:
            print("pasajero existe en este viaje")
            messages.warning(request, "El pasajero ya existe en este viaje")
            return redirect("crear_viaje")
        else:
            
            #se asigna el viaje a la cuenta de usuario del transportista, el id de esta cuenta es la misma que el Id de transportista 
            #esta cuenta se genera automaticamente al crear un nuevo transportista
            #de este modo, si en algun momento el transportista inicia sesion con su cuenta, podra ver todos los viajes que ha hecho, ya que estos se asignan a su cuenta
            codigo_transportista=request.session["transportista_asignado"]
            transportista_asignado=Account.objects.get(username=codigo_transportista)
              
        
            V = Viaje(
                numero_viaje=request.session["numero_viaje"],
                id_viaje=None,
                transportista=transportista_asignado,
                site_destino_origen=request.session["site_destino_origen"],
                fecha_viaje=request.POST["fecha_viaje"],
                hora_viaje=request.session["hora_viaje"],
                tipo_viaje=request.session["tipo_viaje"],
                hora_entrada=request.POST["hora_entrada"],
                hora_salida=request.POST["hora_salida"],
                id_pasajero=pasajero_escaneado,
                nombre_pasajero=pasajero_escaneado.nombre,
                apellido_pasajero=pasajero_escaneado.apellido,
                campaña_pasajero=pasajero_escaneado.cuenta,
                site_pasajero=pasajero_escaneado.site,
                ruta_pasajero=ruta_pasajero,
                direccion_pasajero=pasajero_escaneado.direccion,
                excepcion=request.POST["excepcion"],
                razon_excepcion=request.POST["razon_excepcion"],
                # cantidad_pasajeros =5,
                # precio_viaje =5,
            )
            if V:
                V.save()
                messages.success(request, "Se agrego el pasajero correctamente")
                return redirect("crear_viaje")
            else:
                messages.success(request, "Ha Habido un error Creando el Viaje")

                return redirect("crear_viaje")
#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_transportista,name='dispatch')
class agregar_viaje_manual(View):
    model = Viaje
    form_class = viaje_form
    # template_name = 'agregar_viaje_manual.html'
    success_url = "#"

    # obtener datos de usuario para llenar formulario automaticamente
    def get(self, request, id_ingresado):
         
        try:
            # pasajero_escaneado = serializers.serialize('json', Pasajero.objects.filter(id_pasajero=id_escaneado))

            # con el escaner se bueca el pasajero este Id es pasado por la URL, y capturado como parametro en la funcion agregar_viaje
            # luego este se usa para filtrar la lista de Pasajeros , ya q es una llave primaria deberia devolver solo un pasajero y este seria el 0, primero y unico
            # una vez se obtiene ese pasajero se puede acceder a cada atributo del pasajero y asignarle el valor a cada uno de los campos del modelo Viaje para agregar pasajeros a los viajes.
           

           

            horario=Horario.objects.filter(dia=dia_actual,pasajero=id_ingresado)#cargar el horario filtrando por el dia y id pasajero 
            pasajero_escaneado = Pasajero.objects.get(id_pasajero=id_ingresado)
            # strftime año mes dia %Y-%m-%d  devuelve hora mintu segundo %H:%M:%S
            fecha_tiempo = datetime.now().strftime("%Y-%m-%d")
            usuario_logueado = User.objects.get(username=request.user.username)

            #se asigna el viaje a la cuenta de usuario del transportista, el id de esta cuenta es la misma que el Id de transportista 
            #esta cuenta se genera automaticamente al crear un nuevo transportista
            #de este modo, si en algun momento el transportista inicia sesion con su cuenta, podra ver todos los viajes que ha hecho, ya que estos se asignan a su cuenta
            codigo_transportista=request.session["transportista_asignado"]
            transportista_asignado=Account.objects.get(username=codigo_transportista)

            #cargar excepciones para poner en dropdown con pool en los viajes manualas
            excepciones=Excepciones.objects.all()
              

            id_pasajero = pasajero_escaneado.id_pasajero
            nombre = pasajero_escaneado.nombre
            apellido = pasajero_escaneado.apellido
            direccion = pasajero_escaneado.direccion
            telefono = pasajero_escaneado.telefono
            ruta_pasajero = pasajero_escaneado.Ruta
            cuenta = pasajero_escaneado.cuenta
            site = pasajero_escaneado.site
            #hora_entrada = pasajero_escaneado[0].hora_entrada
            #hora_salida = pasajero_escaneado[0].hora_salida

            hora_entrada = horario[0].hora_entrada
            hora_salida = horario[0].hora_salida
        except (IndexError):
            messages.success(request, "No se encontro el pasajero, es posible que no exista o no tenga horario cargado para el dia de hoy")
            return redirect('crear_viaje')
        except Exception as e:
            messages.success(request, "error: "+ str(e))
            return redirect('crear_viaje')
            
        context = {
            "numero_viaje": request.session["numero_viaje"],
            "id_viaje": None,
            "transportista": transportista_asignado,
            'site_destino_origen':request.session["site_destino_origen"],
            "fecha_viaje": fecha_tiempo,
            "hora_entrada": hora_entrada,
            "hora_salida": hora_salida,
            "id_pasajero": id_pasajero,
            "nombre_pasajero": nombre,
            "apellido_pasajero": apellido,
            "campaña_pasajero": cuenta,
            "site_pasajero": site,
            "ruta_pasajero": ruta_pasajero,
            "direccion_pasajero": direccion,
            "excepciones":excepciones,
        }

        return render(request, "viajes_templates/agregar_viaje_manual.html", context)

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
#agregar un viaje casual es un pasajero que no esta registrado en la base de datos
@method_decorator(permiso_transportista,name='dispatch')
class agregar_viaje_casual(View):
    model = Viaje
    form_class = viaje_form
    # template_name = 'agregar_viaje_manual.html'
    success_url = "#"

    # obtener datos de usuario para llenar formulario automaticamente
    def get(self, request):
         
        try:

            fecha_tiempo = datetime.now().strftime("%Y-%m-%d")
            usuario_logueado = User.objects.get(username=request.user.username)

            #se asigna el viaje a la cuenta de usuario del transportista, el id de esta cuenta es la misma que el Id de transportista 
            #esta cuenta se genera automaticamente al crear un nuevo transportista
            #de este modo, si en algun momento el transportista inicia sesion con su cuenta, podra ver todos los viajes que ha hecho, ya que estos se asignan a su cuenta
            codigo_transportista=request.session["transportista_asignado"]
            transportista_asignado=Account.objects.get(username=codigo_transportista)
              

        except (IndexError):
            messages.success(request, "Error")
            return redirect('crear_viaje')
        except Exception as e:
            messages.success(request, "error: "+ str(e))
            return redirect('crear_viaje')
            
        context = {
            "numero_viaje": request.session["numero_viaje"],
            "id_viaje": None,
            "transportista": transportista_asignado,
            'site_destino_origen':request.session["site_destino_origen"],
            "fecha_viaje": fecha_tiempo,
         
        }

        return render(request, "viajes_templates/agregar_viaje_casual.html", context)



# esta funcion devuelve los viajes en curso, tomando como filtro el numero de viaje que que esta en el momento
@permiso_transportista
def listar_viaje_en_curso(request):

    try:
        
        qs = Viaje.objects.filter(numero_viaje=request.session["numero_viaje"]).order_by('-fecha_viaje')

        context = {
            "object_list": qs,

           
        }

        return render(request, "viajes_templates/listar_viaje_en_curso.html", context)
    except Exception as e:
        messages.success(request, str(e) +' '+ "Debe generar un numero de viaje primero")
        return redirect('home')

#esta funcion es para exluir a los pasajeros de los viajes en curso, asi se puede sacar un pasajero del viaje antes de comenzar y concluir el viaje
@method_decorator(permiso_transportista,name='dispatch')
class excluir_pasajero(DeleteView):
    model = Viaje
    template_name = "viajes_templates/excluir_pasajero.html"
    success_url="/viaje_en_curso"

#esta funcion es para Borrar los viajes 
@permiso_transportista
def borrar_viaje(request,numero_viaje):

    try:
        Viaje.objects.filter(numero_viaje=numero_viaje).delete()
        
        messages.success(request,'se ha eliminado el viaje satisfactoriamente')
        return redirect('home')
        
    except Exception as E:
        messages.success(request,'Ocurrio un error aliminando el viaje ' +str(E))

    return redirect('borrar_viaje')
        



# esta funcion devuelve los viajes que se han realizado por el transportista logueado al momento
@permiso_transportista
def mis_viajes(request):
 
    usuario_logueado = User.objects.get(username=request.user.username)
    numero_exacto_viaje = request.GET.get("dato")
    qs = Viaje.objects.filter(transportista=usuario_logueado).order_by('-fecha_viaje')

    if numero_exacto_viaje != "" and numero_exacto_viaje is not None:
        qs = qs.filter(
            transportista=usuario_logueado,
            numero_viaje__icontains=numero_exacto_viaje,
        ).order_by('-fecha_viaje')

    context = {
        "object_list": qs,
    }

    return render(request, "viajes_templates/listar_viajes_transportista_logueado.html", context)



@permiso_staff
def generar_viaje_admin(request):
     #si no es un Supe usuario o un Transportista la app manda un mensaje de eeor y lo envia al home
   

    try:
        nombre_usuario = request.user.username
        request.session["numero_viaje_admin"] = (
            "TPGAD-"
            + str(nombre_usuario[:3]).upper()
            + dia
            + mes
            + ano
            + "-"
            + str(random.randint(1, 20000))
        )
        request.session["hora"] = hora_actual
        return redirect("crear_viaje_admin")
    except KeyError:
        pass
    

#con method decorator se pueden poner decoradores sobre las clases, y hay q soobrescribir el nombre dispacth
@method_decorator(permiso_staff,name='dispatch')
class crear_viaje_admin(FormView):
    form_class =viaje_admin_form
    template_name = "viajes_templates/viaje_admin_form.html"
    success_url = 'viajes_admin'
    
    #con esta funcion se guarda el viaje administrativo, y se llama al metodo de enviar correo, para enviar un correo al vendor con la indormacion del Viaje para que este le de seguimiento
    def form_valid(self, form):

        try:
            form.save()
            self.enviar_correo()
            messages.success(self.request,"Viaje Creado, se enviaron una notificacion al vendor")
            return redirect('viajes_admin')
        except IndexError as e:
            messages.success(self.request,str(e)+ " "+ "Error")
            return redirect('crear_viaje_admin')
            

    def enviar_correo(self):
        #se busca el email del vendor elegigo
        id_vendor = self.request.POST.get('vendor') #obtiene el Id del vendor
        vendor = Vendor.objects.get(id_vendor=id_vendor) #obtiene todos los datos de Vendor donde el Id_vendor sea igual al id del vendor que se otubo del formulario
        email_vendor = vendor.email_vendor

        #creando direccion de viaje
        hostname= self.request.META['HTTP_HOST']
    
        #datos para correo
        numero_viaje = self.request.POST.get('numero_viaje')
        email_from = settings.EMAIL_HOST_USER

        subject = 'Nuevo Viaje Administrativo'
        mensaje = "Se le ha asignado un nuevo viaje administrativo\n\n"+"El numero de viaje es: "+str(numero_viaje)+".\n\n"+ "Inicie sesion en link debajo para mas informacion. \n\n"
        message_email = "Asunto: %s\n\nEnviado por: %s\n\nMensaje: %s\n\nAcceder: %s\n\n" %(subject, email_from, mensaje, hostname)
       
        recipient_list = [email_vendor]
        send_mail( subject, message_email, email_from, recipient_list )
        print(recipient_list, numero_viaje, hostname)
        pass

    
@permiso_staff
def listar_viajes_admin(request):
    
    numero_viaje_exacto = request.GET.get("dato")
    qs = ViajeAdministrativo.objects.all()

    if numero_viaje_exacto != "" and numero_viaje_exacto is not None:
        qs = qs.filter(numero_viaje__icontains=numero_viaje_exacto)

    context = {
        "object_list": qs,
    }

    return render(request, "viajes_templates/listar_viajes_administrativos.html", context)


#aqui se listan las solictudes de viajes administrativos para el vendor logueado

def solicitudes(request, *args, **kwargs):
    try:
        vendor_logueado = request.user.username
        numero_viaje_exacto = request.GET.get("dato")
        qs = ViajeAdministrativo.objects.filter(vendor=vendor_logueado)

        if numero_viaje_exacto != "" and numero_viaje_exacto is not None:
            qs = qs.filter(numero_viaje__icontains=numero_viaje_exacto)

        context = {
            "object_list": qs,
        }

        return render(request, "viajes_templates/listar_solicicitures_vendor.html", context)
    except Exception as e:
        pass


class cambiar_estatus_viaje(UpdateView):
    model = ViajeAdministrativo
    form_class = viaje_admin_form
    template_name = "viajes_templates/cambiar_estado_viaje.html"
    success_url ="solicitudes"
    


def crear_excepcion(request):
    if request.method=="POST":

        nombre_excepcion=request.POST['nombre_excepcion']
        detalle_excepcion=request.POST['detalle_excepcion']

        E= Excepciones(
            nombre_excepcion=nombre_excepcion,
            detalle_excepcion=detalle_excepcion,
        )

        E.save()
        return render(request,"excepciones_templates/excepciones_form.html")

    return render(request,"excepciones_templates/excepciones_form.html")


def listar_excepciones(request):
    nombre_exacto = request.GET.get("dato")

    if nombre_exacto!="" and nombre_exacto is not None:
        excepciones=Excepciones.objects.filter(nombre_excepcion__contains=nombre_exacto)
    
    else:
        excepciones=Excepciones.objects.all()

    context={
        'excepciones':excepciones
    }

    return render(request,"excepciones_templates/listar_excepciones.html",context)

def editar_excepcion(request,pk):
    excepciones=Excepciones.objects.filter(id=pk)


    try:
        excepciones.update(

        nombre_excepcion=request.POST['nombre_excepcion'],
        detalle_excepcion=request.POST['detalle_excepcion'],
    )
        return redirect('Excepciones')

    except:
        context={
            'excepciones':excepciones
        }

    return render(request,"excepciones_templates/excepciones_form.html",context)

def borrar_excepcion(request,pk):

    try:
        excepcione=Excepciones.objects.filter(id=pk)
        excepcione.delete()
        messages.success(request, "Se ha Elimindado correctamente la Excepcion")
    except Exception as e:
        messages.success(request, "No se ha podidio elinar la excepcion "+ e)


    return redirect('excepciones')

