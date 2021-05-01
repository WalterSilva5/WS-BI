from django.db import models


class Vendedor(models.Model):
    nome = models.CharField('nome', max_length=250)
    email = models.CharField('email', max_length=250, blank="true")
    codigo = models.IntegerField('codigo')
    
class Venda_por_dia_por_vendedor(models.Model):
    data = models.DateTimeField('data')
    valor = models.FloatField('valor')
    vendedor_idvendedor = models.IntegerField('vendedor_idvendedor')