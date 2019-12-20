from django import forms
from django.contrib.auth import authenticate
from apps.account.models import Account
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("username", "password")

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data["username"]
            password = self.cleaned_data["password"]
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login")


class registro_usuario_form(UserCreationForm):
    email = forms.EmailField(max_length=60)

    class Meta:
        model =Account
        fields = [
        "email", 
        "username",
        "first_name",
        "last_name",
        "phone",
        "password1",
        "password2",

         ]

        widgets={

        "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
        "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre de Usuario"}),
        "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Apellido"}),
        "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Telefono"}),
        "password1": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Contraseña"}),
        "password2": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Repetor Contraseña"}),

        }
        
