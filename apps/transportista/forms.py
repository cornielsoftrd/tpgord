from django import forms
from apps.transportista.models import Transportista


class TransportistaForm(forms.ModelForm):
    class Meta:
        model = Transportista
        fields = [
            "codigo_transportista",
            "nombre",
            "apellido",
            "ruta",
            "vendor",
        ]

        labels = {
            "codigo_transportista": "codigo del Trasnportista",
            "nombre": "Nombre",
            "apellido": "Apellido",
            "ruta": "Ruta",
            "vendor": "Vendor",
        }

        widgets = {
            "codigo_transportista": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Id Transportista"}
            ),
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre"}
            ),
            "apellido": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Apellido"}
            ),
            "ruta": forms.CheckboxSelectMultiple(),

            "vendor": forms.Select(
                attrs={"class": "form-control", "placeholder": "Nombre del vendor"}
            ),
        }
