import os
import django
import sys

# Defina o caminho base do projeto (onde o manage.py está localizado)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configure o Django para usar o arquivo settings.py do seu projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  # Certifique-se de que 'loteria' é o nome correto do seu projeto

# Inicialize o Django
django.setup()

# Agora você pode fazer suas importações
from accounts.views import consultaSaldo
from loteria.models import Sorteio, Apostas, User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from random import randint
from datetime import date

# O resto do código continua aqui


def sorteia_numero():
    v1 = []
    c = 0
    while c < 6:
        v = randint(1, 60)
        if v not in v1:
            v1.append(v)
        else:
            c -= 1
        c += 1
    v1.append(date.today())
    Sorteio.objects.create(valor1=v1[0], valor2=v1[1], valor3=v1[2], valor4=v1[3], valor5=v1[4], valor6=v1[5], data_sorteio=v1[6])

def procura_ganhador():
    print("Buscando ganhadores do dia...")
    hoje = date.today()

    # Busca os sorteios do dia
    sorteios = Sorteio.objects.filter(data_sorteio=hoje)

    # Busca as apostas do dia agrupadas por usuário
    apostas_por_usuario = Apostas.objects.filter(data_aposta=hoje).values(
        'usuario', 'valor1', 'valor2', 'valor3', 'valor4', 'valor5', 'valor6'
    )
    
    # Dicionário para armazenar as apostas por usuário
    apostas_por_usuario_dict = {}
    for aposta in apostas_por_usuario:
        usuario_id = aposta['usuario']
        numeros_aposta = set([
            aposta['valor1'], aposta['valor2'], aposta['valor3'],
            aposta['valor4'], aposta['valor5'], aposta['valor6']
        ])
        apostas_por_usuario_dict.setdefault(usuario_id, []).append(numeros_aposta)

    # Verifica as apostas e sorteios
    for sorteio in sorteios:
        numeros_sorteio = set([
            sorteio.valor1, sorteio.valor2, sorteio.valor3,
            sorteio.valor4, sorteio.valor5, sorteio.valor6
        ])
        ganhadores = []
        for usuario_id, apostas in apostas_por_usuario_dict.items():
            for aposta in apostas:
                if aposta.issubset(numeros_sorteio):
                    ganhadores.append(usuario_id)
                    
                    # Calcula o saldo do usuário
                    saldo = consultaSaldo(usuario_id)  # Usa consultaSaldo sem request
                    usuario = User.objects.get(id=usuario_id)
                    
                    # Atualize o saldo ou faça outro processamento
                    usuario.saldo = saldo  # Dependendo de sua lógica, você pode alterar o saldo
                    usuario.save()

        # Envia e-mails aos ganhadores
        if ganhadores:
            subject = 'Parabéns! Você ganhou na loteria!'
            print("Enviando e-mails aos ganhadores...")
            for usuario_id in ganhadores:
                usuario = User.objects.get(id=usuario_id)
                context = {'usuario': usuario}
                message = render_to_string('loteria/notificacao.html', context)
                recipient_list = [usuario.email]
                send_mail(
                    subject,
                    '',  # Corpo do e-mail em texto simples (não é necessário, pode ser deixado vazio)
                    settings.EMAIL_HOST_USER,  # Seu e-mail de envio
                    [usuario.email],  # Lista de destinatários
                    html_message=message,  # Mensagem em HTML
                )

            print("E-mails enviados com sucesso!")

from datetime import datetime

def minha_tarefa():
    print(f"A tarefa foi executada em: {datetime.now()}")