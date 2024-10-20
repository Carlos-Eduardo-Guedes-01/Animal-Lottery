from django.contrib.auth.models import User
import sys
sys.path.append("accounts/")
from accounts.models import Usuario
from django.db import models
class aposta(models.Model):
    apostador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    animal1_aposta = models.CharField(max_length=2)
    animal2_aposta = models.CharField(max_length=2)
    data_aposta = models.DateField()
    valor_aposta = models.FloatField()

class bichos(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=2)
    def __str__(self):
        return self.nome

class sorteio(models.Model):
    data_sorteio = models.DateField()
    animail1 = models.CharField(max_length=100)
    animail2 = models.CharField(max_length=100)
    aposta=models.ManyToManyField(aposta, null=True)