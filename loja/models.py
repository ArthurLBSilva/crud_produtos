from django.db import models
from django.core.validators import MinValueValidator

# Criação da tabela
class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)  # Definindo id_produto como chave primária
    #Mesmo tendo esse maximo ele não aponta erro na hora de salvar no banco
    nome = models.CharField(max_length=100)
    # O preço tem que ser minimamente maior que 0.01
    preco = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0.01)])
    # O minimo do estoque é 0, menos que isso não pode
    quantidade_estoque = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    # É salvo a data automaticamente ao ser criado
    data_criacao = models.DateTimeField(auto_now_add=True) 
