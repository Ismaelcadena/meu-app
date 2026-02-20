import streamlit as st
import time
import random

st.set_page_config(page_title="REMOTE TERMINAL", layout="wide")

# ===== ESTILO =====
st.markdown("""
<style>
.stApp {
    background-color: black;
    color: #00ff88;
    font-family: Consolas, monospace;
}
.cursor {
    border-right: 3px solid #00ff88;
    animation: blink 1s infinite;
}
@keyframes blink {
    0% {border-color:#00ff88;}
    50% {border-color:transparent;}
    100% {border-color:#00ff88;}
}
</style>
""", unsafe_allow_html=True)

st.title("remote terminal connected")

terminal = st.empty()

commands = [
"ssh root@192.168.0.1",
"entering password ********",
"access granted",
"scanning network...",
"locating targets...",
"bypassing firewall...",
"injecting payload...",
"extracting database...",
"downloading packets...",
"cleaning logs...",
"disconnecting trace..."
]

text = ""

def type_writer(line):
    global text
    for c in line:
        text += c
        terminal.markdown(f"<pre class='cursor'>{text}</pre>", unsafe_allow_html=True)
        time.sleep(random.uniform(0.01, 0.05))
    text += "\n"

for cmd in commands:
    type_writer("> " + cmd)
    time.sleep(random.uniform(0.2, 0.7))

st.success("operation completed ☠")
