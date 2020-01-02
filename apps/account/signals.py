from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.vendor.models import Vendor
from apps.transportista.models import Transportista
from apps.account.models import Account

#aqui estan los Signals del modelo Account, para crear usuarios y demas
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
post_save.connect(crear_usuario_transportista, sender=Vendor)
