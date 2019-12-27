from django.shortcuts import render, redirect
from django.views import View
from apps.vendor.models import Vendor
from apps.transportista.models import Transportista
from apps.pasajero.models import Pasajero
from apps.viajes.models import Viaje, ViajeAdministrativo
from django.db.models import Count, Sum, Avg, Q

from datetime import datetime

from django.views.defaults import page_not_found
# Create your views here.


class home_View(View):
    def get(self, request, *args, **kwargs):
        cantidad_vendors = Vendor.objects.all().count
        cantidad_transportistas =Transportista.objects.all().count
        cantidad_pasajeros =Pasajero.objects.all().count
        cantidad_viajes_admin =ViajeAdministrativo.objects.all().count
        #esta linea cuenta los viajes realizados donde el numero de viaje es distinto asi, se toma el numero de viaje exacto y no los cuenta por pasajeros agregados en el viaje
        cantidad_viajes =Viaje.objects.values('numero_viaje').annotate(Count('numero_viaje',disctint=True)).count 
        viajes_con_excepcion =Viaje.objects.filter(excepcion=True).count
        viajes_sin_excepcion =Viaje.objects.filter(excepcion=False).count

        
        #extraer viajes normales por mes para pasar al grafico de barras

        
        #aqui se cuentan los viajes por mes, contando los numeros de viajes distintos,asi un numero de viaje se contara una sola vez 
        viajes_enero= Viaje.objects.filter(fecha_viaje__month=1).values('numero_viaje').annotate(Count('numero_viaje',disctict=True)).count #enero
        viajes_febrero= Viaje.objects.filter(fecha_viaje__month=2).values('numero_viaje').annotate(Count('numero_viaje',disctict=True)).count  # FEBRERO
        viajes_marzo= Viaje.objects.filter(fecha_viaje__month=3).values('numero_viaje').annotate(Count('numero_viaje',disctict=True)).count #MARZO
        viajes_abril= Viaje.objects.filter(fecha_viaje__month=4).values('numero_viaje').annotate(Count('numero_viaje',disctict=True)).count #ABRIL
        viajes_mayo= Viaje.objects.filter(fecha_viaje__month=5).values('numero_viaje').annotate(Count('numero_viaje',disctict=True)).count #MAYO
        viajes_junio= Viaje.objects.filter(fecha_viaje__month=6).values('numero_viaje').annotate(Count('numero_viaje',disctict=True)).count #JUNIO
        viajes_julio= Viaje.objects.filter(fecha_viaje__month=7).values('numero_viaje').annotate(Count('numero_viaje',disctict=True)).count #JULIO
        viajes_agosto= Viaje.objects.filter(fecha_viaje__month=8).values('numero_viaje').annotate(Count('numero_viaje',disctict=True)).count #AGOSTO
        viajes_septiembre= Viaje.objects.filter(fecha_viaje__month=9).values('numero_viaje').annotate(Count('numero_viaje',disctict=True)).count #SEPTIMBRE
        viajes_octubre= Viaje.objects.filter(fecha_viaje__month=10).values('numero_viaje').annotate(Count('numero_viaje',disctict=True)).count #OCTUBRE
        viajes_noviembre= Viaje.objects.filter(fecha_viaje__month=11).values('numero_viaje').annotate(Count('numero_viaje',disctict=True)).count #NOVIEMBRE
        viajes_diciembre= Viaje.objects.filter(fecha_viaje__month=12).values('numero_viaje').annotate(Count('numero_viaje',disctict=True)).count #DICIEMBRE


    #aqui se contaran los agentes llevados cada mes, contanto todas las vilas de viajes de ese mes, 
        pasajeros_viajes_enero= Viaje.objects.filter(fecha_viaje__month=1).count
        pasajeros_viajes_febrero= Viaje.objects.filter(fecha_viaje__month=2).count
        pasajeros_viajes_marzo= Viaje.objects.filter(fecha_viaje__month=3).count
        pasajeros_viajes_abril= Viaje.objects.filter(fecha_viaje__month=4).count
        pasajeros_viajes_mayo= Viaje.objects.filter(fecha_viaje__month=5).count
        pasajeros_viajes_junio= Viaje.objects.filter(fecha_viaje__month=6).count
        pasajeros_viajes_julio= Viaje.objects.filter(fecha_viaje__month=7).count
        pasajeros_viajes_agosto= Viaje.objects.filter(fecha_viaje__month=8).count
        pasajeros_viajes_septiembre= Viaje.objects.filter(fecha_viaje__month=9).count
        pasajeros_viajes_octubre= Viaje.objects.filter(fecha_viaje__month=10).count
        pasajeros_viajes_noviembre= Viaje.objects.filter(fecha_viaje__month=11).count
        pasajeros_viajes_diciembre= Viaje.objects.filter(fecha_viaje__month=12).count


        
        #viajes_mes=Viaje.objects.filter(date_created__)

        context={

        'cantidad_vendors':cantidad_vendors,
        'cantidad_transportistas':cantidad_transportistas,
        'cantidad_pasajeros':cantidad_pasajeros,
        'cantidad_viajes_admin':cantidad_viajes_admin,
        'cantidad_viajes':cantidad_viajes,
        'viajes_con_excepcion':viajes_con_excepcion,
        'viajes_sin_excepcion':viajes_sin_excepcion,


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
        
        

        
        }
        return render(request, "index.html", context)
