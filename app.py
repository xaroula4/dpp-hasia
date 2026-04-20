import streamlit as st
import pandas as pd
import numpy as np

# Ρύθμιση Σελίδας
st.set_page_config(page_title="Hasia Beans DPP", page_icon="🌱", layout="wide")

# CSS ΓΙΑ MOBILE LOOK & ΣΤΑΘΕΡΟ LAYOUT
st.markdown("""
    <style>
    .main { background-color: #f8f9f5; }
    .stApp { max-width: 500px; margin: 0 auto; background: white; padding: 10px; border-radius: 20px; }
    .header-style { background-color: #2e7d32; color: white; padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 15px; }
    .section-header { background-color: #1b5e20; color: white; padding: 8px 15px; border-radius: 10px; margin-top: 15px; font-weight: bold; }
    .info-card { background-color: #ffffff; padding: 12px; border-radius: 10px; border: 1px solid #eee; margin-top: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .stats-container { display: flex; justify-content: space-around; gap: 5px; margin-top: 10px; }
    .stat-card { background: white; border: 1px solid #e0e0e0; border-radius: 12px; padding: 10px; text-align: center; flex: 1; min-width: 90px; }
    .stat-icon { font-size: 20px; display: block; margin-bottom: 5px; }
    .stat-label { font-size: 11px; color: #666; display: block; }
    .stat-value { font-size: 13px; font-weight: bold; color: #1b5e20; display: block; }
    .stButton>button { background-color: #2e7d32; color: white; border-radius: 20px; width: 100%; font-weight: bold; height: 45px; }
    </style>
    """, unsafe_allow_html=True)

# --- ΔΕΔΟΜΕΝΑ ΠΡΟΪΟΝΤΩΝ (ΕΝΗΜΕΡΩΜΕΝΑ) ---
products = {
    "Φακή Χασίων": {
        "id": "#OX-01-066",
        "origin": "Καρπερό, Γρεβενά",
        "area": "Αγροτεμάχιο 'Κάμπος'",
        "date": "Ιούλιος 2025",
        "type": "Βιολογική",
        "drone_date": "05 Ιουνίου 2025",
        "drone_flights": "3 επιτυχείς",
        "hum": "22%",
        "temp": "31°C",
        "lat": 39.941, "lon": 21.632
    },
    "Φασόλια Γίγαντες": {
        "id": "#OX-01-070",
        "origin": "Καστοριά",
        "area": "Αγροτεμάχιο 'Παραλίμνιο'",
        "date": "Σεπτέμβριος 2025",
        "type": "Συμβατική",
        "drone_date": "12 Ιουλίου 2025",
        "drone_flights": "6 επιτυχείς",
        "hum": "28%",
        "temp": "27°C",
        "lat": 40.512, "lon": 21.261
    }
}

# 1. Header
st.markdown('<div class="header-style"><h2>🌱 Ψηφιακό Διαβατήριο</h2><p style="margin:0;">Όσπρια Χασίων | Hasia Beans</p></div>', unsafe_allow_html=True)

# 2. Επιλογή Προϊόντος
selected_prod = st.selectbox("Επιλέξτε Προϊόν:", list(products.keys()))
p = products[selected_prod]

# Quick Info
st.markdown(f"📍 **{p['origin']}** | 📦 **{selected_prod}**")
st.info(f"🆔 Διαβατήριο: {p['id']}")

# 3. Πληροφορίες Παρτίδας
st.markdown('<div class="section-header">📋 Πληροφορίες Παρτίδας</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="info-card">
    <p style="margin:2px;">• <b>Αρ. Παρτίδας:</b> {p['id']}</p>
    <p style="margin:2px;">• <b>Έκταση:</b> 250 στρέμματα</p>
    <p style="margin:2px;">• <b>Συγκομιδή:</b> {p['date']}</p>
    <p style="margin:2px;">• <b>Τοποθεσία:</b> {p['area']}</p>
    <p style="margin:2px;">• <b>Καλλιέργεια:</b> {p['type']}</p>
</div>
""", unsafe_allow_html=True)

# 4. Ψεκασμός με Drone
st.markdown('<div class="section-header">🚁 Ψεκασμός με Drone (UAV)</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="info-card" style="border-left: 5px solid #81c784;">
    <p style="margin:2px;">• <b>Τελευταίος Ψεκασμός:</b> {p['drone_date']}</p>
    <p style="margin:2px;">• <b>Σκεύασμα:</b> Οικολογικό / Εγκεκριμένο</p>
    <p style="margin:2px;">• <b>Αρ. Πτήσεων:</b> {p['drone_flights']}</p>
</div>
""", unsafe_allow_html=True)

# 5. Ανάπτυξη Καλλιέργειας
st.markdown('<div class="section-header">🌡️ Ανάπτυξη Καλλιέργειας</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="stats-container">
    <div class="stat-card">
        <span class="stat-icon">🌱</span>
        <span class="stat-label">Φάση</span>
        <span class="stat-value">Ωρίμανση</span>
    </div>
    <div class="stat-card">
        <span class="stat-icon">💧</span>
        <span class="stat-label">Υγρασία</span>
        <span class="stat-value">{p['hum']}</span>
    </div>
    <div class="stat-card">
        <span class="stat-icon">☀️</span>
        <span class="stat-label">Θερμ.</span>
        <span class="stat-value">{p['temp']}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 6. Χάρτης
st.markdown('<div class="section-header">🗺️ Χάρτης Καλλιέργειας</div>', unsafe_allow_html=True)
map_data = pd.DataFrame({'lat': [p['lat']], 'lon': [p['lon']]})
st.map(map_data)

# 7. Calculator
st.markdown('<div class="section-header">🍃 Περιβαλλοντικό Όφελος</div>', unsafe_allow_html=True)
acres = st.slider("Επιλέξτε Στρέμματα:", 1, 250, 100)
st.write(f"Μείωση πόρων: **{acres * 0.12:.2f} μονάδες**")

# 8. Button
if st.button("⭐ Book an Agrotourism Tour"):
    st.balloons()
    st.success("Registration Successful!")

st.markdown("<br><p style='text-align:center; font-size:12px; color:#999;'>Αρχική | Παρακολούθηση | Αναφορές | Προφίλ</p>", unsafe_allow_html=True)
