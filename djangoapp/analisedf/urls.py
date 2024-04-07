from django.contrib import admin
from django.urls import path, include
from .views import AnaliseListView, ProdutoListView, ProdStatusListView, Login, PedidoAnaliseCreateView, ProdutoAnaliseCreateView

app_name = 'analisedf'

urlpatterns = [
    #path('', Login.as_view(), name='login'),
    path('analisedf', AnaliseListView.as_view(), name='analiselist'),
    path('list-prod', ProdutoListView.as_view(), name='list_prod'),
    path('prod-status', ProdStatusListView.as_view(), name='prod_status'),
    path('pedido-analise/incluir', PedidoAnaliseCreateView.as_view(), name='pedido_analise'),
    path('pedido-analise/<int:pk>/produto/incluir', ProdutoAnaliseCreateView.as_view(), name='produto_analise'),
 ]