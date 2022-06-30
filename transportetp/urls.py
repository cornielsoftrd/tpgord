"""transportetp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetForm,
    PasswordChangeDoneView,
    PasswordChangeView,
)
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static


from apps.home.views import (
    home_View,
    costos,
    cuentas_overview,

    
    
    )

from apps.pasajero.views import (
    crear_pasajero,
    listar_pasajeros,
    editar_pasajero,
    borrar_pasajeros,
    crear_cuenta,
    listar_cuentas,
    editar_cuenta,
    borrar_cuenta,
)

from apps.vendor.views import (
    crear_vendor, 
    listar_vendor, 
    editar_vendor, 
    borrar_vendor,
    
    
    )

from apps.transportista.views import (
    crear_transportista,
    listar_transportistas,
    editar_transportista,
    borrar_transportista,
)
from apps.ruta.views import ( 
    crear_ruta, 
    listar_rutas, 
    editar_ruta, 
    borrar_ruta,

    crear_tipo_ruta, 
    listar_tipo_rutas, 
    editar_tipo_ruta, 
    borrar_tipo_ruta,
    
    )

from apps.sites.views import (
    crear_site, 
    listar_sites, 
    editar_site, 
    borrar_site,
    
    )


from apps.manejadoqr.views import (
    creneradorqr,
    
    )

from apps.lectorQR.views import (
    leer_qr,
    
    )

from apps.viajes.views import (
    generar_viaje,
    agregar_viaje,
    finalizar_viaje,
    crear_viaje,
    crear_viaje_admin,
    generar_viaje_admin,
    listar_viajes_admin,
    agregar_viaje_manual,
    agregar_viaje_casual,
    listar_viaje_en_curso,
    excluir_pasajero,
    borrar_viaje,
    mis_viajes,
    solicitudes,
    cambiar_estatus_viaje,
    crear_excepcion,
    listar_excepciones,
    editar_excepcion,
    borrar_excepcion,



 

    
)

from apps.reportes.views import (
    reporte_viaje_excel, 
    reporte_tr,
    detalle_viaje,
)

from apps.account.views import login_view, registrar_usuario


urlpatterns = [
    path("admin/", admin.site.urls),
    path("registrartr/", registrar_usuario, name="registrartr"),
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # manejo de contraseñas
    path("accounts/", include("django.contrib.auth.urls")),  

    path('password_change/done/', login_required(PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html')), 
        name='password_change_done'),

    path('password_change/',login_required(PasswordChangeView.as_view(template_name='registration/password_change.html')), 
        name='password_change'),

    # new
    # --------------
    # vistas de la App Home
    path("home", login_required(home_View.as_view()), name="home"),
    path("", login_required(home_View.as_view()), name="home"),
    path("costos", costos, name="costos"),
    path("cuentas_overview", cuentas_overview, name="cuentas_overview"),

    # Vistas de App Vendor
    path("crear_vendor/", login_required(crear_vendor.as_view()), name="crear_vendor"),
    path("vendor", login_required(listar_vendor), name="vendor"),
    path("editar_vendor/<pk>", login_required(editar_vendor.as_view()), name="editar_vendor"),
    path("borrar_vendor/<pk>", login_required(borrar_vendor.as_view()), name="borrar_vendor"),

    # Vistas de App Transportista
    path(
        "crear_transportista/",
        login_required(crear_transportista.as_view()),
        name="crear_transportista",
    ),
    path(
        "transportistas/", login_required(listar_transportistas), name="transportistas"
    ),
    path(
        "editar_transportista/<pk>",
        login_required(editar_transportista.as_view()),
        name="editar_transportista",
    ),
    path(
        "borrar_transportista/<pk>",
        login_required(borrar_transportista.as_view()),
        name="borrar_transportista",
    ),
    path("crear_ruta/", login_required(crear_ruta.as_view()), name="crear_ruta"),
    path("rutas/", login_required(listar_rutas), name="rutas"),
    path("editar_ruta/<pk>", login_required(editar_ruta.as_view()), name="editar_ruta"),
    path("borrar_ruta/<pk>", login_required(borrar_ruta.as_view()), name="borrar_ruta"),

    #tipo de ruta
    path("crear_tipo_ruta/", login_required(crear_tipo_ruta.as_view()), name="crear_tipo_ruta"),
    path("tipo_ruta/", login_required(listar_tipo_rutas), name="tipo_ruta"),
    path("editar_tipo_ruta/<pk>", login_required(editar_tipo_ruta.as_view()), name="editar_tipo_ruta"),
    path("borrar_tipo_ruta/<pk>", login_required(borrar_tipo_ruta.as_view()), name="borrar_tipo_ruta"),
    # Vistas de App Cuenta
    path("crear_cuenta/", login_required(crear_cuenta.as_view()), name="crear_cuenta"),
    path("cuentas/", login_required(listar_cuentas), name="cuentas"),
    path(
        "editar_cuenta/<pk>",
        login_required(editar_cuenta.as_view()),
        name="editar_cuenta",
    ),
    path(
        "borrar_cuenta/<pk>",
        login_required(borrar_cuenta.as_view()),
        name="borrar_cuenta",
    ),
    # Vistas de App Pasajeros
    path(
        "crear_pasajero/",
        login_required(crear_pasajero.as_view()),
        name="crear_pasajero",
    ),
    path("pasajeros", login_required(listar_pasajeros), name="pasajeros"),
    path(
        "editar_pasajero/<pk>",
        login_required(editar_pasajero.as_view()),
        name="editar_pasajero",
    ),
    path(
        "borrar_pasajeros/<pk>",
        login_required(borrar_pasajeros.as_view()),
        name="borrar_pasajeros",
    ),
    path("crear_qr", login_required(creneradorqr.as_view()), name="creneradorqr"),
    path("leer_qr", login_required(leer_qr), name="leer_qr"),
    # Vistas de App Site
    path("crear_site/", login_required(crear_site.as_view()), name="crear_site"),
    path("sites", login_required(listar_sites), name="sites"),
    path("editar_site/<pk>", login_required(editar_site.as_view()), name="editar_site"),
    path("site/<pk>", login_required(borrar_site.as_view()), name="borrar_site"),


    # Vistas de App Exepciones
    path("crear_excepcion/", login_required(crear_excepcion), name="crear_excepcion"),
    path("excepciones", login_required(listar_excepciones), name="excepciones"),
    path("editar_excepcion/<pk>", login_required(editar_excepcion), name="editar_excepcion"),
    path("borrar_excepcion/<pk>", login_required(borrar_excepcion), name="borrar_excepcion"),
  


    # Vistas para Viajes Normales
    path("crear_viaje", login_required(crear_viaje.as_view()), name="crear_viaje"),
    path("generar_viaje", login_required(generar_viaje), name="generar_viaje"),
    path("finalizar_viaje", login_required(finalizar_viaje), name="finalizar_viaje"),
    path("viaje_en_curso", login_required(listar_viaje_en_curso), name="viaje_en_curso"),
    path("excluir_pasajero/<pk>", login_required(excluir_pasajero.as_view()), name="excluir_pasajero"),
    path("borrar_viaje/<numero_viaje>", login_required(borrar_viaje), name="borrar_viaje"),
    path("mis_viajes", login_required(mis_viajes), name="mis_viajes"),
    path("reportexls", reporte_viaje_excel.as_view(), name="reportexls"),
    


        #Vistas Viajes Administrativos
    path("generar_viaje_admin", login_required(generar_viaje_admin), name="generar_viaje_admin"),
    path("crear_viaje_admin", login_required(crear_viaje_admin.as_view()), name="crear_viaje_admin"),
    path("viajes_admin", login_required(listar_viajes_admin), name="viajes_admin"),
    path("solicitudes", login_required(solicitudes), name="solicitudes"),
    path("estado_viaje/<pk>", login_required(cambiar_estatus_viaje.as_view()), name="estado_viaje"),


    # esta vista es accesada desde el base.html cuando la camara escanea el QR pasado como parametro el codigo del QR con el cual se genera toda la informacion en la aplicacion Viaje
    path(
        "agregar_viaje/<int:id_escaneado>",
        login_required(agregar_viaje.as_view()),
        name="agregar_viaje",
    ),
    
    path(
        "agregar_viaje_manual/<id_ingresado>",
        login_required(agregar_viaje_manual.as_view()),
        name="agregar_viaje_manual",
    ),

    path(
        "agregar_viaje_casual",
        login_required(agregar_viaje_casual.as_view()),
        name="agregar_viaje_casual",
    ),

    path('reporte_tr', reporte_tr, name='reporte_tr'),
    path("detalle_viaje/<numero_viaje>", login_required(detalle_viaje), name="detalle_viaje"),


    path('settings/', include('django_mfa.urls'), name="mfa"),

    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
