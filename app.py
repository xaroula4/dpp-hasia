import streamlit as st
import pandas as pd
import numpy as np
import os

# Ρύθμιση Σελίδας
st.set_page_config(page_title="OSPRIA HASION DPP", page_icon="🌱", layout="wide")

# CSS ΓΙΑ ΤΟ ΣΩΣΤΟ LAYOUT (ΔΙΠΛΑ-ΔΙΠΛΑ ΤΑ STATS)
st.markdown("""
    <style>
    .main { background-color: #f8f9f5; }
    .stApp { max-width: 500px; margin: 0 auto; background: white; padding: 10px; border-radius: 20px; box-shadow: 0px 0px 20px rgba(0,0,0,0.1); }
    
    /* Header */
    .header-style { background-color: #2e7d32; color: white; padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 15px; }
    .header-style h2 { margin: 0; font-size: 22px; }
    .header-style p { margin: 5px 0 0 0; font-size: 13px; font-weight: bold; }

    /* Ενότητες */
    .section-header { background-color: #1b5e20; color: white; padding: 8px 15px; border-radius: 10px; margin-top: 15px; font-weight: bold; font-size: 15px; }
    .info-card { background-color: #ffffff; padding: 12px; border-radius: 10px; border: 1px solid #eee; margin-top: 5px; font-size: 13px; line-height: 1.5; }
    
    /* Stats Row (Αναγκαστικά Δίπλα-Δίπλα) */
    .stats-row { display: flex; justify-content: space-between; gap: 8px; margin-top: 10px; }
    .stat-box { background: #f9fbf7; border: 1px solid #e0e0e0; border-radius: 12px; padding: 10px; text-align: center; flex: 1; min-width: 0; }
    .stat-box span { font-size: 18px; display: block; }
    .stat-box div { font-size: 11px; color: #666; font-weight: bold; margin: 4px 0; }
    .stat-box b { font-size: 14px; color: #1b5e20; display: block; }

    .stButton>button { background-color: #2e7d32 !important; color: white !important; border-radius: 20px; width: 100%; font-weight: bold; height: 45px; border: none; }
    .bio-text { font-size: 9px; text-align: center; font-weight: bold; color: #333; margin-top: -8px; }
    </style>
    """, unsafe_allow_html=True)

# --- ΔΕΔΟΜΕΝΑ ---
products = {
    "Φακή Χασίων (Παρτίδα #OX-01)": {
        "producer": "Νικόλαος Παπαδόπουλος",
        "id": "#OX-01-066", "origin": "Καρπερό, Γρεβενά", "type": "Βιολογική",
        "phase": "Ανάπτυξη", "health": "96%", "temp": "28°C",
        "img": "fakes.JPEG", "bio_img": "bio.png", "show_bio": True,
        "drone_flights": "3 επιτυχείς", "drone_date": "05 Ιουνίου 2025",
        "video": "https://www.youtube.com/watch?v=m0md-5Wzp1E",
        "recipe": "🍲 <b>Σαλάτα Beluga:</b> Βράστε για 20', προσθέστε φρέσκο κρεμμυδάκι, ντοματίνια και βαλσάμικο.",
        "lat": 39.941, "lon": 21.632
    },
    "Φασόλια Γίγαντες (Παρτίδα #KT-05)": {
        "producer": "Δημήτριος Γεωργίου",
        "id": "#KT-05-070", "origin": "Καστοριά", "type": "Συμβατική",
        "phase": "Ωρίμανση", "health": "98%", "temp": "27°C",
        "img": "gigantes.png", "bio_img": "bio.png", "show_bio": False,
        "drone_flights": "6 επιτυχείς", "drone_date": "12 Ιουλίου 2025",
        "video": "https://www.youtube.com/watch?v=SKGdu1x0sxo",
        "recipe": "🥘 <b>Γίγαντες στο φούρνο:</b> Με φρέσκια ντομάτα, σέλινο και πολύ μεράκι!",
        "lat": 40.512, "lon": 21.261
    }
}

