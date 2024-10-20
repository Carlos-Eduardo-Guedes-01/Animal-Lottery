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
from jogodobicho.models import *
from loteria.models import Sorteio, Apostas, User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from random import randint
from django.utils import timezone  # Certifique-se de que o timezone do Django está importado
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
                    #usuario = consultaSaldo(usuario_id)  # Usa consultaSaldo sem request
                    usuario = User.objects.get(id=usuario_id)
                    
                    # Atualize o saldo ou faça outro processamento
                    #usuario.saldo = saldo  # Dependendo de sua lógica, você pode alterar o saldo
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





# TAREFAS JOGO DO BICHO

def sorteio_():
    from random import sample

    # Gera 4 números aleatórios distintos entre 0 e 9
    lista = sample(range(10), 4)
    animal1, animal2 = int(''.join(map(str, lista[:2]))), int(''.join(map(str, lista[2:])))

    # Definição dos grupos de animais
    grupos = {
        1: [1, 2, 3, 4], 2: [5, 6, 7, 8], 3: [9, 10, 11, 12], 4: [13, 14, 15, 16],
        5: [17, 18, 19, 20], 6: [21, 22, 23, 24], 7: [25, 26, 27, 28], 8: [29, 30, 31, 32],
        9: [33, 34, 35, 36], 10: [37, 38, 39, 40], 11: [41, 42, 43, 44], 12: [45, 46, 47, 48],
        13: [49, 50, 51, 52], 14: [53, 54, 55, 56], 15: [57, 58, 59, 60], 16: [61, 62, 63, 64],
        17: [65, 66, 67, 68], 18: [69, 70, 71, 72], 19: [73, 74, 75, 76], 20: [77, 78, 79, 80],
        21: [81, 82, 83, 84], 22: [85, 86, 87, 88], 23: [89, 90, 91, 92], 24: [93, 94, 95, 96],
        25: [97, 98, 99, 0],
    }

    # Mapeia os números dos animais
    numero_animal1 = next((num for num, lst in grupos.items() if animal1 in lst), None)
    numero_animal2 = next((num for num, lst in grupos.items() if animal2 in lst), None)

    # Cria o sorteio no banco de dados
    hj = timezone.now().date()  # Captura a data atual corretamente
    novo_sorteio = sorteio.objects.create(
        animail1=numero_animal1, 
        animail2=numero_animal2, 
        data_sorteio=hj
    )

    return {
        'msg': 'Sorteio realizado!',
        'animal1': numero_animal1,
        'animal2': numero_animal2,
        'data': str(hj),
    }
# Função que procura ganhadores
def procura_ganhador_bicho():
    
    # Obtém o sorteio do dia atual
    sorteios_do_dia = sorteio.objects.filter(data_sorteio=timezone.now())

    if not sorteios_do_dia.exists():
        return 'Nenhum sorteio realizado hoje.'

    # Obtém as apostas do dia atual
    apostas_do_dia = aposta.objects.filter(data_aposta=timezone.now())
    ganhadores = []

    for sorteio_atual in sorteios_do_dia:
        lista_sorteio = [sorteio_atual.animail1, sorteio_atual.animail2]

        for aposta_atual in apostas_do_dia:
            lista_apostas = [aposta_atual.animal1_aposta, aposta_atual.animal2_aposta]
            # Verifica se a aposta contém pelo menos 2 números sorteados
            if len(set(lista_apostas) & set(lista_sorteio)) >= 2:
                ganhadores.append(aposta_atual.apostador)

    if not ganhadores:
        return 'Não houveram ganhadores!'

    # Envio de email para os ganhadores
    for ganhador in ganhadores:
        subject = 'Animal Lottery'
        message = "Olá, você ganhou o sorteio do Jogo do Bicho!"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [ganhador.usuario.email]

        # Envia o e-mail para o ganhador
        send_mail(subject, message, email_from, recipient_list)

    return 'E-mails enviados para os ganhadores com sucesso!'

def teste_timezone():
    from django.utils import timezone
    print("Data e hora atual:", timezone.now())