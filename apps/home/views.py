from django.shortcuts import render, redirect
from django.views import View
from apps.vendor.models import Vendor
from apps.transportista.models import Transportista
from apps.pasajero.models import Pasajero
from apps.viajes.models import Viaje, ViajeAdministrativo
from django.db.models import Count, Sum, Avg, Q

from datetime import datetime
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

        
     
        viajes_enero= Viaje.objects.filter(fecha_viaje__month=1).count
        viajes_febrero= Viaje.objects.filter(fecha_viaje__month=2).count
        viajes_marzo= Viaje.objects.filter(fecha_viaje__month=3).count
        viajes_abril= Viaje.objects.filter(fecha_viaje__month=4).count
        viajes_mayo= Viaje.objects.filter(fecha_viaje__month=5).count
        viajes_junio= Viaje.objects.filter(fecha_viaje__month=6).count
        viajes_julio= Viaje.objects.filter(fecha_viaje__month=7).count
        viajes_agosto= Viaje.objects.filter(fecha_viaje__month=8).count
        viajes_septiembre= Viaje.objects.filter(fecha_viaje__month=9).count
        viajes_octubre= Viaje.objects.filter(fecha_viaje__month=10).count
        viajes_noviembre= Viaje.objects.filter(fecha_viaje__month=11).count
        viajes_diciembre= Viaje.objects.filter(fecha_viaje__month=12).count


        
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
        
        

        
        }
        return render(request, "index.html", context)
