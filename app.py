import streamlit as st
import pandas as pd
import numpy as np
import os

# Ρύθμιση Σελίδας
st.set_page_config(page_title="OSPRIA HASION DPP", page_icon="🌱", layout="wide")

# CSS ΓΙΑ ΤΟ ΣΩΣΤΟ LAYOUT (ΕΠΑΝΑΦΟΡΑ ΜΕΓΕΘΟΥΣ & ICON ALIGNMENT)
st.markdown("""
    <style>
    .main { background-color: #f8f9f5; }
    .stApp { max-width: 500px; margin: 0 auto; background: white; padding: 10px; border-radius: 20px; box-shadow: 0px 0px 20px rgba(0,0,0,0.1); }
    
    /* Header */
    .header-style { background-color: #2e7d32; color: white; padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 15px; }
    .header-style h2 { margin: 0; font-size: 22px; }
    .header-style p { margin: 5px 0 0 0; font-size: 14px; font-weight: bold; text-transform: uppercase; }

    /* Ενότητες */
    .section-header { background-color: #1b5e20; color: white; padding: 8px 15px; border-radius: 10px; margin-top: 15px; font-weight: bold; font-size: 15px; }
    .info-card { background-color: #ffffff; padding: 12px; border-radius: 10px; border: 1px solid #eee; margin-top: 5px; font-size: 14px; line-height: 1.6; }
    .producer-card { background: linear-gradient(135deg, #f1f8e9 0%, #dcedc8 100%); padding: 15px; border-radius: 15px; border: 1px solid #aed581; margin-top: 10px; }

    /* Stats Container - Δίπλα-δίπλα με σωστό μέγεθος */
    .stats-container { display: flex; justify-content: space-between; gap: 8px; margin-top: 10px; }
    .stat-card { background: #f1f8e9; border: 1px solid #e0e0e0; border-radius: 12px; padding: 12px 5px; text-align: center; flex: 1; }
    .stat-card span { font-size: 20px; display: block; margin-bottom: 5px; }
    .stat-card small { font-size: 11px; color: #666; font-weight: bold; display: block; }
    .stat-card b { font-size: 15px; color: #1b5e20; display: block; margin-top: 2px; }

    .stButton>button { background-color: #2e7d32 !important; color: white !important; border-radius: 20px; width: 100%; font-weight: bold; height: 48px; border: none; }
    .about-section { background-color: #e8f5e9; padding: 15px; border-radius: 15px; border-left: 5px solid #2e7d32; margin-top: 10px; font-size: 13px; }
    .recipe-card { background-color: #fffde7; padding: 12px; border-radius: 10px; border: 1px dashed #fbc02d; margin-top: 10px; font-size: 14px; }
    .bio-text { font-size: 10px; text-align: center; font-weight: bold; color: #333; margin-top: -10px; }
    </style>
    """, unsafe_allow_html=True)

# --- ΔΕΔΟΜΕΝΑ ΠΡΟΪΟΝΤΩΝ ---
products = {
    "Φακή Χασίων (Παρτίδα #OX-01)": {
        "producer": "Νικόλαος Παπαδόπουλος",
        "id": "#OX-01-066", "origin": "Καρπερό, Γρεβενά", "type": "Βιολογική",
        "phase": "Ανάπτυξη", "health": "96%", "temp": "28°C",
        "img": "fakes.JPEG", "bio_img": "bio.png", "show_bio": True,
        "drone_date": "05 Ιουνίου 2025", "drone_flights": "3 επιτυχείς", "drone_tool": "Βιολογικό Εντομοκτόνο",
        "video": "https://www.youtube.com/watch?v=m0md-5Wzp1E",
        "recipe": "🍲 <b>Σαλάτα Beluga:</b> Βράστε για 20', προσθέστε φρέσκο κρεμμυδάκι, ντοματίνια και βαλσάμικο.",
        "lat": 39.941, "lon": 21.632
    },
    "Φασόλια Γίγαντες (Παρτίδα #KT-05)": {
        "producer": "Δημήτριος Γεωργίου",
        "id": "#KT-05-070", "origin": "Καστοριά", "type": "Συμβατική",
        "phase": "Ωρίμανση", "health": "98%", "temp": "27°C",
        "img": "gigantes.png", "bio_img": "bio.png", "show_bio": False,
        "drone_date": "12 Ιουλίου 2025", "drone_flights": "6 επιτυχείς", "drone_tool": "Εγκεκριμένο Σκεύασμα",
        "video": "https://www.youtube.com/watch?v=SKGdu1x0sxo",
        "recipe": "🥘 <b>Γίγαντες στο φούρνο:</b> Με φρέσκια ντομάτα, σέλινο και πολύ μεράκι!",
        "lat": 40.512, "lon": 21.261
    }
}

