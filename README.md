# Projeto para Prever preço da pizza ao informar dimensão

Acessar o link https://projeto-ml-pizza.streamlit.app/

## 📌 Principais Bibliotecas

- `requests`: Para fazer requisições HTTP.
- `pandas`: Para manipulação de dados.
- `matplotlib`: Para visualização de dados.
- `seaborn`: Para gráficos estatísticos.
- `joblib`: Para salvar e carregar modelos.
- `sklearn`: Biblioteca de aprendizado de máquina.
- `streamlit`: Para criar o app web.

## 📌 Arquivos Essenciais para o Repositório

Certifique-se de que os seguintes arquivos estejam no seu repositório:

1️⃣ **`pyproject.toml`** → Define as dependências e configurações do projeto.  
2️⃣ **`poetry.lock`** → Garante que todos instalem as mesmas versões das bibliotecas.  
3️⃣ **(Opcional)** **`requirements.txt`** → Para quem quiser instalar sem Poetry.

## 🔧 Passos para Subir os Arquivos no GitHub

1️⃣ **Confirme que os arquivos estão atualizados**  
   Rode o comando:
   ```bash
   poetry lock  # Garante que poetry.lock está atualizado

2️⃣ Adicione os arquivos ao Git
Use os comandos:
git add pyproject.toml poetry.lock
git commit -m "Adicionando arquivos de dependências"
git push

🏗️ Como Instalar Localmente
Agora, qualquer pessoa pode clonar seu repositório e rodar:

📌 Usando Poetry
Execute os seguintes comandos para instalar as dependências usando o Poetry:

git clone https://github.com/seu-usuario/projeto-ml.git
cd projeto-ml
poetry install

