from datetime import timedelta, datetime

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

STATUS_PRODUTO = [('recebido','Recebido'),('pedido_em_edição','Pedido em Edição'),('em_analise','Em analise'), ('aguardando_transporte','aguardando transporte')]

class PedidoAnalise(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    filial = models.CharField('Código/Nome Filial', max_length=200)
    nome_cliente = models.CharField('Nome do cliente', max_length=200)
    telefone = models.CharField('Telefone', max_length=15)
    email = models.EmailField('E-mail', blank=True, null=True)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=15, blank=True, null=True)
    doc_fiscal = models.CharField('Número NFe/CFe', max_length=10, blank=True, null=True)
    data_entrada = models.DateTimeField('Data Entrada', auto_now=True)
    data_max_resp = models.DateTimeField('Data Máxima de Resposta')
    data_max_retorno = models.DateTimeField('Data Máxima Para Retorno')
    

    def save(self, *args, **kwargs):
        if self.id is None:
            data_atual = datetime.now()
            self.data_max_resp = data_atual + timedelta(days=15)
            self.data_max_retorno = data_atual + timedelta(days=30)

    
        super(PedidoAnalise, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.id}'  
    

class ProdutoAnalise(models.Model):
    pedido = models.ForeignKey(PedidoAnalise, on_delete = models.CASCADE)
    codigo = models.CharField('Codigo Produto Completo', max_length=15)
    descricao = models.CharField('Descrição Produto', max_length=120)
    descricao_df = models.TextField('Descrição do Defeito')

    def __str__(self):
        return f'{self.codigo} - {self.descricao}'
    
    def save(self, *args, **kwargs):
        if self.id is None:
           data_atual = datetime.now()
           produto_status = ProdutoStatus(
               user = self.pedido.user,
               data_status = data_atual,
               status = 'pedido_em_edição',
               produto = self
               )
            
        super(ProdutoAnalise, self).save(*args, **kwargs)


class ProdutoAnaliseFoto(models.Model):
    produto = models.ForeignKey(ProdutoAnalise, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='produto/imagens')

    def __str__(self):
        return f'{self.produto}' 

class ProdutoStatus(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    produto = models.ForeignKey(ProdutoAnalise, on_delete = models.CASCADE)
    data_status = models.DateTimeField('Data',auto_now=True)
    status = models.CharField('Status', choices=STATUS_PRODUTO, default='aguardando_transporte', max_length=30)

    def __str__(self):
        return f'{self.produto} - {self.data_status} - {self.status}' 
    
    class Meta:
        verbose_name_plural = "Produto status"


    """
        desenhar status depois que estiver na fabrica
        filial - funcionario que recebeu
        status: (recebido, em analise, (Produto não localizado,realizado_conserto, sem conserto,
        autorizado_credito, Devolução sem conserto, aguardando_retornar_loja, em_transporte_loja),
        recebido loja, credito_efetivado, entregue_cliente))
    """