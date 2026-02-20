import streamlit as st
import time

st.set_page_config(page_title="Uma surpresa pra você 💝", layout="centered")

# ===== ESTILO =====
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #140014, #2a0033, #000000);
    color: #ffd9f7;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
}
.card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 18px;
    margin-top: 20px;
    box-shadow: 0 0 25px rgba(255,105,180,0.3);
}
</style>
""", unsafe_allow_html=True)

st.title("Ei... clica aqui primeiro 👇")

# memória de etapas
if "step" not in st.session_state:
    st.session_state.step = 0

# ===== BOTÃO AVANÇAR =====
if st.button("abrir 💌"):
    st.session_state.step += 1

st.write("")

# ===== ETAPAS =====
if st.session_state.step >= 1:
    st.markdown("<div class='card'>Eu preparei isso porque você é muito especial pra mim.</div>", unsafe_allow_html=True)

if st.session_state.step >= 2:
    st.markdown("<div class='card'>Nem sempre eu falo, mas eu sou muito grato(a) por tudo que você faz.</div>", unsafe_allow_html=True)

if st.session_state.step >= 3:
    st.markdown("<div class='card'>Você esteve comigo em momentos que ninguém mais estava.</div>", unsafe_allow_html=True)

if st.session_state.step >= 4:
    st.markdown("<div class='card'>Me ajudou, me ouviu e me apoiou mais do que imagina.</div>", unsafe_allow_html=True)

if st.session_state.step >= 5:
    st.markdown("<div class='card'>Eu tenho muita sorte de ter você como irmã.</div>", unsafe_allow_html=True)

if st.session_state.step >= 6:
    st.balloons()
    st.markdown("<h2>Te amo muito 💖</h2>", unsafe_allow_html=True)
