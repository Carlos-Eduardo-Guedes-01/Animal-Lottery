from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import time

# Verifica se o usuário está logado e retorna o objeto 'Usuario'
@login_required
def verifica_login(request):
    return request.user  # Retorna a instância do usuário autenticado

# Consulta saldo de um usuário
def consultaSaldo(id_user):
    user_model = User.objects.get(id=id_user)
    usuario = Usuario.objects.get(usuario=user_model)
    return usuario

# Página inicial
def home(request):
    return render(request, '../../accounts/templates/home.html')

# Formulário de cadastro
def create(request):
    return render(request, '../../accounts/templates/create.html')

# Inserção dos dados do usuário no banco
def store(request):
    data = {}
    try:
        # Verifica se já existe um usuário com o mesmo nome ou senha
        usuario_aux = User.objects.get(username=request.POST['user'])
        usuario_aux2 = User.objects.filter(password=request.POST['password'])

        if usuario_aux or usuario_aux2:
            data['msg'] = 'Usuario ou Senha já existem!'
            data['class'] = 'alert-danger'
    except User.DoesNotExist:
        # Cria um novo usuário se não existir
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()

        # Cria o objeto 'Usuario' associado ao novo usuário
        query_user = User.objects.get(id=user.id)
        usu = Usuario.objects.create(usuario=query_user, saldo=0)
        data['msg'] = 'Usuário Cadastrado com sucesso! Faça Login.'
        data['class'] = 'alert-success'

    return render(request, '../../accounts/templates/painel.html', data)

# Formulário painel de login
def painel(request):
    return render(request, '../../accounts/templates/painel.html')

# Processa login tradicional
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect("accounts:dashboard")
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, '../../accounts/templates/painel.html', data)

# Dashboard após o login
@login_required
def dashboard(request):
    usuario = consultaSaldo(request.user.id)  # Use o ID do User autenticado

    if not usuario:
        return redirect("accounts:painel")  # Redireciona se não encontrar o usuário

    # Agora você pode acessar o saldo
    saldo = usuario.saldo

    context = {
        'usuario': usuario,
        'valor': saldo,
        # Outros dados para o contexto
    }

    return render(request, 'dashboard/home.html', context)
# Logout
def logouts(request):
    logout(request)
    return redirect('accounts:painel')

# Alterar senha
@login_required
def changepass(request):
    user = request.user
    return render(request, '../../accounts/templates/dashboard/changepassword.html', {'user': user})

# Processa a alteração de senha
@login_required
def changePassword(request):
    senha_atual = request.POST.get("senha_atual")
    nova_senha = request.POST.get("nova_senha")
    user = User.objects.get(username=request.user.username)

    context = {}
    if user.check_password(senha_atual):  # Verifica se a senha atual está correta
        user.set_password(nova_senha)  # Altera a senha
        user.save()
        context = {
            'msg': "Senha Alterada com Sucesso!",
            'class': "alert-success"
        }
    else:
        context = {
            'msg': "Senha atual inválida!",
            'class': "alert-danger"
        }

    return render(request, '../../accounts/templates/dashboard/changepassword.html', context)

# Função de depósito
@login_required
def depositar(request):
    usuario = consultaSaldo(request.user.id)
    print('Saldo atual:', usuario.saldo)
    valor = request.POST.get('valor')

    if valor and float(valor) > 0:
        usuario.saldo = usuario.saldo + float(valor)
        usuario.save()
        print('Saldo novo:', usuario.saldo)
    else:
        print('Valor inválido para depósito!')

    return redirect('accounts:dashboard')

# Login com Google
def google_login(request):
    # Redireciona para o login com o Google
    time.sleep(2)
    return redirect('social:begin', 'google-oauth2')

# Callback após o login com Google
def google_login_callback(request):
    # Aqui tratamos o retorno do login via Google
    google_user_data = request.user  # Dados do Google

    # Busque o usuário no banco de dados ou crie um novo
    try:
        user = User.objects.get(username=google_user_data.username)
    except User.DoesNotExist:
        # Se não existir, cria um novo usuário no Django
        user = User.objects.create_user(
            username=google_user_data.username,
            email=google_user_data.email,
            password=None  # Login social não precisa de senha
        )
        user.save()

    # Verifique se o objeto 'Usuario' já existe, se não, cria-o
    try:
        usuario = Usuario.objects.get(usuario=user)
    except Usuario.DoesNotExist:
        usuario = Usuario.objects.create(usuario=user, saldo=0.0)

    # Autentica o usuário
    login(request, user)
    return redirect('accounts:dashboard')
