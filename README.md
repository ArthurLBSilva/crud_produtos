# CRUD de Produtos em Django
Um sistema simples de gerenciamento de produtos (CRUD) desenvolvido com Django e Python, permitindo cadastrar, listar, editar e excluir produtos de forma prática e funcional.

🚀 Funcionalidades
Cadastro de Produtos: Adicione novos produtos com nome, preço e quantidade em estoque.
Listagem de Produtos: Visualize todos os produtos cadastrados com busca e filtros (por nome ou preço).
Edição de Produtos: Atualize informações de qualquer produto por meio de um formulário.
Exclusão de Produtos: Remova produtos com confirmação do usuário.
🛠️ Tecnologias Utilizadas
Backend: Django 4.x, Python 3.11.9
Frontend: Bootstrap, HTML e CSS personalizados
Banco de Dados: SQLite (padrão do Django)
📦 Como Instalar e Executar o Projeto
Clone o repositório

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie e ative um ambiente virtual

No Windows:
bash
Copiar código
python -m venv .venv
.\Scripts\activate
Instale as dependências

bash
Copiar código
pip install -r requirements.txt
Aplique as migrações do banco de dados

bash
Copiar código
python manage.py migrate
Execute o servidor

bash
Copiar código
python manage.py runserver
Acesse a aplicação no navegador pelo link: http://127.0.0.1:8000/

📁 Estrutura do Projeto
crud_produtos/
Diretório principal contendo configurações e estrutura do projeto Django.
loja/
Aplicação principal onde estão as views, models e templates.
templates/
Diretório com os arquivos HTML para renderização das páginas.
static/
Arquivos de estilo (CSS) e outros recursos estáticos.
🗃️ Banco de Dados
O projeto utiliza o banco de dados SQLite.
O banco já está configurado e não é necessário criar um novo. Caso deseje resetar, use o comando:

bash
Copiar código
python manage.py flush
🖼️ Imagens do Projeto (Opcional)
Se desejar, inclua screenshots da interface principal e funcionalidades do sistema.

⚠️ Observações
Não há testes automatizados implementados.
Nenhuma licença foi atribuída ao projeto.
Se precisar de ajustes ou informações adicionais, avise!
