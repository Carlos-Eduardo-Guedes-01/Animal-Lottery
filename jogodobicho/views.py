from django.shortcuts import render
import sys
sys.path.append("accounts/")
from accounts.models import Usuario
from django.conf import settings
from django.core.mail import send_mail
#jogo do bicho
from django.contrib import messages #import messages
import email
from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from random import randint
from datetime import date

from jogodobicho.models import Usuario, aposta,sorteio
def jogodobicho(request,valor):
    context={
        'valor':valor
    }
    return render(request,'dashboard/bicho.html',context)
#CADASTRO DE APOSTAS
def jogodobicho2(request):
    data = {}
    #print(request.user)
    usu = User.objects.get(username=request.user)
    #print('ID USER',usu.id)
    apostador=Usuario.objects.get(usuario=usu.id)
    form=request.POST
    identidade=apostador.id
    lista=[]
    hj=date.today()
    print('apostador: ',apostador.id)
    valor=request.POST.get('moeda')
    upd=Usuario.objects.filter(usuario=usu.id).update(saldo=apostador.saldo-float(valor))
    jogador=Usuario.objects.get(usuario=usu.id)
    #print(valor)
    for i in form:
        lista.append(i)
    animal1_aposta0 = aposta.objects.create(animal1_aposta=lista[1],animal2_aposta=lista[2],data_aposta=hj,valor_aposta=valor,apostador=apostador)
    return render(request, '../../jogodobicho/templates/dashboard/bicho.html',{'valor':jogador.saldo})
def sorteio_(request):
    data={}
    from random import randint
    for i in range(0,5):
        c=0
        lista=[]
        while(c<4):
            valor=str(randint(0, 9))
            if(valor not in lista):
                lista.append(str(valor))
            else:
                c-=1
            c+=1
        lista_invert=(lista[3],lista[2],lista[1],lista[0])
        print(lista_invert)
        #print(lista_invert[0],lista_invert[1],lista_invert[2],lista_invert[3])
        lista_invert1=[]
        lista_invert1=(lista_invert[0],lista_invert[1])
        print(lista[0],lista[1],lista[2],lista[3])
        print(lista_invert1)
        lista_invert2=[]
        lista_invert2=(lista_invert[2],lista_invert[3])
        print(lista_invert2)
        separator=''
        animal1_=separator.join(lista_invert1)
        animal2_=separator.join(lista_invert2)
        animal1=int(animal1_)
        animal2=int(animal2_)

        print("Animal 1: ",animal1)
        print("Animal 2: ",animal2)
        gp1 = [1,2,3,4]
        gp2 = [5,6,7,8]
        gp3 = [9,10,11,12]          
        gp4 = [13,14,15,16]
        gp5 = [17,18,19,20]
        gp6 = [21,22,23,24]
        gp7 = [25,26,27,28]
        gp8 = [29,30,31,32]
        gp9 = [33,34,35,36]
        gp10 = [37,38,39,40]
        gp11 = [41,42,43,44]
        gp12 = [45,46,47,48]
        gp13 = [49,50,51,52]
        gp14 = [53,54,55,56]
        gp15 = [57,58,59,60]
        gp16 = [61,62,63,64]
        gp17 = [65,66,67,68]
        gp18 = [69,70,71,72]
        gp19 = [73,74,75,76]
        gp20 = [77,78,79,80]
        gp21 = [81,82,83,84]
        gp22 = [85,86,87,88]
        gp23 = [89,90,91,92]
        gp24 = [93,94,95,96]
        gp25 = [97,98,99,0]
        numero_animal1=None
        numero_animal2=None
        if(animal1 in gp1):
            numero_animal1=1
        if(animal1 in gp2):
            numero_animal1=2
        if(animal1 in gp3):
            numero_animal1=3
        if(animal1 in gp4):
            numero_animal1=4
        if(animal1 in gp5):
            numero_animal1=5
        if(animal1 in gp6):
            numero_animal1=6
        if(animal1 in gp7):
            numero_animal1=7
        if(animal1 in gp8):
            numero_animal1=8
        if(animal1 in gp1):
            numero_animal1=9
        if(animal1 in gp10):
            numero_animal1=10
        if(animal1 in gp11):
            numero_animal1=11
        if(animal1 in gp12):
            numero_animal1=12
        if(animal1 in gp13):
            numero_animal1=13
        if(animal1 in gp14):
            numero_animal1=14
        if(animal1 in gp15):
            numero_animal1=15
        if(animal1 in gp16):
            numero_animal1=16
        if(animal1 in gp17):
            numero_animal1=17
        if(animal1 in gp18):
            numero_animal1=18
        if(animal1 in gp19):
            numero_animal1=19
        if(animal1 in gp20):
            numero_animal1=20
        if(animal1 in gp21):
            numero_animal1=21
        if(animal1 in gp22):
            numero_animal1=22
        if(animal1 in gp23):
            numero_animal1=23
        if(animal1 in gp24):
            numero_animal1=24
        if(animal1 in gp25):
            numero_animal1=25
        if(animal2 in gp1):
            numero_animal2=1
        if(animal2 in gp2):
            numero_animal2=2
        if(animal2 in gp3):
            numero_animal2=3
        if(animal2 in gp4):
            numero_animal2=4
        if(animal2 in gp5):
            numero_animal2=5
        if(animal2 in gp6):
            numero_animal2=6
        if(animal2 in gp7):
            numero_animal2=7
        if(animal2 in gp8):
            numero_animal2=8
        if(animal2 in gp1):
            numero_animal2=9
        if(animal2 in gp10):
            numero_animal2=10
        if(animal2 in gp11):
            numero_animal2=11
        if(animal2 in gp12):
            numero_animal2=12
        if(animal2 in gp13):
            numero_animal2=13
        if(animal2 in gp14):
            numero_animal2=14
        if(animal2 in gp15):
            numero_animal2=15
        if(animal2 in gp16):
            numero_animal2=16
        if(animal2 in gp17):
            numero_animal2=17
        if(animal2 in gp18):
            numero_animal2=18
        if(animal2 in gp19):
            numero_animal2=19
        if(animal2 in gp20):
            numero_animal2=20
        if(animal2 in gp21):
            numero_animal2=21
        if(animal2 in gp22):
            numero_animal2=22
        if(animal2 in gp23):
            numero_animal2=23
        if(animal2 in gp24):
            numero_animal2=24
        if(animal2 in gp25):
            numero_animal2=25
        usu = User.objects.get(username=request.user)
        #print('ID USER',usu.id)
        apostador=Usuario.objects.get(usuario=usu.id)
        print('Número animal 1: ',numero_animal1)
        print('Número anumal 2: ',numero_animal2)
        data['class']="alert-success"
        data['msg']="Sorteio Realizado!"
        data['valor']=apostador.saldo
        hj=date.today()
        sort=sorteio.objects.create(animail1=numero_animal1,animail2=numero_animal2,data_sorteio=hj)
    return render(request, '../../jogodobicho/templates/dashboard/bicho.html',data)
