import sys
sys.path.append("accounts/")
from accounts.models import Usuario
import asyncio
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect
#from .forms import ApostaForm
from django.utils.datastructures import MultiValueDictKeyError
from random import randint
from itertools import chain
from .models import Apostas,Sorteio
from datetime import date,time
from django.contrib import messages #import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='accounts:/dologing/')
def form_jogo(request,valor):
    usuario=request.user
    user_model=User.objects.get(username=usuario)
    id_usuario=user_model.id
    hj=date.today()
    lista_numeros=[]
    for i in range(1,61):
        lista_numeros.insert(i, i)
    context={
        'hj':hj,
        'user':id_usuario,
        'lista_numeros':lista_numeros,
        'valor':valor
    }
    msg=''
    return render(request,'loteria/aposta3.html',context)
def cadastra_aposta(request):
    data={}
    if request.method=='POST':
        form=request.POST
        print('Lista: ',form)
        lista=[]
        for i in form:
            lista.append(i)
        hj=date.today()
        usu=request.POST.get('usuario',None)
        valor=request.POST.get('moeda',None)
        user_model=User.objects.get(id=usu)
        saldo=request.POST.get('saldo')
        mode_user=User.objects.get(id=usu)
        jogador=Usuario.objects.get(usuario=mode_user.id)
        upd=Usuario.objects.filter(usuario=mode_user.id).update(saldo=jogador.saldo-float(valor))
        jogador=Usuario.objects.get(usuario=mode_user.id)
        #get_usuario=Usuario.objects.get(usuario=usu)
        #get_usuario2=Usuario.objects.get(usuario=usu.update(saldo=get_usuario.saldo-valor))
        if(valor<=saldo):
            aposta=Apostas.objects.create(valor1=lista[1],valor2=lista[2],valor3=lista[3],valor4=lista[4],valor5=lista[5],valor6=lista[6],data_aposta=hj,valor_aposta=valor,usuario=user_model)
            #aposta = form.save(commit=False)
            #form.save()
            if(aposta is not None):
                data['msg'] = 'Aposta Realizada com sucesso!'
                data['class'] = 'alert-success'
                data['valor']=jogador.saldo
            #return redirect('listar_sorteio')
            else:
                data['msg'] = 'Aposta Realizada com sucesso!'
                data['class'] = 'alert-danger'
        elif(valor>saldo):
            data['msg'] = 'Saldo Insuficiente!'
            data['class'] = 'alert-danger'
            data['valor']=saldo
        else:
            data['msg'] = 'Erro desconhecido!'
            data['class'] = 'alert-danger'
    return render(request, '../../accounts/templates/dashboard/home.html',data)
def sorteia_numero(request):
    #hora=time('%H','%m')
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
def procura_ganhador2(request):
    var={}
    sort=Sorteio.objects.all().filter(data_sorteio=date.today())
    query_sort1=None
    for l in sort:
        query_sort1=[l]
        print(l)
    aposta2=Apostas.objects.all().filter(data_aposta=date.today())
    ganhadores=None
    quant=0
    clientes=''
    quant=0
    cli=None
    for lista3 in aposta2:
        lista_apostas=[lista3.valor1,lista3.valor2,lista3.valor3,lista3.valor4,lista3.valor5,lista3.valor6]
        print(lista3.usuario.first_name)
        for lista2 in query_sort1:
            print(lista3)
            print(lista2)
            lista_sorteio=[lista2.valor1,lista2.valor2,lista2.valor3,lista2.valor4,lista2.valor5,lista2.valor6]
            for l4 in lista_apostas:
                if(l4 in lista_sorteio):
                    if(str(l4) not in str(lista_sorteio)):
                        pass
                    else:
                        quant+=1
            print(quant)
            if(quant>6):
                email=[lista3.usuario.email]
                cli=[lista3.usuario]
                id_use=lista3.usuario
                v=Usuario.objects.get(usuario=id_use)
                var['valor']=v.saldo
                print(lista2.id)
                a = Sorteio.objects.get(id=lista2.id).aposta.add(lista3.id)

    if(cli is None):
        print('Não encontrou ganhador')
        messages.warning(request,'Não houveram ganhadores!')
    elif(cli!=None):
        subject = 'Animal Lottery'
        message = "Olá você ganhou o sorteio da Loteria"
        email_from = settings.EMAIL_HOST_USER
        for em in email:
            recipient_list = [str(em) ,]
            print(em)
            send_mail(subject, message, email_from, recipient_list )
        context={
            'msg' :'Seu email foi enviado com sucesso.',
        }
        var
        print(cli)
        messages.success(request, 'E-mail enviado!')
        return render(request, 'loteria/aposta3.html',var)
    return render(request, 'loteria/sem_ganhadores.html',var)
def sacar(request):
    pass
