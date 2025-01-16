from django.urls import path
from loja import views

urlpatterns = [
    # Rota para a página inicial, onde é possível cadastrar novos produtos
    path('', views.home, name='home'),

    # Rota para exibir a lista de produtos cadastrados
    path('listagem/', views.listagem, name='listagem_produtos'),

    # Rota para excluir um produto com base no ID fornecido
    path('produto/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),

    # Rota para editar as informações de um produto específico com base no ID fornecido
    path('editar_produto/<int:id>/', views.editar_produto, name='editar_produto'),
]
