# Projeto para Prever preço da pizza ao informar dimensão

Acessar o link https://projeto-ml-pizza.streamlit.app/

📌 Principais bibliotecas para importar no app.py

requests                  # Para fazer requisições HTTP
pandas                    # Para manipulação de dados
matplotlib                # Para visualização de dados
seaborn                   # Gráficos estatísticos
joblib                    # Para salvar e carregar modelos
sklearn                   # Biblioteca de aprendizado de máquina
streamlit                 # Para criar o app web

📌 Arquivos essenciais para o repositório
Certifique-se de que estes arquivos estão no GitHub:

1️⃣ pyproject.toml → Define as dependências e configurações do projeto.
2️⃣ poetry.lock → Garante que todos instalem as mesmas versões das bibliotecas.
3️⃣ (Opcional) requirements.txt → Para quem quiser instalar sem Poetry.

🔧 Passos para subir os arquivos no GitHub

1️⃣ Confirme que os arquivos estão atualizados
poetry lock  # Garante que poetry.lock está atualizado

2️⃣ Adicione os arquivos ao Git
git add pyproject.toml poetry.lock
git commit -m "Adicionando arquivos de dependências"
git push

🏗️ Como instalar localmente
Agora, qualquer pessoa pode clonar seu repositório e rodar:

📌 Usando Poetry
git clone https://github.com/seu-usuario/projeto-ml.git
cd projeto-ml
poetry install
📌 Alternativa: Criar um requirements.txt (para quem usa pip)
Se quiser facilitar a instalação para quem não usa poetry, gere um requirements.txt:
poetry export -f requirements.txt --output requirements.txt
git add requirements.txt
git commit -m "Adicionando requirements.txt para instalação via pip"
git push

Agora, quem quiser instalar sem Poetry pode rodar:
pip install -r requirements.txt