# 1. Header
st.markdown('<div class="header-style"><h2>🌱 Ψηφιακό Διαβατήριο</h2><p>ΟΣΠΡΙΑ ΧΑΣΙΩΝ / OSPRIA HASION</p></div>', unsafe_allow_html=True)

# 2. Επιλογή
selected_prod = st.selectbox("Επιλέξτε Παρτίδα:", list(products.keys()), label_visibility="collapsed")
p = products[selected_prod]

# 3. Εικόνες & Σήμα Bio
col1, col2 = st.columns([3, 1.2])
with col1:
    if os.path.exists(p['img']): st.image(p['img'], use_container_width=True)
with col2:
    if p['show_bio'] and os.path.exists(p['bio_img']):
        st.image(p['bio_img'], use_container_width=True)
        st.markdown('<p class="bio-text">HELLAS Agriculture<br>GR-BIO-007</p>', unsafe_allow_html=True)

# 4. Πληροφορίες Παρτίδας
st.markdown('<div class="section-header">📋 Πληροφορίες Παρτίδας</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="info-card">
    • <b>Παραγωγός:</b> {p['producer']}<br>
    • <b>Lot ID:</b> {p['id']} | <b>ISO 22000:2018</b><br>
    • <b>Προέλευση:</b> {p['origin']}
</div>
""", unsafe_allow_html=True)

# 5. Drone Section (Με τις πτήσεις εδώ)
st.markdown('<div class="section-header">🚁 Drone Spraying (Real Footage)</div>', unsafe_allow_html=True)
st.video(p['video'])
st.markdown(f"""
<div class="info-card" style="border-left: 5px solid #2e7d32;">
    • <b>Τελευταίος Ψεκασμός:</b> {p['drone_date']}<br>
    • <b>Επεμβάσεις:</b> {p['drone_flights']}
</div>
""", unsafe_allow_html=True)

# 6. Live Κατάσταση (Δίπλα-δίπλα τα κουτάκια)
st.markdown('<div class="section-header">🌡️ Live Κατάσταση (UAV Data)</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="stats-row">
    <div class="stat-box">
        <span>❤️</span><div>Υγεία</div><b>{p['health']}</b>
    </div>
    <div class="stat-box">
        <span>🌿</span><div>Στάδιο</div><b>{p['phase']}</b>
    </div>
    <div class="stat-box">
        <span>☀️</span><div>Temp</div><b>{p['temp']}</b>
    </div>
</div>
""", unsafe_allow_html=True)

# 7. Συνταγή & Ιστορία
st.markdown('<div class="section-header">👩‍🍳 Πρόταση Μαγειρικής</div>', unsafe_allow_html=True)
st.markdown(f'<div class="info-card">{p["recipe"]}</div>', unsafe_allow_html=True)

st.markdown('<div class="section-header">🏠 Η Ιστορία μας</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="info-card">
    <b>ΟΣΠΡΙΑ ΧΑΣΙΩΝ (Καρπερό Γρεβενών)</b><br>
    Καλλιεργούμε 250 στρέμματα με τεχνολογία Drone για προϊόντα υψηλής ποιότητας.
</div>
""", unsafe_allow_html=True)

# 8. Χάρτης
st.markdown('<div class="section-header">🗺️ Τοποθεσία Αγροτεμαχίου</div>', unsafe_allow_html=True)
map_data = pd.DataFrame({'lat': [p['lat']], 'lon': [p['lon']]})
st.map(map_data)

if st.button("⭐ Κλείστε Ξενάγηση στο Κτήμα"):
    st.balloons()

st.markdown("<p style='text-align:center; font-size:10px; color:#999; margin-top:15px;'>ΟΣΠΡΙΑ ΧΑΣΙΩΝ DPP v11.0</p>", unsafe_allow_html=True)
