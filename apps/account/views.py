from django.shortcuts import render
from django.shortcuts import render, redirect
from apps.account.forms import AccountAuthenticationForm
from django.contrib.auth import login, authenticate, logout


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
