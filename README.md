# CRUD de Produtos em Django

Um sistema simples de gerenciamento de produtos (CRUD) desenvolvido com Django e Python, permitindo cadastrar, listar, editar e excluir produtos de forma prática e funcional.

## 🚀 Funcionalidades

- **Cadastro de Produtos:** Adicione novos produtos com nome, preço e quantidade em estoque.  
- **Listagem de Produtos:** Visualize todos os produtos cadastrados com busca e filtros (por nome ou preço).  
- **Edição de Produtos:** Atualize informações de qualquer produto por meio de um formulário.  
- **Exclusão de Produtos:** Remova produtos com confirmação do usuário.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Django, Python 3.11.9  
- **Frontend:** Bootstrap, HTML e CSS personalizados  
- **Banco de Dados:** SQLite (padrão do Django)

## 📦 Como Instalar e Executar o Projeto

1. **Clone o repositório:**

   - git clone https://github.com/ArthurLBSilva/crud_produtos.git
   - cd crud_produtos
   
2. **Crie e ative um ambiente virtual**
   
    - No Windows:
    -  python -m venv .venv
    - .\Scripts\activate

4. **Instale a dependencia**

   • pip install django

5. **Aplique as migrações do banco de dados**
   
   • python manage.py migrate

6. **Execute o servidor**
 
   • python manage.py runserver
   
7. **Acesse a aplicação no navegador pelo link: http://127.0.0.1:8000/**

## 📁 Estrutura do Projeto

- **crud_produtos/**
Diretório principal contendo configurações e estrutura do projeto Django. 

- **loja/**
Aplicação principal onde estão as views, models e templates.

- **templates/**
Diretório com os arquivos HTML para renderização das páginas.

- **static/**
Arquivos de estilo (CSS) e outros recursos estáticos.

## 🗃️ Banco de Dados 
   - O projeto utiliza o banco de dados SQLite. 
   - O banco já está configurado e não é necessário criar um novo. 
   - Caso deseje resetar, use o comando: python manage.py flush

## ⚠️ Observações 

 - Não há testes automatizados implementados. 
 - Nenhuma licença foi atribuída ao projeto. 
 - Se precisar de ajustes ou informações adicionais, avise!

