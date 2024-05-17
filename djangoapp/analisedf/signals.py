from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

from .models import ProdutoAnalise, ProdutoStatus

@receiver(post_save, sender=ProdutoAnalise)
def create_produto_status(sender,instance, created, **kwargs):
    if created:
        data_atual = datetime.now()
        produto_status = ProdutoStatus(
            user = instance.pedido.user,
            data_status = data_atual,
            status = 'pedido_em_edição',
            produto = instance
        )
        produto_status.save()
