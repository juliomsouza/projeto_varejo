from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
#from django.contrib.auth.decorators import login_required
from .models import PedidoAnalise, ProdutoAnalise, ProdutoStatus
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(TemplateView):
   template_name = "login.html"

#class Analisedefeito(TemplateView):
 #   template_name = "analisedf.html"

#@login_required
class ProdutoListView(LoginRequiredMixin,ListView):
    model = ProdutoAnalise
    template_name = 'list-prod.html'
    context_object_name = 'list_prod'

class AnaliseListView(LoginRequiredMixin,ListView):
    model = PedidoAnalise
    template_name = 'analisedf.html'
    context_object_name = 'analiselist' 

class ProdStatusListView(LoginRequiredMixin,ListView):
    model = ProdutoStatus
    template_name = 'prod-status.html'
    context_object_name = 'prod_status'

class PedidoAnaliseCreateView(LoginRequiredMixin,CreateView):
    model = PedidoAnalise
    template_name = 'pedidoanalise_form.html'
    fields = ('filial','nome_cliente','telefone','email','cpf_cnpj','doc_fiscal')
    success_url = reverse_lazy('analisedf:produto-analise') # URL para redirecionado em caso de sucesso
    #success_message = 'Pedido criado!.'
    # implementa o método que conclui a ação com sucesso (dentro da classe)
    #def form_valid(self, form):
     #   messages.success(self.request, self.success_message)
      #  return super(ProdutoAnalise, self).form_valid(form)
    
class ProdutoAnaliseCreateView(LoginRequiredMixin,CreateView):
    model = ProdutoAnalise
    template_name = 'produto-analise_form.html'
    fields = ('pedido','codigo','descricao','descricao_df')

    def get_success_url(self):
        return reverse_lazy("analisedf:analiselist")
    
