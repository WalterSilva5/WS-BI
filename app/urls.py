from django.urls import path


# views
from .views.viewTelas import *
from .views.viewApi import *

urlpatterns = [

    path('', index, name='index'),
    # relatorios
    path('relatorios', relatorios, name='relatorios'),
    path('relatorios/vendas_por_vendedor', relatorios_vendas_por_vendedor, name='relatorios_vendas_por_vendedor'),

    path('alertas', alertas, name='alertas'),
    path('ferramentas', ferramentas, name='ferramentas'),
    path('atalhos', atalhos, name='atalhos'),

    # index
    path('api/api_vendas_do_dia_por_vendedor',
         api_vendas_do_dia_por_vendedor, name="api_vendas_do_dia_por_vendedor"),
    path('api/api_vendas_do_dia_por_filial', api_vendas_do_dia_por_filial,
         name="api_vendas_do_dia_por_filial"),



]
