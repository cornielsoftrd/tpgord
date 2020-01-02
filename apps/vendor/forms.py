from django import forms
from apps.vendor.models import Vendor


class VendorForm(forms.ModelForm):
    
    class Meta:
        model = Vendor

        fields =  [

            "id_vendor",
            "nombre_vendor",
            "email_vendor",
            "telefono_vendor",
        ]

        labels = {

            "id_vendor": "Id del Vendor",
            "nombre_vendor" : "Nombre del Vendor",
            "email_vendor" : "Email del Vendor",
            "telefono_vendor" : "Telefono del Vendor",
        }

        widgets={

            "id_vendor" : forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Id del vendor"}
            ),

            "nombre_vendor": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del vendor"}
            ),

            "email_vendor": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email del vendor"}
            ),

            "telefono_vendor": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Telefono del vendor"}
            ),
        }
