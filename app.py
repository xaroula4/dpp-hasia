import streamlit as st
import pandas as pd
import numpy as np
import os

# Ρύθμιση Σελίδας
st.set_page_config(page_title="Hasia Beans DPP", page_icon="🌱", layout="wide")

# CSS ΓΙΑ ΤΟ ΤΕΛΙΚΟ MOBILE LOOK
st.markdown("""
    <style>
    .main { background-color: #f8f9f5; }
    .stApp { max-width: 500px; margin: 0 auto; background: white; padding: 10px; border-radius: 20px; box-shadow: 0px 0px 20px rgba(0,0,0,0.1); }
    .header-style { background-color: #2e7d32; color: white; padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 15px; }
    .section-header { background-color: #1b5e20; color: white; padding: 8px 15px; border-radius: 10px; margin-top: 15px; font-weight: bold; font-size: 14px; }
    .info-card { background-color: #ffffff; padding: 12px; border-radius: 10px; border: 1px solid #eee; margin-top: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .stats-container { display: flex; justify-content: space-around; gap: 5px; margin-top: 10px; }
    .stat-card { background: #f1f8e9; border: 1px solid #e0e0e0; border-radius: 12px; padding: 10px; text-align: center; flex: 1; }
    .stButton>button { background-color: #2e7d32; color: white; border-radius: 20px; width: 100%; font-weight: bold; height: 45px; border: none; }
    .about-section { background-color: #e8f5e9; padding: 15px; border-radius: 15px; border-left: 5px solid #2e7d32; margin-top: 10px; font-size: 13px; }
    .recipe-card { background-color: #fffde7; padding: 12px; border-radius: 10px; border: 1px dashed #fbc02d; margin-top: 10px; }
    .bio-text { font-size: 10px; text-align: center; font-weight: bold; color: #333; margin-top: -10px; }
    </style>
    """, unsafe_allow_html=True)

# --- ΔΕΔΟΜΕΝΑ ΠΡΟΪΟΝΤΩΝ ---
products = {
    "Φακή Χασίων": {
        "id": "#OX-01-066", "origin": "Καρπερό, Γρεβενά", "type": "Βιολογική",
        "date": "Ιούλιος 2025", "phase": "Ανάπτυξη", "health": "96%", 
        "img": "fakes.JPEG", "bio_img": "bio.png", "show_bio": True,
        "drone_date": "05 Ιουνίου 2025", "drone_flights": "3 επιτυχείς", "drone_tool": "Βιολογικό Εντομοκτόνο",
        "video": "https://www.youtube.com/watch?v=m0md-5Wzp1E",
        "recipe": "🍲 <b>Σαλάτα Beluga:</b> Βράστε για 20', προσθέστε φρέσκο κρεμμυδάκι, ντοματίνια και βαλσάμικο.",
        "lat": 39.941, "lon": 21.632
    },
    "Φασόλια Γίγαντες": {
        "id": "#OX-01-070", "origin": "Καστοριά", "type": "Συμβατική",
        "date": "Σεπτέμβριος 2025", "phase": "Ωρίμανση", "health": "98%", 
        "img": "gigantes.png", "bio_img": "bio.png", "show_bio": False,
        "drone_date": "12 Ιουλίου 2025", "drone_flights": "6 επιτυχείς", "drone_tool": "Εγκεκριμένο Σκεύασμα",
        "video": "https://www.youtube.com/watch?v=SKGdu1x0sxo",
        "recipe": "🥘 <b>Γίγαντες στο φούρνο:</b> Με φρέσκια ντομάτα, σέλινο και πολύ μεράκι!",
        "lat": 40.512, "lon": 21.261
    }
}

# 1. Header με τη ΔΙΟΡΘΩΜΕΝΗ ΕΠΩΝΥΜΙΑ
st.markdown('<div class="header-style"><h2>🌱 Ψηφιακό Διαβατήριο</h2><p style="margin:0; font-weight: bold; letter-spacing: 1px;">ΟΣΠΡΙΑ ΧΑΣΙΩΝ / OSPRIA HASION</p></div>', unsafe_allow_html=True)

