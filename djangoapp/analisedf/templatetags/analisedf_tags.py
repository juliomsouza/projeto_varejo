from django import template

register = template.Library()


@register.filter(name='status_ped')
def status_prod(status, pedido_id):
    return status.get(pedido_id) 