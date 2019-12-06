from django import forms
from apps.vendor.models import Vendor


class VendorForm(forms.ModelForm):
    
    class Meta:
        model = Vendor

        fields =  [

            "id_vendor",
            "nombre_vendor",
        ]

        labels = {

            "id_vendor": "Id del Vendor",
            "nombre_vendor" : "Nombre del Vendor",
        }

        widgets={

            "id_vendor" : forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Id del vendor"}
            ),

            "nombre_vendor": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del vendor"}
            ),
        }
