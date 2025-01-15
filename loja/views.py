from django.shortcuts import render, redirect 
from django.shortcuts import get_object_or_404, redirect
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
            # Aparece esse aviso ao cadastrar um produto com sucesso
            return render(request, 'produtos/home.html', {'message': 'Produto cadastrado com sucesso!'})

    # Se não for um POST, renderiza o formulário vazio
    return render(request, 'produtos/home.html')

def listagem(request):
    # Obtém todos os produtos cadastrados no banco de dados
    produtos = {
        'produtos' : Produto.objects.all()
    }
    # O render() serve para processar um template HTML diretamente e retornar a resposta
    return render(request, 'produtos/listagem.html', produtos)

def excluir_produto(request, id):
    # Busca o produto pelo ID ou retorna um erro 404 se não for encontrado
    produto = get_object_or_404(Produto, id_produto=id)
    
    # Exclui o produto do banco de dados
    produto.delete()
    
    # Renderiza a página de listagem com uma mensagem de sucesso
    produtos = {
        'produtos': Produto.objects.all(),
        'message': f'O produto "{produto.nome}" foi excluído com sucesso!'
    }
    return render(request, 'produtos/listagem.html', produtos)

def editar_produto(request, id):
    # Recupera o produto pelo ID
    produto = get_object_or_404(Produto, id_produto=id)
    mensagem = None 
    if request.method == 'POST':
        # Atualiza os dados do produto com base no formulário enviado
        produto.nome = request.POST.get('nome_produto')
        produto.preco = request.POST.get('preco_produto')
        produto.quantidade_estoque = request.POST.get('qtd_estoque')
        
        # Salva as alterações no banco de dados
        produto.save()
        
        # Redireciona para a página inicial com mensagem de sucesso
        # Define a mensagem de sucesso
        mensagem = "Produto atualizado com sucesso!"
    
    # Renderiza a página de edição, passando os dados do produto e a mensagem
    return render(request, 'produtos/editar_produto.html', {'produto': produto, 'mensagem': mensagem})
    