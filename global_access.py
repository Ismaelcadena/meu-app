import streamlit as st
import time
import random

st.set_page_config(page_title="GLOBAL ACCESS", layout="wide")

# ===== ESTILO HACKER =====
st.markdown("""
<style>
.stApp {
    background-color: black;
    color: #00ff88;
    font-family: Consolas, monospace;
}
.big {
    font-size: 36px;
    text-align: center;
    text-shadow: 0 0 15px #00ff88;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big'>GLOBAL NETWORK ACCESS</div>", unsafe_allow_html=True)
st.write("establishing secure worldwide connections...")

bar = st.progress(0)
status = st.empty()

cities = [
    ("New York", 40.7128, -74.0060),
    ("London", 51.5072, -0.1276),
    ("Tokyo", 35.6762, 139.6503),
    ("São Paulo", -23.5505, -46.6333),
    ("Berlin", 52.5200, 13.4050),
    ("Dubai", 25.2048, 55.2708),
    ("Sydney", -33.8688, 151.2093)
]

connections = []

for i in range(100):
    time.sleep(0.03)
    bar.progress(i + 1)
    city = random.choice(cities)
    status.write(f"connecting to {city[0]} node...")
    connections.append({"lat": city[1], "lon": city[2]})

st.success("all systems online ☠")

st.map(connections)
