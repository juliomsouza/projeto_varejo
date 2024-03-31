from django.db import models
from datetime import timedelta, datetime


STATUS_PRODUTO = [('recebido','Recebido'),('em_analise','Em analise'), ('aguardando_transporte','aguardando transporte')]

class PedidoAnalise(models.Model):
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
    

class ProdutoAnalise(models.Model):
    pedido = models.ForeignKey(PedidoAnalise, on_delete = models.CASCADE)
    codigo = models.CharField('Codigo Produto Completo', max_length=15)
    descricao = models.CharField('Descrição Produto', max_length=120)
    descricao_df = models.TextField('Descrição do Defeito')

    def __str__(self):
        return f'{self.codigo} - {self.descricao}' 


class ProdutoAnaliseFoto(models.Model):
    produto = models.ForeignKey(ProdutoAnalise, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='produto/imagens')

    def __str__(self):
        return f'{self.produto}' 

class ProdutoStatus(models.Model):
    produto = models.ForeignKey(ProdutoAnalise, on_delete = models.CASCADE)
    data_status = models.DateTimeField('Data',auto_now=True)
    status = models.CharField('Status', choices=STATUS_PRODUTO, default='aguardando_transporte', max_length=30)

    def __str__(self):
        return f'{self.produto} - {self.data_status} - {self.status}' 
    
    class Meta:
        verbose_name_plural = "Produto status"


    """
    pedido 
        cliente: Nome, celular , e-mail, cpf , NFe
    produtos: cod_produto, tipo:() cor:  tamanho: descricao do(s) defeito(s)
    data_entrada - previsao_entrega_cliente - previsão_reposta 10 ou 15 antes de estourar o prazo de 30 dias
    filial - funcionario que recebeu
    status: (recebido, em analise, (Produto não localizado,realizado_conserto, sem conserto),
         (aguardando transporte, liberado credito))
"""