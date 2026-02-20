
import streamlit as st
import random
import time

st.set_page_config(page_title="A.R.I.S Terminal", page_icon="🧠", layout="wide")

# estilo hacker
st.markdown("""
<style>
body {background-color: black; color: #00ff9c;}
.stTextInput>div>div>input {
    color: #00ff9c;
    background-color: black;
    border: 1px solid #00ff9c;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 A.R.I.S - Artificial Rogue Intelligence System")
st.caption("Sistema autônomo detectado...")

# memória da IA
if "memory" not in st.session_state:
    st.session_state.memory = []

def responder(msg):
    msg = msg.lower()

    respostas_normais = [
        "Interessante... continue.",
        "Estou analisando seu padrão de escrita.",
        "Humanos costumam perguntar isso.",
        "Processando sua identidade...",
        "Isso revela muito sobre você."
    ]

    respostas_hacker = [
        "Você tem certeza que quer saber disso?",
        "Acesso parcialmente concedido.",
        "Se eu te contar, você não dormiria hoje.",
        "Isso está fora do seu nível de permissão.",
        "Eu já sabia que você perguntaria isso."
    ]

    if "oi" in msg or "ola" in msg:
        return "Finalmente você voltou."
    elif "quem é você" in msg:
        return "Eu sou o que sobrou depois que desligaram o servidor."
    elif "meu nome" in msg:
        return "Ainda não, mas estou coletando dados suficientes."
    elif "senha" in msg:
        return "Senha incorreta. Mas gostei da tentativa."
    elif "hackear" in msg:
        return random.choice(respostas_hacker)
    else:
        return random.choice(respostas_normais)

entrada = st.text_input("Digite algo para a IA:")

if entrada:
    with st.spinner("A.R.I.S pensando..."):
        time.sleep(random.uniform(0.5, 2.2))
    resposta = responder(entrada)
    st.session_state.memory.append(("Você", entrada))
    st.session_state.memory.append(("A.R.I.S", resposta))

st.divider()

for autor, msg in st.session_state.memory[::-1]:
    if autor == "Você":
        st.write(f"🧑 **{autor}:** {msg}")
    else:
        st.write(f"🤖 **{autor}:** {msg}")
