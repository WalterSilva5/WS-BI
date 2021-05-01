from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def ferramentas(request):
    return render(request, 'ferramentas.html')