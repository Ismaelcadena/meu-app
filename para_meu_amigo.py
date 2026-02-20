import streamlit as st
import random

st.set_page_config(page_title="Pro meu parceiro 🤜🤛", layout="centered")

# ===== ESTILO =====
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #00111a, #000000);
    color: #a8e6ff;
    text-align: center;
    font-family: Consolas, monospace;
}
.card {
    background: rgba(255,255,255,0.05);
    padding: 22px;
    border-radius: 15px;
    margin-top: 20px;
    box-shadow: 0 0 20px rgba(0,200,255,0.35);
}
.big {
    font-size: 50px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big'>🤜🤛</div>", unsafe_allow_html=True)
st.title("Mensagem importante")

st.write("primeiro... aperta o botão ↓")

if "step" not in st.session_state:
    st.session_state.step = 0

if st.button("continuar"):
    st.session_state.step += 1

# ===== ETAPAS =====
if st.session_state.step >= 1:
    st.markdown("<div class='card'>Nem sempre eu falo essas coisas.</div>", unsafe_allow_html=True)

if st.session_state.step >= 2:
    st.markdown("<div class='card'>Mas você é um amigo de verdade.</div>", unsafe_allow_html=True)

if st.session_state.step >= 3:
    st.markdown("<div class='card'>Obrigado pelas risadas, pelas conversas e por estar sempre junto.</div>", unsafe_allow_html=True)

if st.session_state.step >= 4:
    st.markdown("<div class='card'>Parceiro pra momentos bons e ruins.</div>", unsafe_allow_html=True)

if st.session_state.step >= 5:
    frases = [
        "amizade assim não se acha todo dia",
        "tmj sempre",
        "irmão que a vida me deu",
        "conta comigo pra tudo",
        "respeito máximo"
    ]
    st.markdown(f"<div class='card'>{random.choice(frases)}</div>", unsafe_allow_html=True)

if st.session_state.step >= 6:
    st.balloons()
    st.markdown("## valeu por tudo meu irmão 💙")
