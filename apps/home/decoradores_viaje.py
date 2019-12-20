from django.contrib import messages
from django.shortcuts import redirect, render


def premiso_transportista(function):
    def wrap(request, *args, **kwargs):
        #si no es un Supe usuario o un Transportista la app manda un mensaje de eeor y lo envia al home
        if  request.user.is_transportista or request.user.is_superuser:
            return function(request, *args, **kwargs)

        else:
            messages.success(request, "No tiene permisos Para acceder a seccion")
            return redirect('home')
    
    return wrap


#este decorador lo hago para usarlo en clases con la el decorador method decorators de django.util.decoratos
def premiso_admin(function):
    def wrap(request, *args, **kwargs):
        #si no es un usuario Admin la app manda un mensaje de eeor y lo envia al home
        if  request.user.is_admin or request.user.is_superuser:
            return function(request, *args, **kwargs)

        else:
            messages.success(request, "No tiene permisos Para acceder a seccion")
            return redirect('home')
    
    return wrap

 