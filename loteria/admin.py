from django.contrib import admin
from .models import Apostas,Sorteio
from django.contrib.auth.models import User
admin.site.register(Sorteio)
admin.site.register(Apostas)
