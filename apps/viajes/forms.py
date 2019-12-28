from django import forms
from apps.viajes.models import Viaje,  ViajeAdministrativo


class TimeInput(forms.TimeInput):
    input_type = "time"


class viaje_form(forms.ModelForm):
    class Meta:
        model = Viaje
        # el numero de viaje y la Hora del viaje no estan en este formulario, debido a que estos seran incluidos de manera automatica atravez de variiables del sistema
        fields = [
            "id_viaje",
            "transportista",
            'site_destino_origen',
            "fecha_viaje",
            "hora_viaje",
            "tipo_viaje",
            "hora_entrada",
            "hora_salida",
            "id_pasajero",
            "nombre_pasajero",
            "apellido_pasajero",
            "campaña_pasajero",
            "site_pasajero",
            "ruta_pasajero",
            "direccion_pasajero",
            "excepcion",
            "razon_excepcion",
            #'cantidad_pasajeros',
            #'precio_viaje',
        ]

        labels = {
            "id_viaje": "Id viaje",
            "transportista": "Transportista",
            "site_destino_origen": "site_destino_origen",
            "fecha_viaje": "Fecha de Viaje",
            "hora_viaje": "Hora de viaje",
            "tipo_viaje": "tipo de Viaje",
            "hora_entrada": "Horario de Entrada",
            "hora_salida": "Horario de Salida",
            "id_pasajero": "Id de pasajero",
            "nombre_pasajero": "Nombre de Pasajero",
            "apellido_pasajero": "Apellido de Pasajero",
            "campaña_pasajero": "Campaña de Pasajero",
            "site_pasajero": "site de Pasajero",
            "ruta_pasajero": "Ruta de Pasajero",
            "direccion_pasajero": "Direccion de Pasajero",
            "excepcion": "Excepcion",
            "razon_excepcion": "Razon de Excepcion",
            #'cantidad_pasajeros' : 'Cantidad de Pasajeros',
            #'precio_viaje' :      'Precio de Viaje',
        }

        widgets = {
            "id_viaje": forms.HiddenInput(attrs={"class": "form-control"}),
            "transportista": forms.TextInput(attrs={"class": "form-control"}),
            "site_destino_origen": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_viaje": forms.TextInput(attrs={"class": "form-control"}),
            "hora_viaje": forms.TimeInput(attrs={"class": "form-control"}),
            "tipo_viaje": forms.TextInput(attrs={"class": "form-control"}),
            "hora_entrada,": forms.TimeInput(attrs={"class": "form-control"}),
            "hora_salida": forms.TimeInput(attrs={"class": "form-control"}),
            "id_pasajero": forms.TextInput(attrs={"class": "form-control"}),
            "nombre_pasajero": forms.TextInput(attrs={"class": "form-control"}),
            "apellido_pasajero": forms.TextInput(attrs={"class": "form-control"}),
            "campaña_pasajero": forms.TextInput(attrs={"class": "form-control"}),
            "site_pasajero": forms.TextInput(attrs={"class": "form-control"}),
            "ruta_pasajero": forms.TextInput(attrs={"class": "form-control"}),
            "direccion_pasajero": forms.TextInput(attrs={"class": "form-control"}),
            "excepcion": forms.Select(attrs={"class": "form-control"}),
            "razon_excepcion": forms.Textarea(attrs={"class": "form-control"}),
            #'cantidad_pasajeros': forms.TextInput(),
            #'precio_viaje': forms.TextInput(),
        }

class viaje_admin_form(forms.ModelForm):
    
    class Meta:
        model = ViajeAdministrativo
        fields = [
            
            "numero_viaje",
            "usuario",
            "vendor",
            "fecha_viaje",
            "hora_viaje",
            "origen",
            "destino",
            "tipo_vehiculo",
            "tipo_visita",
            "numero_contacto",
            "observaciones",
                    
        
        ]

        labels = {
            "numero_viaje" : "Numero de viaje",
            "usuario" : "Usuario",
            "vendor" : "Transportista",
            "fecha_viaje" : "Fecha de viaje",
            "hora_viaje" : "Hora del viaje",
            "origen" : "Origen",
            "destino" : "Destino",
            "tipo_vehiculo" : "Tipo de vehiculo",
            "tipo_visita" : "Tipo de visita",
            "numero_contacto" : "Numero de contacto",
            "observaciones" : "Observaciones",
        }


        widgets = {

            "numero_viaje" : forms.TextInput(attrs={"class": "form-control" , "placeholder" :"Numero de viaje"}),
            "usuario" : forms.TextInput(attrs={"class": "form-control" , "placeholder":"Usuario"}),
            "vendor" : forms.Select(attrs={"class": "form-control" , "placeholder":"Transportista"}),
            "fecha_viaje" : forms.DateInput(attrs={"class": "form-control" , "placeholder":"Fecha de viaje"}),
            "hora_viaje" : forms.TimeInput(attrs={"class": "form-control" , "placeholder":"Hora del viaje"}),
            "origen" : forms.TextInput(attrs={"class": "form-control" , "placeholder":"Origen"}),
            "destino" : forms.TextInput(attrs={"class": "form-control" , "placeholder":"Destino"}),
            "tipo_vehiculo" : forms.TextInput(attrs={"class": "form-control" , "placeholder":"Tipo de vehiculo"}),
            "tipo_visita" : forms.TextInput(attrs={"class": "form-control" , "placeholder":"Tipo de visita"}),
            "numero_contacto" : forms.TextInput(attrs={"class": "form-control" , "placeholder":"Numero de contacto"}),
            "observaciones" : forms.Textarea(attrs={"class": "form-control" , "placeholder":"Observaciones"}),
        }