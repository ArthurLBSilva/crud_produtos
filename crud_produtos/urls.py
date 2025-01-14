from django.urls import path
from loja import views
urlpatterns = [
    # caminho para a tela inicial
    path('', views.home, name='home'),
    # caminho para a tela de listagem
    path('listagem/', views.listagem, name='listagem_produtos')
]
