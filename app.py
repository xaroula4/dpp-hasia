import streamlit as st
import pandas as pd
import numpy as np
import os

# Ρύθμιση Σελίδας
st.set_page_config(page_title="OSPRIA HASION DPP", page_icon="🌱", layout="wide")

# CSS ΓΙΑ ΤΟ ΤΕΛΙΚΟ LOOK
st.markdown("""
    <style>
    .main { background-color: #f8f9f5; }
    .stApp { max-width: 500px; margin: 0 auto; background: white; padding: 10px; border-radius: 20px; box-shadow: 0px 0px 20px rgba(0,0,0,0.1); }
    .header-style { background-color: #2e7d32; color: white; padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 15px; }
    .section-header { background-color: #1b5e20; color: white; padding: 8px 15px; border-radius: 10px; margin-top: 15px; font-weight: bold; font-size: 14px; }
    .info-card { background-color: #ffffff; padding: 12px; border-radius: 10px; border: 1px solid #eee; margin-top: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .eco-badge { background-color: #e1f5fe; padding: 10px; border-radius: 10px; border: 1px solid #01579b; color: #01579b; font-size: 12px; font-weight: bold; text-align: center; margin: 10px 0; }
    .stat-card { background: #f1f8e9; border: 1px solid #e0e0e0; border-radius: 12px; padding: 10px; text-align: center; flex: 1; }
    .stButton>button { background-color: #2e7d32 !important; color: white !important; border-radius: 20px; width: 100%; font-weight: bold; border: none; height: 45px; }
    .bio-text { font-size: 10px; text-align: center; font-weight: bold; color: #333; margin-top: -10px; }
    </style>
    """, unsafe_allow_html=True)

# --- ΔΕΔΟΜΕΝΑ ΠΡΟΪΟΝΤΩΝ ---
products = {
    "Φακή Χασίων (Παρτίδα #OX-01)": {
        "producer": "Νικόλαος Παπαδόπουλος",
        "id": "#OX-01-066", "origin": "Καρπερό, Γρεβενά", "type": "Βιολογική",
        "date": "Ιούλιος 2025", "phase": "Ανάπτυξη", "health": "96%", 
        "img": "fakes.JPEG", "bio_img": "bio.png", "show_bio": True,
        "drone_date": "05 Ιουνίου 2025", "drone_flights": "3 επιτυχείς",
        "video": "https://www.youtube.com/watch?v=m0md-5Wzp1E",
        "recipe": "🍲 <b>Σαλάτα Beluga:</b> Βράστε για 20', προσθέστε φρέσκο κρεμμυδάκι, ντοματίνια και βαλσάμικο.",
        "eco_win": "💧 1.200L Νερό εξοικονομήθηκε",
        "lat": 39.941, "lon": 21.632
    },
    "Φασόλια Γίγαντες (Παρτίδα #KT-05)": {
        "producer": "Δημήτριος Γεωργίου",
        "id": "#KT-05-070", "origin": "Καστοριά", "type": "Συμβατική",
        "date": "Σεπτέμβριος 2025", "phase": "Ωρίμανση", "health": "98%", 
        "img": "gigantes.png", "bio_img": "bio.png", "show_bio": False,
        "drone_date": "12 Ιουλίου 2025", "drone_flights": "6 επιτυχείς",
        "video": "https://www.youtube.com/watch?v=SKGdu1x0sxo",
        "recipe": "🥘 <b>Γίγαντες στο φούρνο:</b> Με φρέσκια ντομάτα, σέλινο και πολύ μεράκι!",
        "eco_win": "🚜 -35% Λιγότερα Καύσιμα (CO2)",
        "lat": 40.512, "lon": 21.261
    }
}

# 1. Header
st.markdown('<div class="header-style"><h2>🌱 Ψηφιακό Διαβατήριο</h2><p style="margin:0; font-weight: bold;">ΟΣΠΡΙΑ ΧΑΣΙΩΝ / OSPRIA HASION</p></div>', unsafe_allow_html=True)

