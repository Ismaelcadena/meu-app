import streamlit as st

st.set_page_config(page_title="Teste de Amizade", layout="centered")

st.title("🧠 Teste oficial de amizade")

st.write("Responde aí ↓")

score = 0

# Pergunta 1
q1 = st.radio(
    "Quem sempre aparece quando dá problema?",
    ["ninguém", "qualquer um", "tu"]
)
if q1 == "tu":
    score += 1

# Pergunta 2
q2 = st.radio(
    "Quem topa qualquer ideia aleatória?",
    ["tu", "a polícia", "minha mãe"]
)
if q2 == "tu":
    score += 1

# Pergunta 3
q3 = st.radio(
    "Quem já ouviu meus desabafos infinitos?",
    ["tu", "psicólogo", "internet"]
)
if q3 == "tu":
    score += 1

# Pergunta 4
q4 = st.radio(
    "Quem eu chamo primeiro pra contar algo?",
    ["tu", "grupo da família", "ninguém"]
)
if q4 == "tu":
    score += 1

st.divider()

if st.button("ver resultado"):
    if score >= 3:
        st.balloons()
        st.success("resultado: amigo raro desbloqueado 🤝💙")
        st.write("valeu por sempre estar comigo, de verdade.")
    else:
        st.warning("resultado inconclusivo... refaça o teste kkk")