def procura_ganhador(request):
    sort=sorteio.objects.all().filter(data_sorteio=date.today())
    context={}
    query_sort1=None
    for l in sort:
        query_sort1=[l]
        print(l)
    aposta2=aposta.objects.all().filter(data_aposta=date.today())
    ganhadores=None
    quant=0
    clientes=''
    quant=0
    cli=None
    for lista3 in aposta2:
        lista_apostas=[lista3.animal1_aposta,lista3.animal2_aposta]
        print(lista3.apostador.usuario.first_name)
        for lista2 in query_sort1:
            print(lista3)
            print(lista2)
            lista_sorteio=[lista2.animail1,lista2.animail2]
            for l4 in lista_apostas:
                if(l4 in lista_sorteio):
                    if(str(l4) not in str(lista_sorteio)):
                        pass
                    else:
                        quant+=1
            print(quant)
            if(quant>=2):
                email=[lista3.apostador.usuario.email]
                cli=[lista3.apostador.usuario]
                #ganhadores=[lista]
                print(lista2.id)
                #ganha=Sorteio.aposta.add(sorteio=lista2.id,aposta=lista3.id)
                a = sorteio.objects.get(id=lista2.id).aposta.add(lista3.id)

    #Sorteio.objects.create(valor1=v1[1],valor2=v1[2],valor3=v1[3],valor4=v1[4],valor5=v1[5],valor6=v1[6],data_sorteio=v1[7])
    if(cli is None):
        print('Não encontrou ganhador')
        messages.warning(request,'Não houveram ganhadores!')
    elif(cli!=None):
        #messages.SUCCESS(request,'Você ganhou')
        '''print('Encontrou ganhador')
        context={
            'valores':cli,
            'valores2':email
        }'''
        subject = 'Animal Lottery'
        message = "Olá você ganhou o sorteio do Jogo do Bicho"
        email_from = settings.EMAIL_HOST_USER
        for em in email:
            recipient_list = [str(em) ,]
            print(em)
            send_mail(subject, message, email_from, recipient_list )
        #send_mail('Djando Sending email', 'body of the message', 'fgsantos.ti@gmai
        #l.com', ['carloseduardoguedes89981456761@gmail.com',])
        context={
            'msg' :'Seu email foi enviado com sucesso.'
        }
        print(cli)
        messages.success(request, 'E-mail enviado!')
        return render(request, '../../jogodobicho/templates/ganhador.html',context)
    return render(request, '../../jogodobicho/templates/sem_ganhadores.html',context)