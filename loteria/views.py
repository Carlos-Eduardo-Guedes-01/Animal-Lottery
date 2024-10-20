from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from random import randint
from datetime import date
from .models import Apostas, Sorteio
from accounts.models import Usuario
from accounts.views import consultaSaldo, verifica_login

# Formulário de jogo
def form_jogo(request):
    autenticacao = verifica_login(request)
    usuario = consultaSaldo(autenticacao.id)
    if not autenticacao:
        return redirect("accounts:painel")  # Redireciona se não estiver autenticado

    # Prepare os dados para renderização
    valor = usuario.saldo
    hj = date.today()
    lista_numeros = list(range(1, 61))  # Números de 1 a 60

    context = {
        'hj': hj,
        'user': usuario.id,
        'lista_numeros': lista_numeros,
        'valor': valor
    }

    return render(request, 'loteria/aposta3.html', context)

# Cadastro de apostas
def cadastra_aposta(request):
    autenticacao = verifica_login(request)

    # Verifique se a autenticação retornou um objeto de usuário
    if not autenticacao or not isinstance(autenticacao, User):
        print("Usuário não autenticado ou não é uma instância de User.")
        return redirect("accounts:painel")  # Redireciona se não estiver autenticado

    usuario = consultaSaldo(autenticacao.id)
    saldo = usuario.saldo if usuario else 0  # Assegure que saldo é um número

    if request.method == 'POST':
        form = request.POST
        print('Dados do Formulário: ', form)

        # Obter os números apostados
        # Obter os números apostados
        lista = [int(form.get(i)) for i in form if i.isdigit() and form.get(i) is not None]
        print(f'Números apostados: {lista}')  # Log dos números apostados

        # Verifique se há pelo menos 6 números
        if len(lista) < 6:
            print('Menos de 6 números escolhidos.')
            return redirect("accounts:dashboard")

        hj = date.today()
        valor = float(form.get('moeda', 0))  # Garantir que é um float

        # Verifica se o saldo é suficiente
        if saldo < valor:
            print('Saldo insuficiente!')
            return redirect("accounts:dashboard")

        # Registrar aposta no banco de dados
        try:
            aposta = Apostas.objects.create(
                usuario=autenticacao,  # Aqui você deve usar o usuário do Django
                valor1=lista[0],
                valor2=lista[1],
                valor3=lista[2],
                valor4=lista[3],
                valor5=lista[4],
                valor6=lista[5],
                data_aposta=hj,
                valor_aposta=valor  # Certifique-se de que o valor da aposta está sendo salvo
            )
            print(f'Aposta cadastrada: {aposta}')

            # Deduzir o valor apostado do saldo
            usuario.saldo -= valor
            usuario.save()
            print(f'Saldo atualizado: {usuario.saldo}')
        except Exception as e:
            print(f'Erro ao cadastrar aposta ou atualizar saldo: {e}')

    return redirect("accounts:dashboard")


# Função para sortear números
def sorteia_numero(request):
    usuario = verifica_login(request)
    v1 = []
    c = 0
    while c < 6:
        v = randint(1, 60)
        if v not in v1:
            v1.append(v)
        c += 1
    v1.append(date.today())

    # Registrar sorteio
    Sorteio.objects.create(
        valor1=v1[0], valor2=v1[1], valor3=v1[2], 
        valor4=v1[3], valor5=v1[4], valor6=v1[5], 
        data_sorteio=v1[6]
    )

    context = {'valores': v1}
    return render(request, 'loteria/listar_sorteio.html', context)

# Procura ganhador do sorteio
def procura_ganhador(request):
    var = {}
    hoje = date.today()
    
    # Obter todos os sorteios de hoje
    sorteios = Sorteio.objects.filter(data_sorteio=hoje)

    # Obter todas as apostas de hoje
    apostas_por_usuario = Apostas.objects.filter(data_aposta=hoje).values('usuario', 'valor1', 'valor2', 'valor3', 'valor4', 'valor5', 'valor6')

    # Organizar apostas por usuário
    apostas_por_usuario_dict = {}
    for aposta in apostas_por_usuario:
        usuario_id = aposta['usuario']
        numeros_aposta = set([aposta['valor1'], aposta['valor2'], aposta['valor3'], aposta['valor4'], aposta['valor5'], aposta['valor6']])
        apostas_por_usuario_dict.setdefault(usuario_id, []).append(numeros_aposta)

    ganhadores = []
    for sorteio in sorteios:
        numeros_sorteio = set([sorteio.valor1, sorteio.valor2, sorteio.valor3, sorteio.valor4, sorteio.valor5, sorteio.valor6])
        for usuario_id, apostas in apostas_por_usuario_dict.items():
            for aposta in apostas:
                if aposta.issubset(numeros_sorteio):
                    ganhadores.append(usuario_id)
                    usuario = Usuario.objects.get(id=usuario_id)
                    usuario.saldo += 1000  # Prêmio (ajustar conforme necessário)
                    usuario.save()

    # Enviar e-mails para os ganhadores
    if ganhadores:
        subject = 'Parabéns! Você ganhou na loteria!'
        for usuario_id in ganhadores:
            usuario = User.objects.get(id=usuario_id)
            context = {'usuario': usuario}
            message = render_to_string('loteria/email_vencedor.html', context)
            recipient_list = [usuario.email]
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
                print(f'E-mail enviado para {usuario.email}')
            except Exception as e:
                print(f'Erro ao enviar e-mail para {usuario.email}: {e}')
    
    return redirect('accounts:dashboard')

# Função de saque (não implementada)
def sacar(request):
    pass
