from django import forms
from apps.pasajero.models import Pasajero, Cuenta


class TimeInput(forms.TimeInput):
    input_type = "time"


class PasajeroForm(forms.ModelForm):
    class Meta:
        model = Pasajero

        fields = [
            "id_pasajero",
            "nombre",
            "apellido",
            "direccion",
            "telefono",
            "Ruta",
            "cuenta",
            "site",
            "hora_entrada",
            "hora_salida",
        ]

        labels = {
            "id_pasajero": "Id pasajero",
            "nombre": "Nombre",
            "apellido": "Apellido",
            "direccion": "Direccion",
            "telefono": "Telefono",
            "Ruta": "Ruta",
            "cuenta": "Cuenta",
            "site": "Site",
            "hora_entrada": "Hora Entrada",
            "hora_salida": "Hora Salida",
        }

        widgets = {
            "id_pasajero": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "ID (CCMS)"}
            ),
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre"}
            ),
            "apellido": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Apellido"}
            ),
            "direccion": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Direcciones"}
            ),
            "telefono": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Telefono"}
            ),
            "Ruta": forms.Select(attrs={"class": "form-control"}),
            "cuenta": forms.Select(attrs={"class": "form-control"}),
            "site": forms.Select(attrs={"class": "form-control"}),
            "hora_entrada": TimeInput(attrs={"class": "form-control"}),
            "hora_salida": TimeInput(attrs={"class": "form-control"}),
        }


class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta

        fields = [
            "id_cuenta",
            "nombre_cuenta",
        ]

        labels = {
            "id_cuenta": "Id",
            "nombre_cuenta": "Nombre",
        }

        widgets = {
            "id_cuenta": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "ID"}
            ),
            "nombre_cuenta": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre"}
            ),
        }
