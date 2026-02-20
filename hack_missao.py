import streamlit as st
import random
import string
import time

st.set_page_config(page_title="Hack Mission", layout="wide")

# ===== ESTILO HACKER =====
st.markdown("""
<style>
.stApp {
    background-color: black;
    color: #00ff88;
    font-family: Consolas, monospace;
}
h1, h2, h3 {
    color: #00ff88;
    text-shadow: 0 0 10px #00ff88;
}
.block {
    background: rgba(0,255,120,0.05);
    padding: 20px;
    border-radius: 10px;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("☠ MISSÃO: INVADIR SISTEMA ☠")
st.write("decodifique a senha antes do tempo acabar...")

# ===== GERAR CÓDIGO =====
if "senha" not in st.session_state:
    st.session_state.senha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

if "start" not in st.session_state:
    st.session_state.start = None

if "fim" not in st.session_state:
    st.session_state.fim = False

if st.button("INICIAR ATAQUE"):
    st.session_state.senha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    st.session_state.start = time.time()
    st.session_state.fim = False

# ===== JOGO =====
if st.session_state.start and not st.session_state.fim:

    tempo = time.time() - st.session_state.start
    restante = 10 - int(tempo)

    if restante <= 0:
        st.error("💀 sistema bloqueado")
        st.session_state.fim = True
    else:
        st.markdown(f"### ⏳ tempo restante: {restante}s")

        tentativa = st.text_input("Digite a senha (4 caracteres):").upper()

        if tentativa == st.session_state.senha:
            st.success("🔥 ACESSO CONCEDIDO 🔥")
            st.balloons()
            st.markdown("### bem-vindo ao sistema, hacker.")
            st.session_state.fim = True

        else:
            st.markdown("`acesso negado...`")

    # dica pequena
    st.markdown(f"<div class='block'>DICA: começa com {st.session_state.senha[0]}</div>", unsafe_allow_html=True)
