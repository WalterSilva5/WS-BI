from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def atalhos(request):
    return render(request, 'atalhos.html')