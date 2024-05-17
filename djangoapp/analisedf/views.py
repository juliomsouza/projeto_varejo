from pprint import pprint
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView
#from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PedidoAnalise, ProdutoAnalise, ProdutoStatus, ProdutoAnaliseFoto
from .forms import ProdutoAnaliseFotoForm


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

    def get_context_data(self, **kwargs):
        context = super(AnaliseListView, self).get_context_data(**kwargs)
        pedidos = self.object_list
        status = {}
        for pedido in pedidos:
            status[pedido.id] = 'consulte'
            status_atual = ProdutoStatus.objects.filter(
                    produto__in=pedido.produtoanalise_set.all()
                ).values_list('status', flat=True)
            if 'pedido_em_edição' in status_atual or len(status_atual) == 0:
                status[pedido.id] = 'Em Edição'
            elif 'aguardando_transporte' in status_atual:
                status[pedido.id] = 'aguardando_transp_loja'
                #pprint(status_atual)
        context['status'] = status
        return context

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
       self.object.user = self.request.user 
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
        pedido_id = self.kwargs.get('pk')
        return reverse_lazy("analisedf:analise_detail", kwargs={'pk': pedido_id})
    
    def dispatch(self, request: HttpRequest, **kwargs) -> HttpResponse:
        self.pedido_analise = get_object_or_404(PedidoAnalise, pk=kwargs.get("pk"))
        return super().dispatch(request, **kwargs)

    def form_valid(self, form):
        form.instance.pedido = self.pedido_analise
        return super().form_valid(form)
    

class ProdutoAnaliseUpdateView(LoginRequiredMixin, UpdateView):
    model = ProdutoAnalise
    template_name = 'produto-analise-form.html'
    fields = ('codigo','descricao','descricao_df')

    def get_success_url(self):
        pedido_id = self.object.pedido.id
        return reverse_lazy("analisedf:analise_detail", kwargs={'pk': pedido_id})
    
class ProdutoAnaliseDetailView(LoginRequiredMixin,DetailView):
    model = ProdutoAnalise
    template_name = 'analisedf/produto_detail.html'
    context_object_name = 'produto_analise'


def produto_upload_fotos(request, produto_id):
    form = ProdutoAnaliseFotoForm(request.POST, request.FILES)
    produto = get_object_or_404(ProdutoAnalise, pk=produto_id)
    if request.method == 'POST':        
        imagens = request.FILES.getlist('image')
        for imagem in imagens:
            produto_imagem = ProdutoAnaliseFoto(image=imagem, produto=produto)
            produto_imagem.save()
        return redirect(reverse_lazy("analisedf:produto_detail", kwargs={'pk': produto_id}))
    
    context = {'form': form, 'produto': produto}
    return render(request,'analisedf/produto_analise_foto_form.html', context)