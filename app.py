import streamlit as st
import pandas as pd
import numpy as np
import os

# Ρύθμιση Σελίδας
st.set_page_config(page_title="Hasia Beans DPP", page_icon="🌱", layout="wide")

# CSS
st.markdown("""
    <style>
    .main { background-color: #f8f9f5; }
    .stApp { max-width: 500px; margin: 0 auto; background: white; padding: 10px; border-radius: 20px; box-shadow: 0px 0px 20px rgba(0,0,0,0.1); }
    .header-style { background-color: #2e7d32; color: white; padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 15px; }
    .section-header { background-color: #1b5e20; color: white; padding: 8px 15px; border-radius: 10px; margin-top: 15px; font-weight: bold; font-size: 14px; }
    .info-card { background-color: #ffffff; padding: 12px; border-radius: 10px; border: 1px solid #eee; margin-top: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .producer-card { background: linear-gradient(135deg, #f1f8e9 0%, #dcedc8 100%); padding: 15px; border-radius: 15px; border: 1px solid #aed581; margin-top: 10px; }
    .bio-text { font-size: 10px; text-align: center; font-weight: bold; color: #333; margin-top: -10px; }
    </style>
    """, unsafe_allow_html=True)

# --- ΔΥΝΑΜΙΚΑ ΔΕΔΟΜΕΝΑ ΠΑΡΤΙΔΩΝ ---
products = {
    "Φακή Χασίων (Παρτίδα #OX-01)": {
        "producer": "Νικόλαος Παπαδόπουλος",
        "location": "Καρπερό Γρεβενών",
        "id": "#OX-01-066", "type": "Βιολογική",
        "date": "Ιούλιος 2025", "health": "96%", 
        "img": "fakes.JPEG", "bio_img": "bio.png", "show_bio": True,
        "drone_date": "05/06/2025", "drone_flights": "3 πτήσεις",
        "video": "https://www.youtube.com/watch?v=m0md-5Wzp1E",
        "lat": 39.941, "lon": 21.632
    },
    "Φασόλια Γίγαντες (Παρτίδα #KT-05)": {
        "producer": "Δημήτριος Γεωργίου",
        "location": "Λιμνοχώρι Καστοριάς",
        "id": "#KT-05-070", "type": "Συμβατική",
        "date": "Σεπτέμβριος 2025", "health": "98%", 
        "img": "gigantes.png", "bio_img": "bio.png", "show_bio": False,
        "drone_date": "12/07/2025", "drone_flights": "6 πτήσεις",
        "video": "https://www.youtube.com/watch?v=SKGdu1x0sxo",
        "lat": 40.512, "lon": 21.261
    }
}

# 1. Header
st.markdown('<div class="header-style"><h2>🌱 Ψηφιακό Διαβατήριο</h2><p style="margin:0; font-weight: bold;">ΟΣΠΡΙΑ ΧΑΣΙΩΝ / OSPRIA HASION</p></div>', unsafe_allow_html=True)

# 2. Selection (Προσομοίωση Σκαναρίσματος διαφορετικού QR)
selected_prod = st.selectbox("Επιλέξτε Σκαναρισμένη Παρτίδα (QR):", list(products.keys()))
p = products[selected_prod]

# 3. Εικόνες & Σήμα
col1, col2 = st.columns([3, 1.2])
with col1:
    st.image(p['img'], use_container_width=True)
with col2:
    if p['show_bio'] and os.path.exists(p['bio_img']):
        st.image(p['bio_img'], use_container_width=True)
        st.markdown('<p class="bio-text">HELLAS Agriculture<br>GR-BIO-007</p>', unsafe_allow_html=True)

# 4. ΣΤΟΙΧΕΙΑ ΠΑΡΑΓΩΓΟΥ (Νέα Ενότητα)
st.markdown('<div class="section-header">👨‍🌾 Στοιχεία Παραγωγού Παρτίδας</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="producer-card">
    <p style="margin:0; font-size:16px;"><b>{p['producer']}</b></p>
    <p style="margin:0; font-size:14px; color:#555;">📍 {p['location']}</p>
    <hr style="margin:10px 0; border:0; border-top:1px solid #aed581;">
    <p style="margin:0; font-size:12px;">Αυτός ο παραγωγός εφαρμόζει τις προδιαγραφές <b>Precision Agriculture</b> της OSPRIA HASION.</p>
</div>
""", unsafe_allow_html=True)

# 5. Πληροφορίες Παρτίδας
st.markdown('<div class="section-header">📋 Πιστοποίηση Παρτίδας</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="info-card">
    <p style="margin:2px;">• <b>Lot ID:</b> {p['id']}</p>
    <p style="margin:2px;">• <b>Πρότυπο:</b> ISO 22000:2018</p>
    <p style="margin:2px;">• <b>Τύπος:</b> {p['type']}</p>
</div>
""", unsafe_allow_html=True)

# 6. Drone Footage
st.markdown('<div class="section-header">🚁 Ιστορικό UAV (Drone)</div>', unsafe_allow_html=True)
st.video(p['video'])
st.caption(f"Τελευταίος έλεγχος: {p['drone_date']} | {p['drone_flights']}")

# 7. Χάρτης (Αλλάζει ανάλογα με το χωράφι του παραγωγού)
st.markdown('<div class="section-header">🗺️ Ακριβής Τοποθεσία Αγροτεμαχίου</div>', unsafe_allow_html=True)
map_data = pd.DataFrame({'lat': [p['lat']], 'lon': [p['lon']]})
st.map(map_data)

# 8. Footer
st.markdown("<p style='text-align:center; font-size:10px; color:#999; margin-top:20px;'>ΟΣΠΡΙΑ ΧΑΣΙΩΝ DPP v6.0<br>Traceability System Enabled</p>", unsafe_allow_html=True)
