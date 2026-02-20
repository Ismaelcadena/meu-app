import streamlit as st
import random

st.set_page_config(page_title="Sistema Confidencial", layout="centered")

st.title("🔒 Sistema protegido")
st.write("Somente amigos verdadeiros conseguem acessar.")

if "acesso" not in st.session_state:
    st.session_state.acesso = False

senha = st.text_input("Digite o código secreto:", type="password")

if st.button("validar"):
    if senha.lower() in ["parceiro", "tmj", "irmao", "amigo"]:
        st.session_state.acesso = True
    else:
        st.error("código incorreto ❌")

if st.session_state.acesso:
    st.success("acesso liberado ✅")
    st.divider()

    mensagens = [
        "valeu por sempre estar do meu lado.",
        "amizade assim é raridade.",
        "conta comigo pra qualquer coisa.",
        "tu é parceiro de verdade.",
        "respeito máximo sempre 🤝"
    ]

    st.write(random.choice(mensagens))
    st.balloons()