# 1. Header
st.markdown('<div class="header-style"><h2>🌱 Ψηφιακό Διαβατήριο</h2><p>ΟΣΠΡΙΑ ΧΑΣΙΩΝ / OSPRIA HASION</p></div>', unsafe_allow_html=True)

# 2. Επιλογή Παρτίδας
selected_prod = st.selectbox("Επιλέξτε Σκαναρισμένη Παρτίδα (QR):", list(products.keys()), label_visibility="collapsed")
p = products[selected_prod]

# 3. Εικόνες & Σήμα Bio
col1, col2 = st.columns([3, 1.2])
with col1:
    if os.path.exists(p['img']):
        st.image(p['img'], use_container_width=True)
with col2:
    if p['show_bio'] and os.path.exists(p['bio_img']):
        st.image(p['bio_img'], use_container_width=True)
        st.markdown('<p class="bio-text">HELLAS Agriculture<br>GR-BIO-007</p>', unsafe_allow_html=True)

# 4. Στοιχεία Παραγωγού
st.markdown('<div class="section-header">👨‍🌾 Στοιχεία Παραγωγού</div>', unsafe_allow_html=True)
st.markdown(f'<div class="producer-card"><p style="margin:0; font-size:16px;"><b>{p["producer"]}</b></p><p style="margin:0; font-size:14px; color:#555;">📍 {p["origin"]}</p></div>', unsafe_allow_html=True)

# 5. Πληροφορίες & Πιστοποίηση
st.markdown('<div class="section-header">📋 Πληροφορίες & Πιστοποίηση</div>', unsafe_allow_html=True)
st.markdown(f'<div class="info-card"><p style="margin:2px;">• <b>Lot ID:</b> {p["id"]}</p><p style="margin:2px;">• <b>Καλλιέργεια:</b> {p["type"]}</p><p style="margin:2px;">• <b>Πρότυπο:</b> ISO 22000:2018</p></div>', unsafe_allow_html=True)

# 6. Βίντεο & Drone Data (Εδώ οι πτήσεις)
st.markdown('<div class="section-header">🚁 Drone Spraying (Real Footage)</div>', unsafe_allow_html=True)
st.video(p['video'])
st.markdown(f'<div class="info-card" style="border-left: 5px solid #81c784;"><p style="margin:2px;">• <b>Τελευταίος Ψεκασμός:</b> {p["drone_date"]}</p><p style="margin:2px;">• <b>Επεμβάσεις:</b> {p["drone_flights"]}</p></div>', unsafe_allow_html=True)

# 7. Live Data (Δίπλα-δίπλα: Υγεία, Στάδιο, Θερμοκρασία)
st.markdown('<div class="section-header">🌡️ Live Κατάσταση (UAV Data)</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="stats-container">
    <div class="stat-card"><span>❤️</span><small>Υγεία</small><b>{p['health']}</b></div>
    <div class="stat-card"><span>🌿</span><small>Στάδιο</small><b>{p['phase']}</b></div>
    <div class="stat-card"><span>☀️</span><small>Καιρός</small><b>{p['temp']}</b></div>
</div>
""", unsafe_allow_html=True)

# 8. Συνταγή
st.markdown('<div class="section-header">👩‍🍳 Πρόταση Μαγειρικής</div>', unsafe_allow_html=True)
st.markdown(f'<div class="recipe-card">{p["recipe"]}</div>', unsafe_allow_html=True)

# 9. Storytelling
st.markdown('<div class="section-header">🏠 Η Ιστορία μας</div>', unsafe_allow_html=True)
st.markdown('<div class="about-section"><b>ΟΣΠΡΙΑ ΧΑΣΙΩΝ (Καρπερό Γρεβενών)</b><br>Καλλιεργούμε 250 στρέμματα με σεβασμό στη γη. Η χρήση των <b>drones</b> μας επιτρέπει να μειώνουμε τις εισροές, προσφέροντας ένα προϊόν απόλυτα ασφαλές.</div>', unsafe_allow_html=True)

# 10. Χάρτης
st.markdown('<div class="section-header">🗺️ Τοποθεσία Αγροτεμαχίου</div>', unsafe_allow_html=True)
map_data = pd.DataFrame({'lat': [p['lat']], 'lon': [p['lon']]})
st.map(map_data)

# 11. Button
if st.button("⭐ Κλείστε Ξενάγηση στο Κτήμα"):
    st.balloons()
    st.success("Σας περιμένουμε!")

st.markdown("<p style='text-align:center; font-size:11px; color:#999; margin-top:20px;'>ΟΣΠΡΙΑ ΧΑΣΙΩΝ DPP v11.0</p>", unsafe_allow_html=True)
