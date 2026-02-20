import streamlit as st
import time
import random
from datetime import datetime

st.set_page_config(page_title="OMEGA PROTOCOL", layout="wide")

# ===== VISUAL EXTREMO =====
st.markdown("""
<style>
.stApp {
    background-color: black;
    color: #00ff9c;
    font-family: Consolas, monospace;
}
.title {
    font-size: 42px;
    text-align: center;
    text-shadow: 0 0 25px #00ff9c;
}
.alert {
    color: red;
    font-weight: bold;
    text-shadow: 0 0 20px red;
}
.box {
    background: rgba(0,255,120,0.05);
    padding: 15px;
    border-radius: 10px;
    height: 300px;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>OMEGA PROTOCOL INITIALIZING</div>", unsafe_allow_html=True)

# ===== LAYOUT =====
col1, col2, col3 = st.columns(3)

log_box = col1.empty()
scan_box = col2.empty()
data_box = col3.empty()

progress = st.progress(0)

logs = [
    "injecting payload",
    "bypassing firewall",
    "spoofing identity",
    "creating backdoor",
    "decrypting database",
    "extracting credentials",
    "overriding security",
    "syncing satellite",
    "tracking operator",
    "establishing persistence"
]

def fake_ips():
    return f"{random.randint(10,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

log_text = ""
scan_text = ""
data_text = ""

for i in range(100):
    time.sleep(0.04)
    progress.progress(i+1)

    log_text += random.choice(logs) + "<br>"
    scan_text += f"port {random.randint(20,9000)} open @ {fake_ips()}<br>"
    data_text += f"packet {hex(random.randint(10000,999999))} received<br>"

    log_box.markdown(f"<div class='box'>{log_text}</div>", unsafe_allow_html=True)
    scan_box.markdown(f"<div class='box'>{scan_text}</div>", unsafe_allow_html=True)
    data_box.markdown(f"<div class='box'>{data_text}</div>", unsafe_allow_html=True)

# ===== ALERTA FINAL =====
st.markdown("<h1 class='alert'>⚠ GLOBAL BREACH DETECTED ⚠</h1>", unsafe_allow_html=True)
time.sleep(1)
st.success("ACCESS LEVEL: GOD MODE")
st.write("operator:", fake_ips())
st.write("session:", hex(random.randint(10**8, 10**10)))
st.write("timestamp:", datetime.now().strftime("%H:%M:%S"))
