from django.urls import path
from loja import views
urlpatterns = [
    path('', views.home, name='home'), # Cadastro de produtos, tela inicial
    
    path('listagem/', views.listagem, name='listagem_produtos'), # Listagem de produtos
    
    path('produto/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),  # Excluir produto
]
