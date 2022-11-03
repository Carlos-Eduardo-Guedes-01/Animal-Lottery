import email
from django.shortcuts import render, redirect,get_object_or_404
#from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Usuario
from datetime import datetime
import time
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

'''quant=0
while True:
    atual=datetime.now()
    if(atual.hour==20 and atual.minute==57 and quant<1):
        redirect(sortear)
        quant+=1
    time.sleep(60)'''

# Create your views here.
def home(request):
    return render(request,'../../accounts/templates/home.html')

#formulário de Cadastro
def create(request):
    return render(request,'../../accounts/templates/create.html')

#Inserção dos dados do usuário no banco
def store(request):
    data ={}
    try:
        usuario_aux = User.objects.get(username=request.POST['user'])
        usuario_aux2= User.objects.filter(password=request.POST['password'])

        if usuario_aux or usuario_aux2:
            data['msg'] = 'Usuario ou Senha já existem!'
            data['class'] = 'alert-danger'
    except User.DoesNotExist:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        query_user=User.objects.get(id=user.id)
        usu= Usuario.objects.create(usuario=query_user,saldo=0)
        data['msg'] = 'Usuário Cadastrado com sucesso! Faça Login.'
        data['class'] = 'alert-success'''
    return render(request,'../../accounts/templates/painel.html', data)
    '''senha=request.POST.get('password')
    usu=request.POST.get('user')
    model_user=User.objects.all()
    query_pass=model_user.extra(where=['password=%s'], params=[senha])
    query_user=model_user.extra(where=['username=%s'], params=[usu])
    #query_pass=model_user.filter(password=senha)
    #query_user=model_user.filter(username=usu)

    print("Senha: ",query_pass)
    print("User: ",query_user)
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    if((query_pass)or(query_user)):
        data['msg'] = 'Usuario ou Senha já existem!'
        data['class'] = 'alert-danger'
    elif((User.DoesNotExist)):
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        query_user=User.objects.get(id=user.id)
        usu= Usuario.objects.create(usuario=query_user,saldo=0)
        data['msg'] = 'Usuário Cadastrado com sucesso! Faça Login.'
        data['class'] = 'alert-success'''
    


#formulário painel de login
def painel(request):
    return render(request,'../../accounts/templates/painel.html')
def chama_sort(request):
    redirect('losteria:sortear')

#processa login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        mode_user=User.objects.get(username=user)
        jogador=Usuario.objects.get(usuario=mode_user.id)
        #print(jogador.saldo)
        login(request, user)
        return render(request,'../../accounts/templates/dashboard/home.html',{'valor':jogador.saldo})
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request,'../../accounts/templates/painel.html', data)

#Página inicial do dashboard
def dashboard(request,valor):
    return render(request,'../../accounts/templates/dashboard/home.html',{'valor':valor})

#Logout do sistema
def logouts(request):
    logout(request)
    return redirect('accounts:/painel/')

#Alterar senha
def changepass(request,user):
    return render(request, '../../accounts/templates/dashboard/changepassword.html',{'user':user})

def changePassword(request):
    senha=request.POST.get("senha_atual")
    user=request.POST.get("usu")
    u = User.objects.get(username=user)
    data=[]
    context={}
    if(u is not None):
        u.set_password(request.POST.get('nova_senha'))
        u.save()
        context={
            'msg':"Senha Alterada com Sucesso!",
            'class':"alert-success"
        }
    else:
        context={
            'msg':"Senha Antiga inválida!",
            'class':"alert-danger"
        }
    return render(request, '../../accounts/templates/dashboard/changepassword.html',context)
def depositar(request):
    usu=request.POST.get('usu')
    valor=request.POST.get('valor')
    print('Usuário: ',usu)
    mode_user=User.objects.get(id=usu)
    jogador=Usuario.objects.get(usuario=mode_user.id)
    upd=Usuario.objects.filter(usuario=mode_user.id).update(saldo=jogador.saldo+float(valor))
    jogador=Usuario.objects.get(usuario=mode_user.id)
    return render(request, '../../accounts/templates/dashboard/home.html',{'valor':jogador.saldo})