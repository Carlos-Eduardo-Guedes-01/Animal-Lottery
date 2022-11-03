from django.contrib.auth.models import User
from django.db import models
#from django.contrib.admin.sites import User
class Usuario(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    saldo=models.FloatField()
    def __str__(self):
        return self.usuario.username