from django import forms
from apps.ruta.models import Ruta


class rutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = [
            "id_ruta",
            "nombre_ruta",
        ]

        labels = {
            "id_ruta": "Id",
            "nombre_ruta": "Nomre",
        }

        widgets = {
            "id_ruta": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "ID"}
            ),
            "nombre_ruta": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre de Ruta"}
            ),
        }
