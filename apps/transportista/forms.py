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
            "telefono",
            "email",
            "vendor",
        ]

        labels = {
            "codigo_transportista": "codigo del Trasnportista",
            "nombre": "Nombre",
            "apellido": "Apellido",
            "telefono": "Telefono",
            "email": "Email",
            "ruta": "ruta",
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
            "telefono": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "telefono"}
            ),
            "email": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "email"}
            ),
            "ruta": forms.CheckboxSelectMultiple(),

            "vendor": forms.Select(
                attrs={"class": "form-control", "placeholder": "Nombre del vendor"}
            ),
        }
