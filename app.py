import streamlit as st
import pandas as pd
import plotly.express as px
import database
import os

database.criar_tabela()

st.set_page_config(page_title="Controle Financeiro", page_icon="💰", layout="wide")

# ---------- SIDEBAR ----------
st.sidebar.title("💰 Financeiro")
pagina = st.sidebar.radio(
    "Navegação",
    ["📊 Dashboard", "➕ Adicionar", "📋 Histórico"]
)


                  #TELA DASHBOARD (tela principal)

dados = database.listar()
df = pd.DataFrame(dados, columns=["ID","Data","Tipo","Categoria","Valor","Descricao"])

if pagina == "📊 Dashboard":

    st.title("📊 Visão Geral")

    ganhos = df[df["Tipo"]=="Ganho"]["Valor"].sum()
    gastos = df[df["Tipo"]=="Gasto"]["Valor"].sum()
    saldo = ganhos - gastos

    c1, c2, c3 = st.columns(3)
    c1.metric("Ganhos", f"R$ {ganhos:,.2f}")
    c2.metric("Gastos", f"R$ {gastos:,.2f}")
    c3.metric("Saldo", f"R$ {saldo:,.2f}")

    st.divider()

    gastos_df = df[df["Tipo"]=="Gasto"]

    if not gastos_df.empty:
        fig = px.pie(gastos_df, names="Categoria", values="Valor", hole=0.5)
        st.plotly_chart(fig, use_container_width=True)

                
                #TELA ADICIONAR

if pagina == "➕ Adicionar":

    st.title("➕ Nova movimentação")

    col1, col2, col3 = st.columns(3)

    with col1:
        tipo = st.selectbox("Tipo", ["Ganho", "Gasto"])

    with col2:
        valor = st.number_input("Valor", min_value=0.0, format="%.2f")

    with col3:
        categoria = st.text_input("Categoria")

    descricao = st.text_input("Descrição")

    if st.button("Salvar"):
        database.adicionar(tipo, valor, categoria, descricao)
        st.success("Movimentação salva!")
        st.rerun()




            #TELA HISTÓRICO

if pagina == "📋 Histórico":

    st.title("📋 Histórico de movimentações")

    st.dataframe(df, use_container_width=True)

    st.divider()

    if st.button("🗑️ Resetar banco"):
        if os.path.exists("financeiro.db"):
            os.remove("financeiro.db")
        database.criar_tabela()
        st.warning("Banco resetado!")
        st.rerun()

















# cria banco
database.criar_tabela()

st.set_page_config(page_title="Controle Financeiro", page_icon="💰", layout="wide")

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
    database.adicionar(tipo, valor, categoria, descricao)
    st.success("Movimentação salva!")
    st.rerun()

# ------------------ DADOS DO BANCO ------------------
dados = database.listar()

df = pd.DataFrame(dados, columns=[
    "ID", "Data", "Tipo", "Categoria", "Valor", "Descricao"
])

# ------------------ CALCULOS (AGORA CORRETO) ------------------
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

gastos_df = df[df["Tipo"] == "Gasto"]

if not gastos_df.empty:
    fig = px.pie(
        gastos_df,
        names="Categoria",
        values="Valor",
        hole=0.45
    )

    fig.update_traces(textinfo="percent+label")
    fig.update_layout(title="Distribuição dos gastos")

    st.plotly_chart(fig, use_container_width=True)

# ------------------ TABELA ------------------
st.subheader("Histórico")
st.dataframe(df, use_container_width=True)

# ------------------ RESET ------------------
st.divider()

if st.button("🗑️ Resetar banco"):
    if os.path.exists("financeiro.db"):
        os.remove("financeiro.db")
    database.criar_tabela()
    st.warning("Banco resetado!")
    st.rerun()