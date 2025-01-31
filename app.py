import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib  # Para salvar e carregar o modelo
from sklearn.linear_model import LinearRegression
from sklearn.exceptions import NotFittedError

# Função para carregar os dados
@st.cache_data
def carregar_dados(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error("O arquivo pizzas.csv não foi encontrado. Certifique-se de que ele está na mesma pasta do aplicativo.")
        st.stop()

# Função para treinar o modelo e salvar
@st.cache_resource
def treinar_modelo(df):
    modelo = LinearRegression()
    x = df[["diametro"]]
    y = df[["preco"]]
    modelo.fit(x, y)
    joblib.dump(modelo, "modelo_pizza.pkl")  # Salva o modelo em disco
    return modelo

# Função para carregar o modelo
def carregar_modelo(file_path="modelo_pizza.pkl"):
    try:
        modelo = joblib.load(file_path)
        return modelo
    except (FileNotFoundError, NotFittedError):
        st.error("O modelo não foi treinado ainda. Por favor, verifique os dados.")
        st.stop()

# Carregar os dados
df = carregar_dados("pizzas.csv")

# Treinar o modelo ou carregar o modelo salvo
modelo = treinar_modelo(df) if "modelo_pizza.pkl" not in st.session_state else carregar_modelo()

# Configuração da aplicação
st.title("Prevendo o Valor de uma Pizza 🍕")
st.divider()

# Visualizar os dados
if st.checkbox("Mostrar dados de treino"):
    st.write("### Dados Carregados")
    st.dataframe(df)

# Visualizar relação entre diâmetro e preço
if st.checkbox("Mostrar gráfico de relação"):
    st.write("### Gráfico: Preço vs Diâmetro")
    fig, ax = plt.subplots()
    ax.scatter(df["diametro"], df["preco"], color="blue", label="Dados reais")
    ax.plot(df["diametro"], modelo.predict(df[["diametro"]]), color="red", label="Modelo Linear")
    ax.set_xlabel("Diâmetro da Pizza (cm)")
    ax.set_ylabel("Preço (R$)")
    ax.set_title("Relação entre Diâmetro e Preço")
    ax.legend()
    st.pyplot(fig)

# Entrada do usuário para prever o preço
diametro = st.number_input("Digite o tamanho da pizza (em cm):", step=1)

if diametro > 0:  # Apenas se o valor for positivo
    try:
        preco_previsto = modelo.predict([[diametro]])[0][0]
        st.success(f"O valor da pizza com o diâmetro de {diametro:.2f} cm é de **R${preco_previsto:.2f}**.")
        #st.balloons()  # Exibir os balões somente após a previsão
    except Exception as e:
        st.error(f"Erro ao prever o preço: {e}")
elif diametro == 0:
    st.info("Por favor, insira um diâmetro maior que 0 para calcular o preço.")
