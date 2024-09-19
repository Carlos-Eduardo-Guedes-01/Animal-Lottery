from django.db import models
from string import _string
from django.contrib.auth.models import User,AbstractUser
'''class User(AbstractUser):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    saldo=models.FloatField()
    def __str__(self):
        return self.usuario.username'''
class Apostas(models.Model):
    valor1=models.IntegerField()
    valor2=models.IntegerField()
    valor3=models.IntegerField()
    valor4=models.IntegerField()
    valor5=models.IntegerField()
    valor6=models.IntegerField()
    data_aposta=models.DateField()
    valor_aposta=models.FloatField()
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.data_aposta)
class Sorteio(models.Model):
    valor1=models.IntegerField()
    valor2=models.IntegerField()
    valor3=models.IntegerField()
    valor4=models.IntegerField()
    valor5=models.IntegerField()
    valor6=models.IntegerField()
    data_sorteio=models.DateField(null=True)
    aposta=models.ManyToManyField(Apostas, null=True)
    def __str__(self):
        return str(self.data_sorteio)
'''class ganhadores(models.Model):
    sorteio=models.ForeignKey(Sorteio, on_delete=models.CASCADE)
    aposta=models.ForeignKey(Apostas, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sorteio.data_sorteio)
        '''