import streamlit as st
import time

st.set_page_config(page_title="Para Minha Irmã 💖", layout="centered")

# ===== ESTILO DELICADO =====
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #1a001f, #330033, #000000);
    color: #ffd6f5;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
}
.big {
    font-size: 60px;
    text-shadow: 0 0 20px #ff66cc;
}
.texto {
    font-size: 20px;
    line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big'>💗</div>", unsafe_allow_html=True)
st.title("Para Minha Irmã")

st.divider()

mensagem = """
Eu só queria que você soubesse o quanto você é importante pra mim.

Obrigada por estar comigo nos dias bons,
e principalmente nos dias difíceis.

Obrigada por cada conselho,
cada risada,
cada apoio silencioso que você me deu.

Se hoje eu sou mais forte,
é porque eu tive você ao meu lado.

Você não é só minha irmã.
Você é minha base, minha amiga,
e uma das pessoas que eu mais amo nesse mundo. 💖
"""

placeholder = st.empty()

texto_animado = ""
for letra in mensagem:
    texto_animado += letra
    placeholder.markdown(f"<div class='texto'>{texto_animado}</div>", unsafe_allow_html=True)
    time.sleep(0.02)

st.divider()

st.markdown("### 💞 Com todo meu carinho")
