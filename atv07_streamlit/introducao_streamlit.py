# pip install streamlit
import streamlit as st
# pip install pandas
import pandas as pd
# python -m streamlit run introducao_streamlit.py
# (após executar o comando acima, lembre-se de pressionar Enter)

st.title("Notas 3° Etapa")

st.write("------------------------------------------------")

st.subheader("3A1")

nome = st.text_input("Digite o seu nome")

if nome:
    st.write(f"Olá, {nome}, bem-vindo.")

st.write("------------------------------------------------")

df =  pd.DataFrame({
    "disciplina": ["Python", "Matemática", "Português"],
    "nota": [5, 8, 2]
})

df

st.write("Estude mais ze por favor.")

st.write("------------------------------------------------")

selecao = st.selectbox("Selecione o que estudar:", ["Português",  "Matemática", "Python"])

st.write(f"Você selecionou: {selecao}")