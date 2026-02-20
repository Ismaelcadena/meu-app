import streamlit as st
import time
import random

st.set_page_config(page_title="SYSTEM TERMINAL", layout="wide")

# ====== CSS HACKER ======
st.markdown("""
<style>
body {
    background-color: black;
}
.stApp {
    background-color: black;
    color: #00ff9c;
    font-family: Consolas, monospace;
}
h1, h2, h3, h4 {
    color: #00ff9c;
    text-shadow: 0 0 10px #00ff9c;
}
div[data-testid="stSidebar"] {
    background-color: #050505;
    border-right: 1px solid #00ff9c;
}
.stButton>button {
    background-color: black;
    color: #00ff9c;
    border: 1px solid #00ff9c;
}
</style>
""", unsafe_allow_html=True)

# ====== HEADER ======
st.title("◤ ACCESS TERMINL ◢")
st.caption("secure connection established")

# ====== FAKE SCAN ======
st.subheader("network scan")

progress = st.progress(0)
status = st.empty()

for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)
    status.text(f"scanning ports... {i+1}%")

status.text("scan complete ✓")

# ====== RANDOM DATA ======
st.subheader("live packets")

for _ in range(15):
    ip = f"{random.randint(10,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    port = random.randint(20,9000)
    st.text(f"connected -> {ip}:{port}")

# ====== TERMINAL INPUT ======
st.subheader("command")

cmd = st.text_input("enter command")

if cmd:
    if cmd.lower() == "access":
        st.success("access granted")
    elif cmd.lower() == "root":
        st.error("permission denied")
    else:
        st.write("command not recognized")
