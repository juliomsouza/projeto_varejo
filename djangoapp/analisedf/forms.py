from django import forms
from .models import PedidoAnalise, ProdutoAnaliseFoto

'''
class PedidoAnaliseForm(forms.ModelForm):
    class Meta:
        model = PedidoAnalise
        fields = ['Filial','NomeCliente','Telefone','Email','CPF/CNPJ','NFe/CFe','data_max_resp','data_max_retorno']
'''

class ProdutoAnaliseFotoForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.TextInput(attrs={'name': 'fotos', 'type': 'File', 'multiple': 'True'}), label='')

    class Meta:
        model = ProdutoAnaliseFoto
        fields = ['image']