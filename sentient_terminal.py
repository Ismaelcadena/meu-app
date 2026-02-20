import streamlit as st
import time
import random

st.set_page_config(page_title="LIVE OPERATOR", layout="wide")

# ===== VISUAL =====
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
.red {color:#ff3b3b;}
.yellow {color:#ffe66d;}
</style>
""", unsafe_allow_html=True)

st.title("live operator session")

term = st.empty()
screen = ""

def render(txt):
    term.markdown(f"<pre class='cursor'>{txt}</pre>", unsafe_allow_html=True)

def type_line(line, speed=(0.01,0.05), mistakes=True):
    global screen
    typed = ""
    for c in line:
        # erro humano aleatório
        if mistakes and random.random() < 0.08:
            wrong = random.choice("abcdefghijklmnopqrstuvwxyz")
            typed += wrong
            render(screen + typed)
            time.sleep(random.uniform(0.02,0.08))

            # apagar
            for _ in range(random.randint(1,2)):
                typed = typed[:-1]
                render(screen + typed)
                time.sleep(0.03)

        typed += c
        render(screen + typed)
        time.sleep(random.uniform(*speed))

    screen += typed + "\n"
    render(screen)

def thinking():
    dots = ""
    for _ in range(random.randint(2,5)):
        dots += "."
        render(screen + dots)
        time.sleep(0.3)
    render(screen)

# ===== SCRIPT =====
script = [
"ssh root@172.16.0.12",
"password: ********",
"access granted",
"",
"scanning subnet",
"found 12 hosts",
"probing target 172.16.0.7",
"",
"deploy exploit",
"waiting response",
"",
"override authentication",
"inject payload",
"extract database",
"",
"clean logs",
"exit"
]

for line in script:
    type_line("> " + line)
    if random.random() < 0.6:
        thinking()

st.markdown("<h3 style='color:#00ff88'>session terminated</h3>", unsafe_allow_html=True)
