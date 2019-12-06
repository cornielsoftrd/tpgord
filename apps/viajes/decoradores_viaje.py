from django.contrib import messages
from django.shortcuts import redirect, render
def premiso_transportista(function):
    def wrap(request):
        #si no es un Supe usuario o un Transportista la app manda un mensaje de eeor y lo envia al home
        if not request.user.is_transportista and not request.user.is_superuser:
            messages.success(request, "No tiene permisos Para Acceder a seccion")
            return redirect("home")

            return function(request)
    
    return wrap;



	