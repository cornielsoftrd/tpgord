from itertools import count
import site
from django.shortcuts import render, redirect
from django.views import View
from apps.vendor.models import Vendor
from apps.transportista.models import Transportista
from apps.pasajero.models import Pasajero
from apps.viajes.models import Viaje, ViajeAdministrativo
from apps.ruta.models import Ruta,Tipo_ruta
from apps.sites.models import Site
from django.db.models import Count, Sum, Avg, Q
from django.contrib import messages
from apps.pasajero.models import Cuenta


from django.utils.decorators import method_decorator
from apps.home.decoradores_viaje import permiso_staff, permiso_transportista, permiso_vendor

from datetime import datetime
import calendar

from django.views.defaults import page_not_found
# Create your views here.

@method_decorator(permiso_transportista,name='dispatch')
class home_View(View):
    def get(self, request, *args, **kwargs):
        
        lista_rutas=Ruta.objects.all()
        lista_sites=Site.objects.all()

        if request.GET.get('filtro_site'):
            site_nombre=request.GET.get('filtro_site')
            
        

             
            #query_site=Site.objects.filter(nombre_site=sites)
        else:
            site_nombre=''
            #query_site=Site.objects.all()

        lista_tipo_ruta=Tipo_ruta.objects.all()
        lista_cuentas=Cuenta.objects.all()

    
        

        #listado de año
        lista_anos = Viaje.objects.values('fecha_viaje__year').annotate(Count('fecha_viaje__year',distinct=True))
        lista_meses = Viaje.objects.values('fecha_viaje__month').annotate(Count('fecha_viaje__month',distinct=True))

        #este codigo filtra los graficos por año, si no se elige un año, el año se mostratan por defecto los datos del año en curso, de lo contrario se mstraran los datos del año seleccionado
        ano_exacto = request.GET.get("dato")
        ano_filtrado = datetime.now().year

        if ano_exacto != "" and ano_exacto is not None:
            ano_filtrado = ano_exacto

        #esta linea cuenta los viajes realizados donde el numero de viaje es distinto asi, se toma el numero de viaje exacto y no los cuenta por pasajeros agregados en el viaje
        cantidad_viajes =Viaje.objects.values('numero_viaje', 'fecha_viaje__year').annotate(Count('numero_viaje',distinct=True)).count 
        viajes_con_excepcion =Viaje.objects.filter(excepcion=True , fecha_viaje__year=ano_filtrado).count
        viajes_sin_excepcion =Viaje.objects.filter(excepcion=False , fecha_viaje__year=ano_filtrado).count

    

        #conteo de datos de viajse , rutas
        cantidad_vendors = Vendor.objects.all().count
        cantidad_transportistas =Transportista.objects.all().count
        cantidad_pasajeros =Pasajero.objects.all().count
        cantidad_viajes_admin = ViajeAdministrativo.objects.filter(fecha_viaje__year=ano_filtrado).count

        viajes_por_ruta= Viaje.objects.filter(fecha_viaje__year=ano_filtrado).values('ruta_pasajero','ruta_pasajero__nombre_ruta').annotate(Count('ruta_pasajero')) 
        

        #extraer viajes normales por mes para pasar al grafico de barras
        #aqui se cuentan los viajes por mes, contando los numeros de viajes distintos,asi un numero de viaje se contara una sola vez 
        viajes_enero= Viaje.objects.filter(fecha_viaje__month=1 , fecha_viaje__year=ano_filtrado).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #enero
        viajes_febrero= Viaje.objects.filter(fecha_viaje__month=2 , fecha_viaje__year=ano_filtrado).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count  # FEBRERO
        viajes_marzo= Viaje.objects.filter(fecha_viaje__month=3 , fecha_viaje__year=ano_filtrado).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #MARZO
        viajes_abril= Viaje.objects.filter(fecha_viaje__month=4 , fecha_viaje__year=ano_filtrado ).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #ABRIL
        viajes_mayo= Viaje.objects.filter(fecha_viaje__month=5 , fecha_viaje__year=ano_filtrado).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #MAYO
        viajes_junio= Viaje.objects.filter(fecha_viaje__month=6 , fecha_viaje__year=ano_filtrado).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #JUNIO
        viajes_julio= Viaje.objects.filter(fecha_viaje__month=7 , fecha_viaje__year=ano_filtrado).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #JULIO
        viajes_agosto= Viaje.objects.filter(fecha_viaje__month=8 , fecha_viaje__year=ano_filtrado).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #AGOSTO
        viajes_septiembre= Viaje.objects.filter(fecha_viaje__month=9 , fecha_viaje__year=ano_filtrado).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #SEPTIMBRE
        viajes_octubre= Viaje.objects.filter(fecha_viaje__month=10 , fecha_viaje__year=ano_filtrado).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #OCTUBRE
        viajes_noviembre= Viaje.objects.filter(fecha_viaje__month=11 , fecha_viaje__year=ano_filtrado).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #NOVIEMBRE
        viajes_diciembre= Viaje.objects.filter(fecha_viaje__month=12 , fecha_viaje__year=ano_filtrado).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #DICIEMBRE


    #aqui se contaran los agentes llevados cada mes, contanto todas las vilas de viajes de ese mes, 
        pasajeros_viajes_enero= Viaje.objects.filter(fecha_viaje__month=1 , fecha_viaje__year=ano_filtrado ).count
        pasajeros_viajes_febrero= Viaje.objects.filter(fecha_viaje__month=2 , fecha_viaje__year=ano_filtrado ).count
        pasajeros_viajes_marzo= Viaje.objects.filter(fecha_viaje__month=3 , fecha_viaje__year=ano_filtrado ).count
        pasajeros_viajes_abril= Viaje.objects.filter(fecha_viaje__month=4 , fecha_viaje__year=ano_filtrado ).count
        pasajeros_viajes_mayo= Viaje.objects.filter(fecha_viaje__month=5 , fecha_viaje__year=ano_filtrado ).count
        pasajeros_viajes_junio= Viaje.objects.filter(fecha_viaje__month=6 , fecha_viaje__year=ano_filtrado ).count
        pasajeros_viajes_julio= Viaje.objects.filter(fecha_viaje__month=7 , fecha_viaje__year=ano_filtrado ).count
        pasajeros_viajes_agosto= Viaje.objects.filter(fecha_viaje__month=8 , fecha_viaje__year=ano_filtrado ).count
        pasajeros_viajes_septiembre= Viaje.objects.filter(fecha_viaje__month=9 , fecha_viaje__year=ano_filtrado ).count
        pasajeros_viajes_octubre= Viaje.objects.filter(fecha_viaje__month=10 , fecha_viaje__year=ano_filtrado ).count
        pasajeros_viajes_noviembre= Viaje.objects.filter(fecha_viaje__month=11 , fecha_viaje__year=ano_filtrado ).count
        pasajeros_viajes_diciembre= Viaje.objects.filter(fecha_viaje__month=12 , fecha_viaje__year=ano_filtrado ).count


        
        mes_actual=datetime.now().month
    
    
        try:
            mes_filtrado=request.GET.get('mes')
            if mes_filtrado != "" and mes_filtrado is not None:
                mes_actual=mes_filtrado
            
        except Exception as E:
            messages.error(request,"Error al filtar el mes "+str(E))

        #calcular el costo de los viajes hechos por dia
        #calcular la cantidad de dias que tiene el mes actual
        
        dias_mes_actual=calendar.monthrange(int(ano_filtrado),int(mes_actual))[1]
        dias=0
        lista_dias=[]
        while dias < dias_mes_actual:
            dias=dias+1
            lista_dias.append(dias)
            
            
        #calcular la cantidad de viajes por dia agrupando los viajes por fecha, pasandole una lista de dias del mes acual al dia de la fecha de viaje
        #pasandole esta lista el query busca 1 po 1 en cada fecha de numero de la lista, que coresponde a 1 dia del mes 
        #esta lista de dias se saca 1 opteniendo el mes actual,2 con la libreria calendar obtenemos el rango de dias del mes actual
        #este rango de dias es almacenado en la variable lista_dias la cual es una lista y por ultimo se le pasa esa lista como filtro de la consula en la variable fecha_viaje
        
        viajes=Viaje.objects.all()

        #validar si se ha elegido un site en el canpo filtro_site
        # si es asi, tambien se filtra por site 

        if site_nombre !='' and site_nombre is not None:
            
           
       
            viajes_diarios=viajes.filter(fecha_viaje__year=ano_filtrado, fecha_viaje__day__in=lista_dias,fecha_viaje__month=mes_actual,site_destino_origen=site_nombre).values('fecha_viaje').annotate(Count('numero_viaje',distinct=True)
            
            )
                
            pasajeros_diarios=viajes.filter(fecha_viaje__year=ano_filtrado, fecha_viaje__day__in=lista_dias,fecha_viaje__month=mes_actual,site_destino_origen=site_nombre).values('fecha_viaje').annotate(Count('fecha_viaje',distinct=False)
            
            ).annotate(Count('id_pasajero'))

            pasajeros_por_hora=viajes.filter(fecha_viaje__year=ano_filtrado, fecha_viaje__day__in=lista_dias,fecha_viaje__month=mes_actual,site_destino_origen=site_nombre).values('hora_viaje').annotate(Count('hora_viaje',distinct=False)
            
            ).annotate(Count('id_pasajero'))
            
           
        else:
            viajes_diarios=viajes.filter(fecha_viaje__year=ano_filtrado, fecha_viaje__day__in=lista_dias,fecha_viaje__month=mes_actual).values('fecha_viaje').annotate(Count('numero_viaje',distinct=True)
            
            )
                
            pasajeros_diarios=viajes.filter(fecha_viaje__year=ano_filtrado, fecha_viaje__day__in=lista_dias,fecha_viaje__month=mes_actual).values('fecha_viaje').annotate(Count('fecha_viaje',distinct=False)
            
            ).annotate(Count('id_pasajero'))
            

            pasajeros_por_hora=viajes.filter(fecha_viaje__year=ano_filtrado, fecha_viaje__day__in=lista_dias,fecha_viaje__month=mes_actual).values('hora_viaje').annotate(Count('hora_viaje',distinct=False)
            
            ).annotate(Count('id_pasajero'))

            
       
            
        context={

        

        'cantidad_vendors':cantidad_vendors,
        'cantidad_transportistas':cantidad_transportistas,
        'cantidad_pasajeros':cantidad_pasajeros,
        'cantidad_viajes_admin':cantidad_viajes_admin,
        'cantidad_viajes':cantidad_viajes,
        'viajes_con_excepcion':viajes_con_excepcion,
        'viajes_sin_excepcion':viajes_sin_excepcion,

        #filtros
        'ano_filtrado': ano_filtrado,
        'lista_anos': lista_anos,
        'lista_meses': lista_meses,


        #viajes por mes
        'viajes_enero' : viajes_enero,
        'viajes_febrero' : viajes_febrero,
        'viajes_marzo' : viajes_marzo,
        'viajes_abril' : viajes_abril,
        'viajes_mayo' : viajes_mayo,
        'viajes_junio' : viajes_junio,
        'viajes_julio' : viajes_julio,
        'viajes_agosto' : viajes_agosto,
        'viajes_septiembre' : viajes_septiembre,
        'viajes_octubre' : viajes_octubre,
        'viajes_noviembre' : viajes_noviembre,
        'viajes_diciembre' : viajes_diciembre,

        #cantidad de viajes por dias
        'viajes_diarios':viajes_diarios,

        #cantidad de pasajeros transportados al dia
        'pasajeros_diarios':pasajeros_diarios,

        #cantidad de pasajeros transportados por hora
        'pasajeros_por_hora':pasajeros_por_hora,


        #viajes Por ruta
        'viajes_por_ruta':viajes_por_ruta,

        #pasajeros llevados Por Mes por mes
        'pasajeros_viajes_enero' : pasajeros_viajes_enero,
        'pasajeros_viajes_febrero' : pasajeros_viajes_febrero,
        'pasajeros_viajes_marzo' : pasajeros_viajes_marzo,
        'pasajeros_viajes_abril' : pasajeros_viajes_abril,
        'pasajeros_viajes_mayo' : pasajeros_viajes_mayo,
        'pasajeros_viajes_junio' : pasajeros_viajes_junio,
        'pasajeros_viajes_julio' : pasajeros_viajes_julio,
        'pasajeros_viajes_agosto' : pasajeros_viajes_agosto,
        'pasajeros_viajes_septiembre' : pasajeros_viajes_septiembre,
        'pasajeros_viajes_octubre' : pasajeros_viajes_octubre,
        'pasajeros_viajes_noviembre' : pasajeros_viajes_noviembre,
        'pasajeros_viajes_diciembre' : pasajeros_viajes_diciembre,
        

        'lista_rutas':lista_rutas,
        'lista_tipo_ruta':lista_tipo_ruta,
        'lista_cuentas':lista_cuentas,
        'lista_sites':lista_sites
        

        
        }
        return render(request, "dashboard/index.html", context)



