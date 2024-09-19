from datetime import date
from random import randint
from celery import shared_task
from django.shortcuts import render
from django.utils import timezone

from loteria.models import Sorteio

@shared_task
def cadastra_aposta_task(request):
    v1=[]
    c=0
    while(c<6):
        v=randint(1, 60)
        if(v not in v1):
            v1.append(v)
        else:
            c-=1
        c+=1
    v1.append(date.today())
    Sorteio.objects.create(valor1=v1[0], valor2=v1[1], valor3=v1[2], valor4=v1[3],valor5=v1[4], valor6=v1[5], data_sorteio=v1[6])
    context={
        'valores':v1
    }
    return render(request, 'loteria/listar_sorteio.html',context)
