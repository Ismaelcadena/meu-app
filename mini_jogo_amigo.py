import streamlit as st
import random
import time

st.set_page_config(page_title="Missão: Amizade", layout="centered")

st.title("🎯 Missão: Provar que é meu amigo")
st.write("Você tem 5 segundos pra clicar no botão certo 😈")

if "start_time" not in st.session_state:
    st.session_state.start_time = None

if "numero_certo" not in st.session_state:
    st.session_state.numero_certo = random.randint(1, 5)

if "fim" not in st.session_state:
    st.session_state.fim = False

# iniciar jogo
if st.button("COMEÇAR"):
    st.session_state.start_time = time.time()
    st.session_state.numero_certo = random.randint(1, 5)
    st.session_state.fim = False

if st.session_state.start_time and not st.session_state.fim:

    col1, col2, col3, col4, col5 = st.columns(5)

    botoes = []
    with col1:
        botoes.append(st.button("1"))
    with col2:
        botoes.append(st.button("2"))
    with col3:
        botoes.append(st.button("3"))
    with col4:
        botoes.append(st.button("4"))
    with col5:
        botoes.append(st.button("5"))

    tempo_passado = time.time() - st.session_state.start_time

    if tempo_passado > 5:
        st.error("tempo esgotado 😭 tenta de novo")
        st.session_state.fim = True

    for i, clicado in enumerate(botoes, start=1):
        if clicado and not st.session_state.fim:
            if i == st.session_state.numero_certo:
                st.success("ACERTOU! amizade lendária desbloqueada 🤝🔥")
                st.balloons()
            else:
                st.error("errou 😅 mas ainda é meu parceiro")
            st.session_state.fim = True
