from django.shortcuts import render, redirect
from .models import Produto

def home(request):
    if request.method == 'POST':
        # Verifica se o botão de Cadastrar Produto foi clicado
        if 'cadastrar_produto' in request.POST:
            novo_produto = Produto()

            # Atribuindo os valores obtidos do formulário
            novo_produto.nome = request.POST.get('nome_produto')
            novo_produto.preco = request.POST.get('preco_produto')
            novo_produto.quantidade_estoque = request.POST.get('qtd_estoque')

            # Salvando o novo produto no banco de dados
            novo_produto.save()
            return render(request, 'produtos/home.html', {'message': 'Produto cadastrado com sucesso!'})

    # Se não for um POST, renderiza o formulário vazio
    return render(request, 'produtos/home.html')

def listagem(request):
    # Obtém todos os produtos cadastrados no banco de dados
    produtos = Produto.objects.all()

    # Renderiza a página de listagem e passa os produtos como contexto
    return render(request, 'produtos/listagem.html', {'produtos': produtos})
