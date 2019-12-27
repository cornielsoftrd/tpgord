from django import forms
from apps.manejadoqr.models import crear_qr


class qrForm(forms.ModelForm):
    class Meta:
        model = crear_qr

        fields = [
            "nombre",
        ]

        labels = {
            "nombre": "Nombre",
        }

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
        }
