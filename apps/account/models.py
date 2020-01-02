from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.vendor.models import Vendor
from apps.transportista.models import Transportista

# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone, password=None):
        if not email:
            raise ValueError("Debe indicar un Email para el usuario")
        if not username:
            raise ValueError("Debe indicar un nombre de usuario para el usuario")
        if not first_name:
            raise ValueError("Debe indicar un Nombre para el usuario")
        if not last_name:
            raise ValueError("Debe indicar un apellido para el usuario")
        if not phone:
            raise ValueError("Debe indicar un Numero de Telefono para el usuario")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            last_name=last_name,
            first_name=first_name,
            phone=phone,
        )
        
        user.is_vendor = False
        user.is_staff = False
        user.is_transportista = False

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, username, phone, password):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            username=username,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_transportista = models.BooleanField(default=False)
    is_soporte = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name", "phone"]

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    # todos los admin tienen permiso para todo
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # este usuario tiene permiso para ver esa app, si siempre
    def has_module_perms(self, app_label):
        return True

#aqui estan los Signals para crear usuarios especificos al guardar otros modelos

#al guardarse un Vendor se crea un usuario tipo Vendor , la contrase es el telefono, el usuario es el id tel Vendor
@receiver(post_save, sender=Vendor)
def crear_usuario_vendor(sender, instance, **kwargs):
    if kwargs['created']:
        usuario_vendor = Account.objects.create_user(
            email=instance.email_vendor,
            username=instance.id_vendor,
            first_name=instance.nombre_vendor,
            last_name=instance.nombre_vendor,
            phone=instance.telefono_vendor,
            password=instance.telefono_vendor,
            
        )
        usuario_vendor.is_vendor=True
        usuario_vendor.save()
       
post_save.connect(crear_usuario_vendor, sender=Vendor)


#al guardarse un transportista se crea un usuario tipo transportista , la contrase es el telefono, el usuario es el id tel transportista
@receiver(post_save, sender=Transportista)
def crear_usuario_transportista(sender, instance, **kwargs):
    if kwargs['created']:
        usuario_transportista = Account.objects.create_user(
            email=instance.email,
            username=instance.codigo_transportista,
            first_name=instance.nombre,
            last_name=instance.apellido,
            phone=instance.telefono,
            password=instance.telefono,
        )
        usuario_transportista.is_transportista=True
        usuario_transportista.save()    
post_save.connect(crear_usuario_transportista, sender=Transportista)

