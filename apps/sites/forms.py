from apps.sites.models import Site
from django import forms


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = [
            "id_site",
            "nombre_site",
        ]

        labels = {
            "id_site": "ID Site",
            "nombre_site": "Nombre Site",
        }

        widgets = {
            "id_site": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Id site",
                    "id": "id_site",
                }
            ),
            "nombre_site": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre site",
                    "id": "nombre_site",
                }
            ),
        }
