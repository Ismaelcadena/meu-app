import streamlit as st
import time
import random
from datetime import datetime

st.set_page_config(page_title="SYSTEM BOOT", layout="wide")

# ===== VISUAL =====
st.markdown("""
<style>
.stApp {
    background-color: black;
    color: #00ff9c;
    font-family: Consolas, monospace;
}
.big {
    font-size: 32px;
    text-shadow: 0 0 12px #00ff9c;
}
</style>
""", unsafe_allow_html=True)

title = st.empty()
log = st.empty()
bar = st.progress(0)

# ===== BOOT =====
title.markdown("<div class='big'>BOOTING SYSTEM...</div>", unsafe_allow_html=True)

logs = [
    "loading kernel modules",
    "starting neural engine",
    "connecting to remote node",
    "decrypting packets",
    "initializing security layer",
    "checking memory sectors",
    "mounting virtual drives",
    "establishing encrypted tunnel",
    "synchronizing time server",
    "accessing mainframe"
]

texto = ""
for i in range(100):
    time.sleep(0.03)
    bar.progress(i + 1)
    texto += random.choice(logs) + "<br>"
    log.markdown(texto, unsafe_allow_html=True)

# ===== ACESSO =====
time.sleep(0.5)
title.markdown("<div class='big'>ACCESS GRANTED</div>", unsafe_allow_html=True)

st.success("welcome back, operator")

st.write("session:", hex(random.randint(10**7, 10**9)))
st.write("ip:", f"192.168.{random.randint(0,255)}.{random.randint(0,255)}")
st.write("time:", datetime.now().strftime("%H:%M:%S"))
