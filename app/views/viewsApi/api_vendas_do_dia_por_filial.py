from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def api_vendas_do_dia_por_filial(request):   

    data = {'filial1': 100512, 'filial2': 80252}
    data = JsonResponse(data)
    data["Access-Control-Allow-Origin"] = "*"
    data["Access-Control-Allow-Methods"] = "GET, OPTIONS, POST"
    data["Access-Control-Max-Age"] = "1000"
    data["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"

    return data

