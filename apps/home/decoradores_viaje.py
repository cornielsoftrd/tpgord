from django.contrib import messages
from django.shortcuts import redirect, render


def permiso_transportista(function):
    def wrap(request, *args, **kwargs):
        #si no es un Supe usuario o un Transportista la app manda un mensaje de eeor y lo envia al home
        if  request.user.is_transportista or request.user.is_superuser:
            return function(request, *args, **kwargs)

        else:
            messages.success(request, "No tiene permisos Para acceder a seccion")
            return redirect('home')
    
    return wrap


#este decorador lo hago para usarlo en clases con la el decorador method decorators de django.util.decoratos
def permiso_staff(function):
    def wrap(request, *args, **kwargs):
        #si no es un usuario Admin la app manda un mensaje de eeor y lo envia al home
        if  request.user.is_staff or request.user.is_superuser:
            return function(request, *args, **kwargs)

        else:
            messages.success(request, "No tiene permisos Para acceder a seccion")
            return redirect('home')
    
    return wrap

 #este decorador lo hago para usarlo en clases con la el decorador method decorators de django.util.decoratos
def permiso_vendor(function):
    def wrap(request, *args, **kwargs):
        #si no es un usuario Admin la app manda un mensaje de eeor y lo envia al home
        if  request.user.is_vendor or request.user.is_superuser:
            return function(request, *args, **kwargs)

        else:
            messages.success(request, "No tiene permisos Para acceder a seccion")
            return redirect('home')
    
    return wrap