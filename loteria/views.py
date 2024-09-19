import sys
sys.path.append("accounts/")
from accounts.models import Usuario
import asyncio
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect
#from .forms import ApostaForm
from random import randint
from itertools import chain
from .models import Apostas,Sorteio
from datetime import date,time
from django.contrib import messages #import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from accounts.views import *
@login_required(login_url='accounts:/dologing/')
def form_jogo(request):
    valor=consultaSaldo(request)
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
    saldo = consultaSaldo(request)
    data = {}
    
    if request.method == 'POST':
        form = request.POST
        print('Dados do Formulário: ', form)
        
        # Obtenha os números apostados
        lista = [form.get(i) for i in form if i.isdigit() and form.get(i) is not None]
        
        # Verifique se a lista tem pelo menos 6 números escolhidos
        if len(lista) < 6:
            data['msg'] = 'Por favor, selecione pelo menos 6 números.'
            data['class'] = 'alert-danger'
            data['valor'] = saldo
            return redirect("accounts:/dashboard/")

        hj = date.today()
        usu = request.POST.get('usuario', None)
        valor = request.POST.get('moeda', None)
        
        try:
            user_model = User.objects.get(id=usu)
            jogador = Usuario.objects.get(usuario=user_model.id)
        except (User.DoesNotExist, Usuario.DoesNotExist):
            data['msg'] = 'Usuário ou jogador não encontrado.'
            data['class'] = 'alert-danger'
            data['valor'] = saldo
            return redirect("accounts:/dashboard/")

        if int(valor) <= saldo:
            # Cria a aposta
            aposta = Apostas.objects.create(
                valor1=lista[0], valor2=lista[1], valor3=lista[2],
                valor4=lista[3], valor5=lista[4], valor6=lista[5],
                data_aposta=hj, valor_aposta=valor, usuario=user_model
            )
            # Atualiza o saldo do jogador
            jogador.saldo -= float(valor)
            jogador.save()

            data['msg'] = 'Aposta realizada com sucesso!'
            data['class'] = 'alert-success'
            data['valor'] = jogador.saldo
        else:
            data['msg'] = 'Saldo insuficiente!'
            data['class'] = 'alert-danger'
            data['valor'] = saldo
            
    data['valor'] = saldo
    return redirect("accounts:/dashboard/")
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
def procura_ganhador(request):
    var = {}
    hoje = date.today()
    saldo =consultaSaldo(request)
    # Obter todos os sorteios de hoje
    sorteios = Sorteio.objects.filter(data_sorteio=hoje)
    valor_aposta = request.POST.get('moeda')
    # Obter todas as apostas de hoje, indexadas por usuário para otimizar a busca
    apostas_por_usuario = Apostas.objects.filter(data_aposta=hoje).values('usuario', 'valor1', 'valor2', 'valor3', 'valor4', 'valor5', 'valor6')
    apostas_por_usuario_dict = {}
    for aposta in apostas_por_usuario:
        usuario_id = aposta['usuario']
        numeros_aposta = set([aposta['valor1'], aposta['valor2'], aposta['valor3'], aposta['valor4'], aposta['valor5'], aposta['valor6']])
        apostas_por_usuario_dict.setdefault(usuario_id, []).append(numeros_aposta)
    for sorteio in sorteios:
        numeros_sorteio = set([sorteio.valor1, sorteio.valor2, sorteio.valor3, sorteio.valor4, sorteio.valor5, sorteio.valor6])
        ganhadores = []
        for usuario_id, apostas in apostas_por_usuario_dict.items():
            for aposta in apostas:
                if aposta.issubset(numeros_sorteio):
                    ganhadores.append(usuario_id)
                    # Atualizar o saldo do ganhador (implementar a lógica de atualização)
                    usuario = User.objects.get(id=usuario_id)
                    #usuario.usuario.saldo += valor_aposta*2  # Substituir por valor_premio real
                    usuario.save()
    # Enviar e-mails para os ganhadores
        if ganhadores:
            subject = 'Parabéns! Você ganhou na loteria!'
            for usuario_id in ganhadores:
                usuario = User.objects.get(id=usuario_id)
                context = {'usuario': usuario}
                message = render_to_string('loteria/aposta3.html', context)
                recipient_list = [usuario.email]
                try:
                    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
                    print(f'E-mail enviado para {usuario.email}')
                except Exception as e:
                    print(f'Erro ao enviar e-mail para {usuario.email}: {e}')
        return redirect('accounts:dashboard')
    return render(request, 'loteria/sem_ganhadores.html',var)
def sacar(request):
    pass