import streamlit as st
import pandas as pd
import numpy as np
import os

# Ρύθμιση Σελίδας
st.set_page_config(page_title="OSPRIA HASION DPP", page_icon="🌱", layout="wide")

# CSS ΓΙΑ ΤΟ ΤΕΛΙΚΟ MOBILE LOOK (v15.1 - Light Map & Fixed Colors)
st.markdown("""
    <style>
    .main { background-color: #f8f9f5; }
    .stApp { max-width: 500px; margin: 0 auto; background: white; padding: 10px; border-radius: 20px; box-shadow: 0px 0px 20px rgba(0,0,0,0.1); }
    
    /* Header */
    .header-style { background-color: #2e7d32; color: white !important; padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 15px; }
    .header-style h2 { margin: 0; font-size: 22px; color: white !important; }
    .header-style p { margin: 5px 0 0 0; font-size: 14px; font-weight: bold; text-transform: uppercase; color: white !important; }

    /* Επικεφαλίδες Ενοτήτων */
    .section-header { background-color: #1b5e20; color: white !important; padding: 8px 15px; border-radius: 10px; margin-top: 15px; font-weight: bold; font-size: 15px; display: flex; align-items: center; gap: 8px; }
    
    /* Κάρτες Πληροφοριών - Μαύρο κείμενο */
    .info-card { background-color: #ffffff; padding: 12px; border-radius: 10px; border: 1px solid #eee; margin-top: 5px; font-size: 14px; line-height: 1.6; color: #333 !important; }
    .info-card b, .info-card p, .info-card span, .info-card div { color: #333 !important; }
    
    .eco-box { background-color: #e1f5fe; padding: 12px; border-radius: 12px; border: 1px solid #01579b; color: #01579b !important; font-size: 13px; text-align: center; margin: 10px 0; font-weight: bold; }

    /* Διαδρομή Προϊόντος */
    .journey-row { display: flex; justify-content: space-between; align-items: center; padding: 15px 5px; background: #f1f8e9; border-radius: 15px; margin-top: 10px; }
    .journey-item { text-align: center; flex: 1; }
    .journey-icon { font-size: 22px; display: block; }
    .journey-label { font-size: 10px; font-weight: bold; color: #1b5e20 !important; margin-top: 5px; text-transform: uppercase; }
    .journey-date { font-size: 9px; color: #555 !important; display: block; margin-top: 2px; }
    .journey-arrow { color: #2e7d32 !important; font-weight: bold; font-size: 18px; margin-bottom: 20px; }

    /* Stats */
    .stats-container { display: flex; justify-content: space-around; gap: 8px; margin-top: 10px; }
    .stat-card { background: #f1f8e9; border: 1px solid #e0e0e0; border-radius: 12px; padding: 12px 5px; text-align: center; flex: 1; }
    .stat-card span { font-size: 20px; display: block; margin-bottom: 5px; }
    .stat-card small { font-size: 11px; color: #555 !important; font-weight: bold; display: block; }
    .stat-card b { font-size: 15px; color: #1b5e20 !important; display: block; margin-top: 2px; }

    /* Buttons */
    .stButton>button { background-color: #2e7d32 !important; color: white !important; border-radius: 20px; width: 100%; font-weight: bold; height: 48px; border: none; }
    
    .bio-text { font-size: 10px; text-align: center; font-weight: bold; color: #333 !important; margin-top: 5px; line-height: 1.1; }
    
    /* Storytelling & Recipe */
    .about-section { background-color: #f1f8e9; padding: 15px; border-radius: 15px; border-left: 5px solid #2e7d32; margin-top: 10px; font-size: 14px; line-height: 1.6; color: #333 !important; }
    .recipe-card { background-color: #fffde7; padding: 12px; border-radius: 10px; border: 1px dashed #fbc02d; margin-top: 10px; font-size: 14px; color: #333 !important; }

    /* Force Map to stay Light */
    [data-testid="stMap"] { border-radius: 15px; overflow: hidden; border: 1px solid #eee; }
    </style>
    """, unsafe_allow_html=True)

