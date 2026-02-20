import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

st.set_page_config(page_title="Controle Financeiro", page_icon="💰", layout="wide")

ARQUIVO = "dados.csv"

# Criar banco se não existir
if not os.path.exists(ARQUIVO):
    df = pd.DataFrame(columns=["Data", "Tipo", "Categoria", "Valor", "Descricao"])
    df.to_csv(ARQUIVO, index=False)

df = pd.read_csv(ARQUIVO)

# ------------------ TITULO ------------------
st.title("💰 Meu Controle Financeiro")

# ------------------ FORMULARIO ------------------
st.subheader("Adicionar movimentação")

col1, col2, col3 = st.columns(3)

with col1:
    tipo = st.selectbox("Tipo", ["Ganho", "Gasto"])

with col2:
    valor = st.number_input("Valor", min_value=0.0, format="%.2f")

with col3:
    categoria = st.text_input("Categoria")

descricao = st.text_input("Descrição")

if st.button("Salvar"):
    nova_linha = pd.DataFrame([{
        "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "Tipo": tipo,
        "Categoria": categoria,
        "Valor": valor,
        "Descricao": descricao
    }])

    df = pd.concat([df, nova_linha], ignore_index=True)
    df.to_csv(ARQUIVO, index=False)
    st.success("Movimentação salva!")

# ------------------ CALCULOS ------------------
ganhos = df[df["Tipo"] == "Ganho"]["Valor"].sum()
gastos = df[df["Tipo"] == "Gasto"]["Valor"].sum()
saldo = ganhos - gastos

st.subheader("Resumo")

c1, c2, c3 = st.columns(3)
c1.metric("Ganhos", f"R$ {ganhos:,.2f}")
c2.metric("Gastos", f"R$ {gastos:,.2f}")
c3.metric("Saldo", f"R$ {saldo:,.2f}")

# ------------------ GRAFICO ------------------
st.subheader("Gráfico de Gastos")

if not df.empty:
    grafico = df[df["Tipo"] == "Gasto"]
    if not grafico.empty:
        fig = px.pie(grafico, names="Categoria", values="Valor", title="Distribuição de gastos")
        st.plotly_chart(fig, use_container_width=True)

# ------------------ TABELA ------------------
st.subheader("Histórico")
st.dataframe(df, use_container_width=True)