from django import forms
from apps.lectorQR.models import LectorQr


class lectorForm(forms.ModelForm):
    class Meta:
        model = LectorQr

        fields = [
            "datos_codigo",
        ]

        labels = {"datos_codigo": "Codigo"}

        widgets = {
            "datos_codigo": forms.TextInput(attrs={"class": "form-control"}),
        }
