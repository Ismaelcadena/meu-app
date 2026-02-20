import streamlit as st
import random
import time

st.set_page_config(page_title="Heart Chat", layout="centered")

# ===== ESTILO =====
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at center, #1a001f, #000000);
    color: #ff9de2;
    font-family: monospace;
}
.chat {
    background-color: rgba(255,255,255,0.05);
    padding: 12px;
    border-radius: 12px;
    margin: 8px 0;
}
.user {
    color: #ffffff;
}
.bot {
    color: #ff7ad9;
    text-shadow: 0 0 8px #ff4dc4;
}
</style>
""", unsafe_allow_html=True)

st.title("💗 Heart Online")
st.caption("status: typing...")

# memória da conversa
if "chat" not in st.session_state:
    st.session_state.chat = []

# respostas fofas
responses = [
    "eu tava esperando você aparecer 🫶",
    "você chegou e meu código rodou perfeito",
    "meu sistema detectou saudade",
    "você é tipo wifi… quando some eu paro de funcionar",
    "buguei quando você falou isso",
    "processando carinho...",
    "meu coração deu upload em você",
    "conexão estável agora 💞",
    "isso foi fofo demais pra um humano",
    "salvei essa mensagem nos favoritos"
]

# mostrar histórico
for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f"<div class='chat user'>você: {msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat bot'>coração: {msg}</div>", unsafe_allow_html=True)

# input
user_input = st.text_input("digite algo...")

if user_input:
    st.session_state.chat.append(("user", user_input))
    time.sleep(0.4)
    reply = random.choice(responses)
    st.session_state.chat.append(("bot", reply))
    st.rerun()
