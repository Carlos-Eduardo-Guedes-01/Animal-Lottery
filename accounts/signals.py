from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Usuario

@receiver(post_save, sender=User)
def create_usuario_profile(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance, saldo=0.0)  # Cria um novo objeto Usuario
        print(f"Usuario profile created for: {instance.username}")  # Debug