from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse


def api_vendas_do_dia_por_vendedor(request):
    data =  {'vendas': buscarVendas()}
    
    return JsonResponse(data)


def buscarVendas():
    return [['teste1', 15512],
            ['teste2', 512312]]
