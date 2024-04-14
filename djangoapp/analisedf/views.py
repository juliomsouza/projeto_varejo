from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, DetailView
#from django.contrib.auth.decorators import login_required
from .models import PedidoAnalise, ProdutoAnalise, ProdutoStatus
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(TemplateView):
   template_name = "login.html"

class AnaliseDetailView(LoginRequiredMixin,DetailView):
    model = PedidoAnalise
    template_name = 'analisedf/pedido_detail.html'
    context_object_name = 'pedido_analise'



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
    template_name = 'pedidoanalise-form.html'
    fields = ('filial','nome_cliente','telefone','email','cpf_cnpj','doc_fiscal')
    #success_url = reverse_lazy('analisedf:produto_analise') # URL para redirecionado em caso de sucesso
    
    def form_valid(self, form):
       self.object = form.save()

       #messages.success(self.request, self.success_message)
       return super(PedidoAnaliseCreateView, self).form_valid(form)
    
    def get_success_url(self) -> str:
        #print(self.object.id)

        return reverse_lazy('analisedf:produto_analise', kwargs={'pk': self.object.id})
    #success_message = 'Pedido criado!.'
    # implementa o método que conclui a ação com sucesso (dentro da classe)
    
    
class ProdutoAnaliseCreateView(LoginRequiredMixin,CreateView):
    model = ProdutoAnalise
    template_name = 'produto-analise-form.html'
    fields = ('codigo','descricao','descricao_df')

    def get_success_url(self):
        return reverse_lazy("analisedf:analiselist")
    
    def dispatch(self, request: HttpRequest, **kwargs) -> HttpResponse:
        self.pedido_analise = get_object_or_404(PedidoAnalise, pk=kwargs.get("pk"))
        return super().dispatch(request, **kwargs)

    def form_valid(self, form):
        form.instance.pedido = self.pedido_analise
        return super().form_valid(form)
    