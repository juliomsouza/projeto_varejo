# -*- coding: utf-8 -*-
from django.contrib import admin


from analisedf.models import PedidoAnalise, ProdutoAnalise, ProdutoAnaliseFoto, ProdutoStatus


@admin.register(PedidoAnalise)
class PedidoAnaliseAdmin(admin.ModelAdmin):
    exclude = ('data_max_resp','data_max_retorno')
    list_display = (
        'id',
        'user',
        'filial',
        'nome_cliente',
        'telefone',
        'email',
        'cpf_cnpj',
        'doc_fiscal',
        'data_entrada',
        'data_max_resp',
        'data_max_retorno',
    )
    list_filter = ('data_entrada', 'data_max_resp', 'data_max_retorno')
    list_per_page = 10
    list_max_show_all = 200

@admin.register(ProdutoAnalise)
class ProdutoAnaliseAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'codigo', 'descricao', 'descricao_df')
    list_filter = ('pedido',)

    list_per_page = 10
    list_max_show_all = 200

@admin.register(ProdutoAnaliseFoto)
class ProdutoAnaliseFotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'image')
    list_filter = ('produto',)
    list_per_page = 10
    list_max_show_all = 200

@admin.register(ProdutoStatus)
class ProdutoStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'data_status', 'status')
    list_filter = ('produto', 'data_status')

    list_per_page = 10
    list_max_show_all = 200