# --- ΔΕΔΟΜΕΝΑ ---
products = {
    "Φακή Χασίων (Παρτίδα #OX-01)": {
        "producer": "Νικόλαος Παπαδόπουλος", "id": "#OX-01-066", "origin": "Καρπερό, Γρεβενά", "type": "Βιολογική",
        "phase": "Ανάπτυξη", "health": "96%", "temp": "28°C", "img": "fakes.JPEG", "bio_img": "bio.png", "show_bio": True,
        "plant_date": "15/04/2025", "drone_date": "05/06/2025", "harvest_date": "20/07/2025",
        "drone_flights": "3 επιτυχείς",
        "eco": "💧 Μείωση νερού 40% μέσω UAV Precision Agriculture.",
        "video": "https://www.youtube.com/watch?v=m0md-5Wzp1E",
        "recipe": "🍲 <b>Σαλάτα Beluga:</b> Βράστε για 20', προσθέστε φρέσκο κρεμμυδάκι & βαλσάμικο.",
        "lat": 39.941, "lon": 21.632
    },
    "Φασόλια Γίγαντες (Παρτίδα #KT-05)": {
        "producer": "Δημήτριος Γεωργίου", "id": "#KT-05-070", "origin": "Καστοριά", "type": "Συμβατική",
        "phase": "Ωρίμανση", "health": "98%", "temp": "27°C", "img": "gigantes.png", "bio_img": "bio.png", "show_bio": False,
        "plant_date": "10/05/2025", "drone_date": "12/07/2025", "harvest_date": "15/09/2025",
        "drone_flights": "6 επιτυχείς",
        "eco": "🚜 Μείωση CO2 κατά 35% λόγω στοχευμένου ψεκασμού.",
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

# 3. Εικόνες & Bio
col1, col2 = st.columns([3, 1.2])
with col1:
    if os.path.exists(p['img']): st.image(p['img'], use_container_width=True)
with col2:
    if p['show_bio'] and os.path.exists(p['bio_img']):
        st.image(p['bio_img'], width=80)
        st.markdown('<p class="bio-text">HELLAS Ag.<br>GR-BIO-007</p>', unsafe_allow_html=True)

# 4. Στοιχεία Παραγωγού & Eco Box
st.markdown('<div class="section-header">👨‍🌾 Στοιχεία Παραγωγού</div>', unsafe_allow_html=True)
st.markdown(f'<div class="info-card"><b>Παραγωγός:</b> {p["producer"]}<br><b>📍 {p["origin"]}</b></div>', unsafe_allow_html=True)
st.markdown(f'<div class="eco-box">🌍 {p["eco"]}</div>', unsafe_allow_html=True)

# 5. Διαδρομή Προϊόντος
st.markdown('<div class="section-header">📅 Διαδρομή Προϊόντος</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="journey-row">
    <div class="journey-item"><span class="journey-icon">🚜</span><span class="journey-label">ΣΠΟΡΑ</span><span class="journey-date">{p['plant_date']}</span></div>
    <div class="journey-arrow">➜</div>
    <div class="journey-item"><span class="journey-icon">🚁</span><span class="journey-label">UAV</span><span class="journey-date">{p['drone_date']}</span></div>
    <div class="journey-arrow">➜</div>
    <div class="journey-item"><span class="journey-icon">🧺</span><span class="journey-label">ΣΥΓΚΟΜΙΔΗ</span><span class="journey-date">{p['harvest_date']}</span></div>
</div>
""", unsafe_allow_html=True)

# 6. Drone Footage
st.markdown('<div class="section-header">🚁 Drone Spraying (Real Footage)</div>', unsafe_allow_html=True)
st.video(p['video'])
st.markdown(f'<div class="info-card" style="border-left: 5px solid #2e7d32;">• <b>Επεμβάσεις:</b> {p["drone_flights"]}</div>', unsafe_allow_html=True)

# 7. Live Data
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
st.markdown(f"""
<div class="about-section">
    <b>ΟΣΠΡΙΑ ΧΑΣΙΩΝ (Καρπερό Γρεβενών)</b><br>
    Από το 2015, η οικογένειά μας καλλιεργεί με μεράκι 250 στρέμματα στην εύφορη γη των Χασίων. 
    Συνδυάζουμε την παράδοση με την τεχνολογία αιχμής των drones, προσφέροντας προϊόντα με μηδενικό περιβαλλοντικό αποτύπωμα, από το δικό μας <b>αγρόκτημα</b> στο πιάτο σας.
</div>
""", unsafe_allow_html=True)

# 10. Χάρτης (Light Mode)
st.markdown('<div class="section-header">🗺️ Τοποθεσία Αγροτεμαχίου</div>', unsafe_allow_html=True)
map_df = pd.DataFrame({'lat': [p['lat']], 'lon': [p['lon']]})
# Ο χάρτης θα πάρει αυτόματα το "Light" theme αν η εφαρμογή τρέχει σε light mode
st.map(map_df, zoom=11, use_container_width=True)

# 11. Αγρόκτημα Button
if st.button("⭐ Κλείστε Ξενάγηση στο Αγρόκτημα"):
    st.balloons()
    st.success("Η αίτηση εστάλη!")

st.markdown("<p style='text-align:center; font-size:10px; color:#999; margin-top:15px;'>ΟΣΠΡΙΑ ΧΑΣΙΩΝ DPP v15.1</p>", unsafe_allow_html=True)
