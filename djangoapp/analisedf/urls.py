from django.contrib import admin
from django.urls import path, include
from .views import (AnaliseListView, ProdStatusListView, Login, PedidoAnaliseCreateView, ProdutoAnaliseCreateView,
                     AnaliseDetailView, ProdutoAnaliseUpdateView, ProdutoAnaliseDetailView, produto_upload_fotos)


app_name = 'analisedf'

urlpatterns = [
    #path('', Login.as_view(), name='login'),
    path('analisedf/', AnaliseListView.as_view(), name='analiselist'),
    path('analisedf/<int:pk>', AnaliseDetailView.as_view(), name='analise_detail'),
    path('prod-status/', ProdStatusListView.as_view(), name='prod_status'),
    path('pedido-analise/incluir/', PedidoAnaliseCreateView.as_view(), name='pedido_analise'),
    path('pedido-analise/<int:pk>/produto/incluir/', ProdutoAnaliseCreateView.as_view(), name='produto_analise'),
    path('produto/<int:pk>/editar/', ProdutoAnaliseUpdateView.as_view(), name='produto_update'),
    path('produto/<int:pk>', ProdutoAnaliseDetailView.as_view(), name='produto_detail'),
    path('produto/<int:produto_id>/upload', produto_upload_fotos, name='produto_foto_upload'),
 ]
