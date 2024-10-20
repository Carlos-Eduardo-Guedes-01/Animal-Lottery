from django.shortcuts import render
import sys
sys.path.append("accounts/")
from accounts.models import Usuario
from accounts.views import consultaSaldo
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
# Na sua view
def jogodobicho(request):
    # Supondo que você tenha um modelo `Animal` para armazenar os dados dos animais
    valor = consultaSaldo(request.user.id)
    context = {
        'valor': valor.saldo,
    }
    return render(request, 'dashboard/bicho.html', context)

#CADASTRO DE APOSTAS
def jogodobicho2(request):
    if request.method == "POST":
        data = {}
        form = request.POST
        lista = []
        hj = date.today()
        
        # Capturando e limpando o valor
        valor = request.POST.get('moeda', '').strip()
        print("POST DATA: ", request.POST)
        print("VALOR LIMPO: ", valor)

        # Verifica se o valor é válido antes de prosseguir
        if not valor:
            print("Erro: O valor da aposta está vazio.")
            return render(request, '../../jogodobicho/templates/dashboard/bicho.html', {'error': 'O valor da aposta não pode ser vazio.'})

        try:
            valor_float = float(valor.replace(',', '.'))  # Converte para float
        except ValueError:
            print("Erro: O valor não é um número válido.")
            return render(request, '../../jogodobicho/templates/dashboard/bicho.html', {'error': 'O valor da aposta deve ser um número.'})

        jogador = consultaSaldo(request.user.id)

        # Verifica se o jogador existe
        if not jogador:
            print("Erro: Jogador não encontrado.")
            return render(request, '../../jogodobicho/templates/dashboard/bicho.html', {'error': 'Jogador não encontrado.'})

        # Verifica se o jogador tem saldo suficiente
        if jogador.saldo < valor_float:
            print("Erro: Saldo insuficiente.")
            return render(request, '../../jogodobicho/templates/dashboard/bicho.html', {'error': 'Saldo insuficiente para realizar a aposta.'})

        for i in form:
            lista.append(i)

        try:
            # Cria a aposta
            animal1_aposta0 = aposta.objects.create(
                animal1_aposta=lista[1],
                animal2_aposta=lista[2],
                data_aposta=hj,
                valor_aposta=valor_float,
                apostador=jogador
            )

            # Subtrai o valor da aposta do saldo do jogador
            jogador.saldo -= valor_float
            jogador.save()  # Salva as alterações no saldo

        except Exception as e:
            print("Erro ao criar aposta: ", e)
            return render(request, '../../jogodobicho/templates/dashboard/bicho.html', {'error': 'Erro ao registrar a aposta.'})
        
        return redirect("accounts:dashboard")
    
    return render(request, '../../jogodobicho/templates/dashboard/bicho.html', {'error': 'Método não permitido.'})
def sorteio_(usuario):
    from datetime import timezone
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

    # Obtenha o usuário atual (exemplo Django)
    usu = User.objects.get(username=usuario)
    apostador = Usuario.objects.get(usuario=usu.id)

    # Cria o sorteio no banco de dados
    hj = timezone.now().date()
    novo_sorteio = sorteio.objects.create(
        animail1=numero_animal1, 
        animail2=numero_animal2, 
        data_sorteio=hj
    )

    return {
        'msg': 'Sorteio realizado!',
        'animal1': numero_animal1,
        'animal2': numero_animal2,
        'saldo': apostador.saldo
    }

# Função que procura ganhadores
def procura_ganhador():
    from datetime import timezone
    # Obtém o sorteio do dia atual
    sorteios_do_dia = sorteio.objects.filter(data_sorteio=timezone.now().date())

    if not sorteios_do_dia.exists():
        return 'Nenhum sorteio realizado hoje.'

    # Obtém as apostas do dia atual
    apostas_do_dia = aposta.objects.filter(data_aposta=timezone.now().date())
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

        send_mail(subject, message, email_from, recipient_list)

    return 'E-mails enviados para os ganhadores com sucesso!'