# 2. Επιλογή
selected_prod = st.selectbox("Επιλέξτε Προϊόν:", list(products.keys()))
p = products[selected_prod]

# 3. Εικόνες (Συσκευασία + Σήμα Bio)
col1, col2 = st.columns([3, 1.2])
with col1:
    try:
        st.image(p['img'], use_container_width=True)
    except:
        st.error(f"Λείπει η εικόνα: {p['img']}")
with col2:
    if p['show_bio'] and os.path.exists(p['bio_img']):
        st.image(p['bio_img'], use_container_width=True)
        st.markdown('<p class="bio-text">HELLAS Agriculture<br>GR-BIO-007</p>', unsafe_allow_html=True)

# 4. Πληροφορίες & ISO
st.markdown('<div class="section-header">📋 Πληροφορίες & Πιστοποίηση</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="info-card">
    <p style="margin:2px;">• <b>ID:</b> {p['id']} | <b>Προέλευση:</b> {p['origin']}</p>
    <p style="margin:2px;">• <b>Καλλιέργεια:</b> {p['type']}</p>
    <p style="margin:2px;">• <b>Πρότυπο Ασφάλειας:</b> ISO 22000:2018</p>
</div>
""", unsafe_allow_html=True)

# 5. Ψεκασμός με Drone (Video & Data)
st.markdown('<div class="section-header">🚁 Drone Spraying (Real Footage)</div>', unsafe_allow_html=True)
st.video(p['video'])
st.markdown(f"""
<div class="info-card" style="border-left: 5px solid #81c784;">
    <p style="margin:2px;">• <b>Τελευταίος Ψεκασμός:</b> {p['drone_date']}</p>
    <p style="margin:2px;">• <b>Σκεύασμα:</b> {p['drone_tool']}</p>
    <p style="margin:2px;">• <b>Αρ. Πτήσεων:</b> {p['drone_flights']}</p>
</div>
""", unsafe_allow_html=True)

# 6. Live Data
st.markdown('<div class="section-header">🌡️ Live Κατάσταση (UAV Data)</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="stats-container">
    <div class="stat-card">❤️<br><small>Υγεία</small><br><b style="color:#2e7d32; font-size:16px;">{p['health']}</b></div>
    <div class="stat-card">🌿<br><small>Στάδιο</small><br><b>{p['phase']}</b></div>
    <div class="stat-card">☀️<br><small>Καιρός</small><br><b>28°C</b></div>
</div>
""", unsafe_allow_html=True)

# 7. Συνταγή
st.markdown('<div class="section-header">👩‍🍳 Πρόταση Μαγειρικής</div>', unsafe_allow_html=True)
st.markdown(f'<div class="recipe-card">{p["recipe"]}</div>', unsafe_allow_html=True)

# 8. Η Ιστορία μας (Storytelling)
st.markdown('<div class="section-header">🏠 Η Ιστορία μας</div>', unsafe_allow_html=True)
st.markdown("""
<div class="about-section">
    <b>ΟΣΠΡΙΑ ΧΑΣΙΩΝ (Καρπερό Γρεβενών)</b><br>
    Καλλιεργούμε 250 στρέμματα με σεβασμό στη γη. Η χρήση των <b>drones</b> μας επιτρέπει 
    να μειώνουμε τις εισροές, προσφέροντας ένα προϊόν απόλυτα ασφαλές και ψηφιακά ιχνηλατήσιμο.
</div>
""", unsafe_allow_html=True)

# 9. Χάρτης
st.markdown('<div class="section-header">🗺️ Τοποθεσία Αγροτεμαχίου</div>', unsafe_allow_html=True)
map_data = pd.DataFrame({'lat': [p['lat']], 'lon': [p['lon']]})
st.map(map_data)

# 10. Button
if st.button("⭐ Κλείστε Ξενάγηση στο Κτήμα"):
    st.balloons()
    st.success("Σας περιμένουμε στα Χάσια!")

st.markdown("<p style='text-align:center; font-size:11px; color:#999; margin-top:20px;'>ΟΣΠΡΙΑ ΧΑΣΙΩΝ DPP v5.0 | 2026</p>", unsafe_allow_html=True)
