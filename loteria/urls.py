from django.urls import path,include
from . import views
app_name='loteria'

urlpatterns = [
    #path('', views.page_login, name='page_login'),
    path('aposta/<str:valor>/',views.form_jogo,name='apostar'),
    path('cadastra_aposta/',views.cadastra_aposta,name='cadastra_numero'),
    path('sortear/',views.sorteia_numero, name='sortear'),
    path('ver_ganhadores/',views.procura_ganhador2,name='testar_ganhadores'),
    path('sacar/',views.sacar,name='sacar'),
    #path('autenticar_cliente/',views.autenticar_cliente,name='autenticar_cliente'),
    #path('logout_usuario', views.logout_usuario, name='logout_usuario'),
]