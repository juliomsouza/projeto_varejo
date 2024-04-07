from django import forms
from .models import PedidoAnalise


class PedidoAnaliseForm(forms.ModelForm):
    class Meta:
        model = PedidoAnalise
        fields = ['Filial','NomeCliente','Telefone','Email','CPF/CNPJ','NFe/CFe','data_entrada','data_max_resp','data_max_retorno']