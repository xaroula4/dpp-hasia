import streamlit as st
import pandas as pd
import numpy as np
import os

# Ρύθμιση Σελίδας
st.set_page_config(page_title="OSPRIA HASION DPP", page_icon="🌱", layout="wide")

# CSS ΓΙΑ COMPACT MOBILE LOOK
st.markdown("""
    <style>
    .main { background-color: #f8f9f5; }
    .stApp { max-width: 450px; margin: 0 auto; background: white; padding: 5px; border-radius: 15px; }
    
    /* Header - Πιο μαζεμένο */
    .header-style { background-color: #2e7d32; color: white; padding: 12px; border-radius: 15px; text-align: center; margin-bottom: 10px; }
    .header-style h2 { font-size: 20px; margin: 0; }
    .header-style p { font-size: 12px; margin: 0; opacity: 0.9; }

    /* Ενότητες - Λιγότερο padding */
    .section-header { background-color: #1b5e20; color: white; padding: 5px 12px; border-radius: 8px; margin-top: 10px; font-weight: bold; font-size: 13px; }
    .info-card { background-color: #ffffff; padding: 8px; border-radius: 8px; border: 1px solid #eee; margin-top: 5px; font-size: 12px; }
    
    /* Stats - Μικρότερα Cards */
    .stats-container { display: flex; justify-content: space-around; gap: 4px; margin-top: 8px; }
    .stat-card { background: #f9fbf7; border: 1px solid #e0e0e0; border-radius: 10px; padding: 6px; text-align: center; flex: 1; }
    .stat-card b { font-size: 13px; color: #2e7d32; }
    .stat-card small { font-size: 10px; color: #666; }

    /* Eco Badge */
    .eco-badge { background-color: #e1f5fe; padding: 6px; border-radius: 8px; border: 1px solid #01579b; color: #01579b; font-size: 11px; text-align: center; margin: 8px 0; }
    
    .stButton>button { background-color: #2e7d32 !important; color: white !important; border-radius: 15px; height: 38px; font-size: 14px; border: none; }
    .bio-text { font-size: 9px; text-align: center; font-weight: bold; color: #333; margin-top: -8px; }
    </style>
    """, unsafe_allow_html=True)

# --- ΔΕΔΟΜΕΝΑ ---
products = {
    "Φακή Χασίων (#OX-01)": {
        "producer": "Ν. Παπαδόπουλος", "id": "#OX-01-066", "type": "Βιολογική",
        "phase": "Ανάπτυξη", "health": "96%", "temp": "28°C",
        "img": "fakes.JPEG", "bio_img": "bio.png", "show_bio": True,
        "drone_flights": "3 πτήσεις", "video": "https://www.youtube.com/watch?v=m0md-5Wzp1E",
        "recipe": "🍲 <b>Beluga:</b> Βράστε 20', προσθέστε κρεμμυδάκι & βαλσάμικο.",
        "eco": "💧 -1.200L Νερό", "lat": 39.941, "lon": 21.632
    },
    "Φασόλια Γίγαντες (#KT-05)": {
        "producer": "Δ. Γεωργίου", "id": "#KT-05-070", "type": "Συμβατική",
        "phase": "Ωρίμανση", "health": "98%", "temp": "27°C",
        "img": "gigantes.png", "bio_img": "bio.png", "show_bio": False,
        "drone_flights": "6 πτήσεις", "video": "https://www.youtube.com/watch?v=SKGdu1x0sxo",
        "recipe": "🥘 <b>Φούρνου:</b> Με ντομάτα, σέλινο και μεράκι!",
        "eco": "🚜 -35% CO2", "lat": 40.512, "lon": 21.261
    }
}

# 1. Header
st.markdown('<div class="header-style"><h2>🌱 Ψηφιακό Διαβατήριο</h2><p>ΟΣΠΡΙΑ ΧΑΣΙΩΝ / OSPRIA HASION</p></div>', unsafe_allow_html=True)

# 2. Selection
selected_prod = st.selectbox("Επιλογή Παρτίδας:", list(products.keys()), label_visibility="collapsed")
p = products[selected_prod]

# 3. Images & Bio Tag
col1, col2 = st.columns([3, 1])
with col1:
    if os.path.exists(p['img']): st.image(p['img'], use_container_width=True)
with col2:
    if p['show_bio'] and os.path.exists(p['bio_img']):
        st.image(p['bio_img'], use_container_width=True)
        st.markdown('<p class="bio-text">HELLAS Ag.<br>GR-BIO-007</p>', unsafe_allow_html=True)

# 4. Eco & Info
st.markdown(f'<div class="eco-badge">🌍 Eco-Benefit: {p["eco"]}</div>', unsafe_allow_html=True)

st.markdown('<div class="section-header">📋 Στοιχεία Παρτίδας</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="info-card">
    • <b>Παραγωγός:</b> {p['producer']} | <b>Lot:</b> {p['id']}<br>
    • <b>Τύπος:</b> {p['type']} | <b>ISO 22000:2018</b>
</div>
""", unsafe_allow_html=True)

# 5. Drone Video
st.markdown('<div class="section-header">🚁 Drone Footage (UAV)</div>', unsafe_allow_html=True)
st.video(p['video'])

# 6. Stats - Compact
st.markdown(f"""
<div class="stats-container">
    <div class="stat-card"><small>Υγεία</small><br><b>{p['health']}</b></div>
    <div class="stat-card"><small>Στάδιο</small><br><b>{p['phase']}</b></div>
    <div class="stat-card"><small>Πτήσεις</small><br><b>{p['drone_flights']}</b></div>
</div>
""", unsafe_allow_html=True)

# 7. Recipe & Story
st.markdown('<div class="section-header">👩‍🍳 Πρόταση Μαγειρικής</div>', unsafe_allow_html=True)
st.markdown(f'<div class="info-card">{p["recipe"]}</div>', unsafe_allow_html=True)

st.markdown('<div class="section-header">🏠 Η Ιστορία μας</div>', unsafe_allow_html=True)
st.markdown('<div class="info-card"><b>ΟΣΠΡΙΑ ΧΑΣΙΩΝ (Καρπερό)</b>: Παραγωγή 250 στρ. με τεχνολογία Drone για μηδενικό αποτύπωμα.</div>', unsafe_allow_html=True)

# 8. Map & Interaction
st.markdown('<div class="section-header">🗺️ Τοποθεσία</div>', unsafe_allow_html=True)
st.map(pd.DataFrame({'lat': [p['lat']], 'lon': [p['lon']]}), zoom=12)

st.markdown("<br>", unsafe_allow_html=True)
if st.button("⭐ Κλείστε Ξενάγηση"):
    st.balloons()

st.markdown("<p style='text-align:center; font-size:9px; color:#999;'>OSPRIA HASION DPP v9.0</p>", unsafe_allow_html=True)
