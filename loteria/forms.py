from django import forms
from datetime import date
'''from loteria.models import Apostas

class ApostaForm(forms.ModelForm):

    class Meta:
        model = Apostas
        fields = ('data_aposta','clientes')

        widgets = {
            'valor1': forms.TextInput(attrs={ 'class': 'form-control','type':'number', 
                                            'placeholder':'Nº','maxlength':'2','type':'number','aria-label':'Sizing example input','aria-describedby':'inputGroup-sizing-sm'}),
            'valor2': forms.TextInput(attrs={ 'class': 'form-control','placeholder':'Nº','type':'number','maxlength':'2','aria-label':'Sizing example input','aria-describedby':'inputGroup-sizing-sm'}),
            'valor3': forms.TextInput(attrs={ 'class': 'form-control','placeholder':'Nº','type':'number','maxlength':'2','aria-label':'Sizing example input','aria-describedby':'inputGroup-sizing-sm'}),
            'valor4': forms.TextInput(attrs={ 'class': 'form-control','placeholder':'Nº','type':'number','maxlength':'2','aria-label':'Sizing example input','aria-describedby':'inputGroup-sizing-sm'}),
            'valor5': forms.TextInput(attrs={ 'class': 'form-control','placeholder':'Nº','type':'number','maxlength':'2','aria-label':'Sizing example input','aria-describedby':'inputGroup-sizing-sm'}),
            'valor6': forms.TextInput(attrs={ 'class': 'form-control','placeholder':'Nº','type':'number','maxlength':'2','aria-label':'Sizing example input','aria-describedby':'inputGroup-sizing-sm'}),
            'valor_aposta':forms.TextInput(attrs={ 'id':'moeda','class': 'form-control','placeholder':'Valor Aposta','type':'number','type':'number', 'maxlength':'12','onkeypress':"return(MascaraMoeda(this,'.',',',event))",'style':'padding-bottom:0%'}),
            'clientes':forms.TextInput(attrs={ 'class': 'form-control','placeholder':'Nº','style':'display:none;'}),
            'data_aposta': forms.DateInput(attrs={ 'class': 'form-control',
                                                    'type':'date','readonly':'readonly','style':'display:none'}),
        }'''