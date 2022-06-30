from django import forms
from apps.ruta.models import Ruta,Tipo_ruta


class rutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = [
            "id_ruta",
            "nombre_ruta",
            "tipo_ruta",
            "precio_ruta",
        ]

        labels = {
            "id_ruta": "Id",
            "nombre_ruta": "Nomre",
            "tipo_ruta": "Nomre",
            "precio_ruta": "Nomre",
        }

        widgets = {
            "id_ruta": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "ID"}
            ),
            "nombre_ruta": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre de Ruta"}
            ),
            "tipo_ruta": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Tipo de Ruta"}
            ),
            "precio_ruta": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Precio de Ruta"}
            ),
        }

class TiporutaForm(forms.ModelForm):
    class Meta:
        model = Tipo_ruta
        fields = [
            
            "id",
            "nombre",

        ]

        labels = {
            "id": "Id",
            "nombre_ruta": "Nomre",
            
        }

        widgets = {
            "id": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "ID"}
            ),

            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre de Tipo de Ruta"}
            )
        }
