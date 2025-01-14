from django.shortcuts import render
from .models import Produto

def home(request):
    return render(request, 'produtos/home.html')

def listagem(request):
    novo_produto = Produto()
    nome = request.POST.get()
    