# 2. Επιλογή Παρτίδας
selected_prod = st.selectbox("Σκανάρετε ή Επιλέξτε Παρτίδα:", list(products.keys()))
p = products[selected_prod]

# 3. Εικόνες & Σήμα Bio
col1, col2 = st.columns([3, 1.2])
with col1:
    if os.path.exists(p['img']): st.image(p['img'], use_container_width=True)
    else: st.info(f"Φορτώνει: {p['img']}")
with col2:
    if p['show_bio'] and os.path.exists(p['bio_img']):
        st.image(p['bio_img'], use_container_width=True)
        st.markdown('<p class="bio-text">HELLAS Agriculture<br>GR-BIO-007</p>', unsafe_allow_html=True)

# 4. Eco Impact Badge
st.markdown(f'<div class="eco-badge">🌍 ΠΕΡΙΒΑΛΛΟΝΤΙΚΟ ΟΦΕΛΟΣ: {p["eco_win"]}</div>', unsafe_allow_html=True)

# 5. Στοιχεία Παραγωγού & Πιστοποίηση
st.markdown('<div class="section-header">👨‍🌾 Στοιχεία Παραγωγού & Batch ID</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="info-card">
    <p style="margin:2px;">• <b>Παραγωγός:</b> {p['producer']}</p>
    <p style="margin:2px;">• <b>Lot ID:</b> {p['id']}</p>
    <p style="margin:2px;">• <b>Πιστοποίηση:</b> ISO 22000:2018</p>
</div>
""", unsafe_allow_html=True)

# 6. Βίντεο Drone
st.markdown('<div class="section-header">🚁 Drone Spraying (Real Footage)</div>', unsafe_allow_html=True)
st.video(p['video'])

# 7. Live Stats
st.markdown('<div class="section-header">🌡️ Live Κατάσταση (UAV Data)</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="stats-container">
    <div class="stat-card">❤️<br><small>Υγεία</small><br><b>{p['health']}</b></div>
    <div class="stat-card">🌿<br><small>Στάδιο</small><br><b>{p['phase']}</b></div>
    <div class="stat-card">☀️<br><small>Temp</small><br><b>28°C</b></div>
</div>
""", unsafe_allow_html=True)

# 8. Συνταγή
st.markdown('<div class="section-header">👩‍🍳 Πρόταση Μαγειρικής</div>', unsafe_allow_html=True)
st.markdown(f'<div class="recipe-card">{p["recipe"]}</div>', unsafe_allow_html=True)

# 9. Storytelling
st.markdown('<div class="section-header">🏠 Η Ιστορία μας</div>', unsafe_allow_html=True)
st.markdown('<div class="info-card"><b>ΟΣΠΡΙΑ ΧΑΣΙΩΝ (Καρπερό Γρεβενών)</b><br>Από το 2015, συνδυάζουμε το μεράκι της οικογένειας με την τεχνολογία αιχμής των drones για ένα καθαρό περιβάλλον.</div>', unsafe_allow_html=True)

# 10. Χάρτης
st.markdown('<div class="section-header">🗺️ Τοποθεσία Αγροτεμαχίου</div>', unsafe_allow_html=True)
map_data = pd.DataFrame({'lat': [p['lat']], 'lon': [p['lon']]})
st.map(map_data)

# 11. Interactive Footer
st.markdown("---")
col_bt1, col_bt2 = st.columns(2)
with col_bt1:
    if st.button("📱 QR Code"):
        st.image("https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://hasia-beans.streamlit.app", caption="Scan for DPP Demo")
with col_bt2:
    if st.button("⭐ Ξενάγηση"):
        st.balloons()
        st.success("Registration Success!")

st.markdown("<p style='text-align:center; font-size:11px; color:#999;'>ΟΣΠΡΙΑ ΧΑΣΙΩΝ DPP v8.0 | Final Thesis Version</p>", unsafe_allow_html=True)