@permiso_transportista
def costos(request):


    lista_rutas=Ruta.objects.all()
    lista_tipo_ruta=Tipo_ruta.objects.all()
    lista_cuentas=Cuenta.objects.all()

    viajes_ruta=Viaje.objects.all()
    dato = request.GET.get("dato")

    
    mes_actual=datetime.now().month
    
    
    try:
        mes_filtrado=request.GET.get('mes')
        if mes_filtrado != "" and mes_filtrado is not None:
            mes_actual=mes_filtrado
    
        
    except Exception as E:
       messages.error(request,"Error al filtar el mes "+str(E))

    ano_exacto=request.GET.get("ano_exacto")

    dato = request.GET.get("dato")
    tipo_ruta_filtrado=lista_tipo_ruta.get(id=dato)
    ano_filtrado = datetime.now().year

    costo_viaje=0

    try:

        if ano_exacto != "" and ano_exacto is not None:
            ano_filtrado = ano_exacto

        #esta linea cuenta los viajes realizados donde el numero de viaje es distinto asi, se toma el numero de viaje exacto y no los cuenta por pasajeros agregados en el viaje
        cantidad_viajes =Viaje.objects.values('numero_viaje', 'fecha_viaje__year').annotate(Count('numero_viaje',distinct=True)).count 
        viajes_con_excepcion =Viaje.objects.filter(excepcion=True , fecha_viaje__year=ano_filtrado,ruta_pasajero__tipo_ruta=dato).count
        viajes_sin_excepcion =Viaje.objects.filter(excepcion=False , fecha_viaje__year=ano_filtrado,ruta_pasajero__tipo_ruta=dato).count
        total_viajes =Viaje.objects.filter(fecha_viaje__year=ano_filtrado,ruta_pasajero__tipo_ruta=dato).count
        lista_anos = Viaje.objects.values('fecha_viaje__year').annotate(Count('fecha_viaje__year',distinct=True))
        lista_meses = Viaje.objects.values('fecha_viaje__month').annotate(Count('fecha_viaje__month',distinct=True))

        

        if dato != "" and dato is not None:
            
            viajes_ruta=Ruta.objects.get(id_ruta=dato)
            precio_ruta=viajes_ruta.precio_ruta
            #total_viajes=Ruta.objects.filter(fecha_viaje__year=2021).values()
            
            
            #extraer viajes normales por mes para pasar al grafico de barras
            #aqui se cuentan los viajes por mes, contando los numeros de viajes distintos,asi un numero de viaje se contara una sola vez 
            viajes_enero= Viaje.objects.filter(fecha_viaje__month=1 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #enero
            viajes_febrero= Viaje.objects.filter(fecha_viaje__month=2 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count  # FEBRERO
            viajes_marzo= Viaje.objects.filter(fecha_viaje__month=3 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #MARZO
            viajes_abril= Viaje.objects.filter(fecha_viaje__month=4 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato ).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #ABRIL
            viajes_mayo= Viaje.objects.filter(fecha_viaje__month=5 , fecha_viaje__year=ano_filtrado,ruta_pasajero__tipo_ruta=dato ).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #MAYO
            viajes_junio= Viaje.objects.filter(fecha_viaje__month=6 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #JUNIO
            viajes_julio= Viaje.objects.filter(fecha_viaje__month=7 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #JULIO
            viajes_agosto= Viaje.objects.filter(fecha_viaje__month=8 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #AGOSTO
            viajes_septiembre= Viaje.objects.filter(fecha_viaje__month=9 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #SEPTIMBRE
            viajes_octubre= Viaje.objects.filter(fecha_viaje__month=10 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #OCTUBRE
            viajes_noviembre= Viaje.objects.filter(fecha_viaje__month=11 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #NOVIEMBRE
            viajes_diciembre= Viaje.objects.filter(fecha_viaje__month=12 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #DICIEMBRE
            


            #calcular el costo de los viajes hechos por dia
            #calcular la cantidad de dias que tiene el mes actual
            
            dias_mes_actual=calendar.monthrange(int(ano_filtrado),int(mes_actual))[1]
            dias=0
            lista_dias=[]
            while dias < dias_mes_actual:
                dias=dias+1
                lista_dias.append(dias)
                
                
            #calcular la cantidad de viajes por dia agrupando los viajes por fecha, pasandole una lista de dias del mes acual al dia de la fecha de viaje
            #pasandole esta lista el query busca 1 po 1 en cada fecha de numero de la lista, que coresponde a 1 dia del mes 
            #esta lista de dias se saca 1 opteniendo el mes actual,2 con la libreria calendar obtenemos el rango de dias del mes actual
            #este rango de dias es almacenado en la variable lista_dias la cual es una lista y por ultimo se le pasa esa lista como filtro de la consula en la variable fecha_viaje
            
            viajes=Viaje.objects.all()
            viajes_diarios=viajes.filter(fecha_viaje__year=ano_filtrado, fecha_viaje__day__in=lista_dias,fecha_viaje__month=mes_actual,  ruta_pasajero__tipo_ruta=dato).values('fecha_viaje').annotate(Count('fecha_viaje',distinct=False)) #Lunes
            
         

        else:
            viajes_ruta=Viaje.objects.all()
            precio_ruta=1


        
        context={
        'lista_rutas':lista_rutas,
        'lista_tipo_ruta':lista_tipo_ruta,
        'tipo_ruta_filtrado':tipo_ruta_filtrado,
        'viajes_ruta':viajes_ruta,
        'precio_ruta':precio_ruta,
        'ruta_filtrado':viajes_ruta.nombre_ruta,
        'total_viajes':total_viajes,
        'cantidad_viajes':cantidad_viajes,
        'viajes_con_excepcion':viajes_con_excepcion,
        'viajes_sin_excepcion':viajes_sin_excepcion,
        'lista_anos':lista_anos,
        'lista_meses':lista_meses,

        #viajes diarios
        'lista_dias':lista_dias,
        'viajes_diarios':viajes_diarios,

        #lista de cuentas
        'lista_cuentas':lista_cuentas,




        #viajes por mes
        'viajes_enero' : viajes_enero,
        'viajes_febrero' : viajes_febrero,
        'viajes_marzo' : viajes_marzo,
        'viajes_abril' : viajes_abril,
        'viajes_mayo' : viajes_mayo,
        'viajes_junio' : viajes_junio,
        'viajes_julio' : viajes_julio,
        'viajes_agosto' : viajes_agosto,
        'viajes_septiembre' : viajes_septiembre,
        'viajes_octubre' : viajes_octubre,
        'viajes_noviembre' : viajes_noviembre,
        'viajes_diciembre' : viajes_diciembre,


        #pasajeros por dia

        
        
    }

        return render(request, "dashboard/costos.html", context)

    except Exception as E:
        messages.success(request,"Seleccione un filtro en la opcion costos del menu" + str(E))
        
        return redirect('home')

@permiso_transportista
def cuentas_overview(request):


    lista_rutas=Ruta.objects.all()
    lista_tipo_ruta=Tipo_ruta.objects.all()
    lista_cuentas=Cuenta.objects.all()
    

    viajes_ruta=Viaje.objects.all()
    dato = request.GET.get("dato")

    
    mes_actual=datetime.now().month

    try:
        cuenta_id=request.GET.get('cuenta')
        cuenta_filtrado=Cuenta.objects.get(id_cuenta=cuenta_id)
    except:
        cuenta_filtrado=None
    
    
    try:
        mes_filtrado=request.GET.get('mes')
        if mes_filtrado != "" and mes_filtrado is not None:
            mes_actual=mes_filtrado
    
        
    except Exception as E:
       messages.error(request,"Error al filtar el mes "+str(E))


    try:
        cuenta_id=request.GET.get('cuenta')
        cuenta_filtrado=Cuenta.objects.get(id_cuenta=cuenta_id)
        if cuenta_filtrado != "" and cuenta_filtrado is not None:
            cuenta=cuenta_filtrado
        else:
            cuenta=None
        print("la cuenta filtrada es")
        print(cuenta)
    
        
    except Exception as E:
       messages.error(request,"Error al filtar el mes "+str(E))

    ano_exacto=request.GET.get("ano_exacto")

    dato = request.GET.get("dato")
    tipo_ruta_filtrado=lista_tipo_ruta.get(id=dato)
    ano_filtrado = datetime.now().year

    costo_viaje=0

    try:

        if ano_exacto != "" and ano_exacto is not None:
            ano_filtrado = ano_exacto

        #esta linea cuenta los viajes realizados donde el numero de viaje es distinto asi, se toma el numero de viaje exacto y no los cuenta por pasajeros agregados en el viaje
        cantidad_viajes =Viaje.objects.values('numero_viaje', 'fecha_viaje__year').annotate(Count('numero_viaje',distinct=True)).count 
        viajes_con_excepcion =Viaje.objects.filter(excepcion=True , fecha_viaje__year=ano_filtrado,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta).count
        viajes_sin_excepcion =Viaje.objects.filter(excepcion=False , fecha_viaje__year=ano_filtrado,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta).count
        total_viajes =Viaje.objects.filter(fecha_viaje__year=ano_filtrado,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta).count
        lista_anos = Viaje.objects.values('fecha_viaje__year').annotate(Count('fecha_viaje__year',distinct=True))
        lista_meses = Viaje.objects.values('fecha_viaje__month').annotate(Count('fecha_viaje__month',distinct=True))

        

        if dato != "" and dato is not None:
            
            viajes_ruta=Ruta.objects.get(id_ruta=dato)
            precio_ruta=viajes_ruta.precio_ruta
            #total_viajes=Ruta.objects.filter(fecha_viaje__year=2021).values()
            
            
            #extraer viajes normales por mes para pasar al grafico de barras
            #aqui se cuentan los viajes por mes, contando los numeros de viajes distintos,asi un numero de viaje se contara una sola vez 
            viajes_enero= Viaje.objects.filter(fecha_viaje__month=1 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #enero
            viajes_febrero= Viaje.objects.filter(fecha_viaje__month=2 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count  # FEBRERO
            viajes_marzo= Viaje.objects.filter(fecha_viaje__month=3 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #MARZO
            viajes_abril= Viaje.objects.filter(fecha_viaje__month=4 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta ).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #ABRIL
            viajes_mayo= Viaje.objects.filter(fecha_viaje__month=5 , fecha_viaje__year=ano_filtrado,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta ).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #MAYO
            viajes_junio= Viaje.objects.filter(fecha_viaje__month=6 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #JUNIO
            viajes_julio= Viaje.objects.filter(fecha_viaje__month=7 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #JULIO
            viajes_agosto= Viaje.objects.filter(fecha_viaje__month=8 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #AGOSTO
            viajes_septiembre= Viaje.objects.filter(fecha_viaje__month=9 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #SEPTIMBRE
            viajes_octubre= Viaje.objects.filter(fecha_viaje__month=10 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #OCTUBRE
            viajes_noviembre= Viaje.objects.filter(fecha_viaje__month=11 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #NOVIEMBRE
            viajes_diciembre= Viaje.objects.filter(fecha_viaje__month=12 , fecha_viaje__year=ano_filtrado ,ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta).values('numero_viaje').annotate(Count('numero_viaje',distinct=True)).count #DICIEMBRE
            


            #calcular el costo de los viajes hechos por dia
            #calcular la cantidad de dias que tiene el mes actual
            
            dias_mes_actual=calendar.monthrange(int(ano_filtrado),int(mes_actual))[1]
            dias=0
            lista_dias=[]
            while dias < dias_mes_actual:
                dias=dias+1
                lista_dias.append(dias)
                
                
            #calcular la cantidad de viajes por dia agrupando los viajes por fecha, pasandole una lista de dias del mes acual al dia de la fecha de viaje
            #pasandole esta lista el query busca 1 po 1 en cada fecha de numero de la lista, que coresponde a 1 dia del mes 
            #esta lista de dias se saca 1 opteniendo el mes actual,2 con la libreria calendar obtenemos el rango de dias del mes actual
            #este rango de dias es almacenado en la variable lista_dias la cual es una lista y por ultimo se le pasa esa lista como filtro de la consula en la variable fecha_viaje
            
            viajes=Viaje.objects.all()
            viajes_diarios=viajes.filter(fecha_viaje__year=ano_filtrado, fecha_viaje__day__in=lista_dias,fecha_viaje__month=mes_actual,  ruta_pasajero__tipo_ruta=dato,campaña_pasajero=cuenta).values('fecha_viaje').annotate(Count('fecha_viaje',distinct=False)) #Lunes
            
         

        else:
            viajes_ruta=Viaje.objects.all()
            precio_ruta=1


        
        context={
        'lista_rutas':lista_rutas,
        'lista_tipo_ruta':lista_tipo_ruta,
        'tipo_ruta_filtrado':tipo_ruta_filtrado,
        'viajes_ruta':viajes_ruta,
        'precio_ruta':precio_ruta,
        'ruta_filtrado':viajes_ruta.nombre_ruta,
        'cuenta_filtrado':cuenta_filtrado.nombre_cuenta,
        'total_viajes':total_viajes,
        'cantidad_viajes':cantidad_viajes,
        'viajes_con_excepcion':viajes_con_excepcion,
        'viajes_sin_excepcion':viajes_sin_excepcion,
        'lista_anos':lista_anos,
        'lista_meses':lista_meses,

        #viajes diarios
        'lista_dias':lista_dias,
        'viajes_diarios':viajes_diarios,

        #lista de cuentas
        'lista_cuentas':lista_cuentas,


        #viajes por mes
        'viajes_enero' : viajes_enero,
        'viajes_febrero' : viajes_febrero,
        'viajes_marzo' : viajes_marzo,
        'viajes_abril' : viajes_abril,
        'viajes_mayo' : viajes_mayo,
        'viajes_junio' : viajes_junio,
        'viajes_julio' : viajes_julio,
        'viajes_agosto' : viajes_agosto,
        'viajes_septiembre' : viajes_septiembre,
        'viajes_octubre' : viajes_octubre,
        'viajes_noviembre' : viajes_noviembre,
        'viajes_diciembre' : viajes_diciembre,


        #pasajeros por dia

        
        
    }

        return render(request, "dashboard/cuentas_overview.html", context)

    except Exception as E:
        messages.success(request,"Seleccione un filtro en la opcion costos del menu" + str(E))
        
        return redirect('home')

   