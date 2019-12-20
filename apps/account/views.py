from django.shortcuts import render
from django.shortcuts import render, redirect
from apps.account.forms import AccountAuthenticationForm
from django.contrib.auth import login, authenticate, logout

from apps.account.forms import registro_usuario_form


# al momento de loguearse se crean variables de sesion:


def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:

        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = AccountAuthenticationForm()
        context["login_form"] = form
    return render(request, "registration/login.html", context)


def registrar_usuario(request):
    if request.method == 'POST':
        form = registro_usuario_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
       
    else:
        form = registro_usuario_form()
    return render(request, 'registration/registro_susuarios.html',{'form':form})