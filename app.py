import streamlit as st
import pd
import numpy as np
import os

# Ρύθμιση Σελίδας
st.set_page_config(page_title="OSPRIA HASION DPP", page_icon="🌱", layout="wide")

# CSS ΓΙΑ ΤΟ ΤΕΛΙΚΟ ΕΠΑΓΓΕΛΜΑΤΙΚΟ LOOK
st.markdown("""
    <style>
    .main { background-color: #f8f9f5; }
    .stApp { max-width: 500px; margin: 0 auto; background: white; padding: 10px; border-radius: 20px; box-shadow: 0px 0px 20px rgba(0,0,0,0.1); }
    
    .header-style { background-color: #2e7d32; color: white; padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 15px; }
    .header-style h2 { margin: 0; font-size: 22px; }
    .header-style p { margin: 5px 0 0 0; font-size: 14px; font-weight: bold; text-transform: uppercase; }

    .section-header { background-color: #1b5e20; color: white; padding: 8px 15px; border-radius: 10px; margin-top: 15px; font-weight: bold; font-size: 15px; display: flex; align-items: center; gap: 8px; }
    .info-card { background-color: #ffffff; padding: 12px; border-radius: 10px; border: 1px solid #eee; margin-top: 5px; font-size: 14px; line-height: 1.6; }
    
    /* Eco Impact Box */
    .eco-box { background-color: #e1f5fe; padding: 12px; border-radius: 12px; border: 1px solid #01579b; color: #01579b; font-size: 13px; text-align: center; margin: 10px 0; font-weight: bold; }

    /* ΝΕΟ TIMELINE (Διαδρομή Προϊόντος) */
    .journey-container { display: flex; flex-direction: column; gap: 10px; padding: 10px 0; }
    .journey-step { display: flex; align-items: center; gap: 15px; padding: 10px; background: #f1f8e9; border-radius: 10px; border-left: 5px solid #2e7d32; }
    .step-icon { font-size: 20px; }
    .step-text { font-size: 13px; font-weight: 500; }

    /* Stats Container (Δίπλα-δίπλα) */
    .stats-container { display: flex; justify-content: space-between; gap: 8px; margin-top: 10px; }
    .stat-card { background: #f1f8e9; border: 1px solid #e0e0e0; border-radius: 12px; padding: 12px 5px; text-align: center; flex: 1; }
    .stat-card span { font-size: 20px; display: block; margin-bottom: 5px; }
    .stat-card small { font-size: 11px; color: #666; font-weight: bold; display: block; }
    .stat-card b { font-size: 15px; color: #1b5e20; display: block; margin-top: 2px; }

    .stButton>button { background-color: #2e7d32 !important; color: white !important; border-radius: 20px; width: 100%; font-weight: bold; height: 48px; border: none; }
    .bio-text { font-size: 10px; text-align: center; font-weight: bold; color: #333; margin-top: -10px; }
    </style>
    """, unsafe_allow_html=True)

# --- ΔΕΔΟΜΕΝΑ ---
products = {
    "Φακή Χασίων (Παρτίδα #OX-01)": {
        "producer": "Νικόλαος Παπαδόπουλος", "id": "#OX-01-066", "origin": "Καρπερό, Γρεβενά", "type": "Βιολογική",
        "phase": "Ανάπτυξη", "health": "96%", "temp": "28°C", "img": "fakes.JPEG", "bio_img": "bio.png", "show_bio": True,
        "drone_date": "05 Ιουνίου 2025", "drone_flights": "3 επιτυχείς",
        "eco": "💧 Μείωση νερού 40% μέσω UAV Precision Agriculture.",
        "video": "https://www.youtube.com/watch?v=m0md-5Wzp1E",
        "recipe": "🍲 <b>Σαλάτα Beluga:</b> Βράστε για 20', προσθέστε φρέσκο κρεμμυδάκι & βαλσάμικο.",
        "lat": 39.941, "lon": 21.632
    },
    "Φασόλια Γίγαντες (Παρτίδα #KT-05)": {
        "producer": "Δημήτριος Γεωργίου", "id": "#KT-05-070", "origin": "Καστοριά", "type": "Συμβατική",
        "phase": "Ωρίμανση", "health": "98%", "temp": "27°C", "img": "gigantes.png", "bio_img": "bio.png", "show_bio": False,
        "drone_date": "12 Ιουλίου 2025", "drone_flights": "6 επιτυχείς",
        "eco": "🚜 Μείωση CO2 κατά 35% λόγω στοχευμένου ψεκασμού.",
        "video": "https://www.youtube.com/watch?v=SKGdu1x0sxo",
        "recipe": "🥘 <b>Γίγαντες στο φούρνο:</b> Με φρέσκια ντομάτα, σέλινο και πολύ μεράκι!",
        "lat": 40.512, "lon": 21.261
    }
}

# 1. Header
st.markdown('<div class="header-style"><h2>🌱 Ψηφιακό Διαβατήριο</h2><p>ΟΣΠΡΙΑ ΧΑΣΙΩΝ / OSPRIA HASION</p></div>', unsafe_allow_html=True)

# 2. Selection
selected_prod = st.selectbox("Επιλέξτε Παρτίδα:", list(products.keys()), label_visibility="collapsed")
p = products[selected_prod]

# 3. Εικόνες & Bio
col1, col2 = st.columns([3, 1.2])
with col1:
    if os.path.exists(p['img']): st.image(p['img'], use_container_width=True)
with col2:
    if p['show_bio'] and os.path.exists(p['bio_img']):
        st.image(p['bio_img'], use_container_width=True)
        st.markdown('<p class="bio-text">HELLAS Agriculture<br>GR-BIO-007</p>', unsafe_allow_html=True)

# 4. Στοιχεία Παραγωγού & Eco Box
st.markdown('<div class="section-header">👨‍🌾 Στοιχεία Παραγωγού</div>', unsafe_allow_html=True)
st.markdown(f'<div class="info-card"><b>Παραγωγός:</b> {p["producer"]}<br><b>📍 {p["origin"]}</b></div>', unsafe_allow_html=True)
st.markdown(f'<div class="eco-box">🌍 {p["eco"]}</div>', unsafe_allow_html=True)

# 5. ΔΙΑΔΡΟΜΗ ΠΡΟΪΟΝΤΟΣ (Νέο Σχήμα)
st.markdown('<div class="section-header">📅 Διαδρομή Προϊόντος</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="journey-container">
    <div class="journey-step"><span class="step-icon">🚜</span><span class="step-text"><b>Σπορά:</b> Απρίλιος 2025</span></div>
    <div class="journey-step"><span class="step-icon">🚁</span><span class="step-text"><b>UAV Έλεγχος:</b> {p['drone_date']}</span></div>
    <div class="journey-step"><span class="step-icon">🧺</span><span class="step-text"><b>Συγκομιδή:</b> Σεπτέμβριος 2025 (Προβλεπόμενη)</span></div>
</div>
""", unsafe_allow_html=True)

# 6. Drone Footage & Data
st.markdown('<div class="section-header">🚁 Drone Spraying (Real Footage)</div>', unsafe_allow_html=True)
st.video(p['video'])
st.markdown(f'<div class="info-card" style="border-left: 5px solid #2e7d32;">• <b>Επεμβάσεις:</b> {p["drone_flights"]}</div>', unsafe_allow_html=True)

# 7. Live Data (Δίπλα-δίπλα)
st.markdown('<div class="section-header">🌡️ Live Κατάσταση (UAV Data)</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="stats-container">
    <div class="stat-card"><span>❤️</span><small>Υγεία</small><b>{p['health']}</b></div>
    <div class="stat-card"><span>🌿</span><small>Στάδιο</small><b>{p['phase']}</b></div>
    <div class="stat-card"><span>☀️</span><small>Καιρός</small><b>{p['temp']}</b></div>
</div>
""", unsafe_allow_html=True)

# 8. Συνταγή & Ιστορία
st.markdown('<div class="section-header">👩‍🍳 Πρόταση Μαγειρικής</div>', unsafe_allow_html=True)
st.markdown(f'<div class="info-card">{p["recipe"]}</div>', unsafe_allow_html=True)

st.markdown('<div class="section-header">🏠 Η Ιστορία μας</div>', unsafe_allow_html=True)
st.markdown('<div class="info-card"><b>ΟΣΠΡΙΑ ΧΑΣΙΩΝ</b>: Καλλιέργεια 250 στρ. με σεβασμό στη γη και τεχνολογία Drone.</div>', unsafe_allow_html=True)

# 9. Χάρτης
st.markdown('<div class="section-header">🗺️ Τοποθεσία Αγροτεμαχίου</div>', unsafe_allow_html=True)
map_data = pd.DataFrame({'lat': [p['lat']], 'lon': [p['lon']]})
st.map(map_data)

# 10. QR CODE (Fix)
st.markdown('<div class="section-header">📲 Scan for Origin</div>', unsafe_allow_html=True)
# Χρησιμοποιούμε QR κώδικα που δείχνει στο site σου
qr_url = f"https://chart.googleapis.com/chart?chs=150x150&cht=qr&chl=https://hasia-beans.streamlit.app&choe=UTF-8"
col_qr, col_txt = st.columns([1, 2])
with col_qr:
    st.image(qr_url, caption="Batch QR Code", width=120)
with col_txt:
    st.markdown("<p style='font-size:12px; margin-top:10px;'>Σκανάρετε το QR Code για να επαληθεύσετε την αυθεντικότητα της παρτίδας και να δείτε τα πλήρη εργαστηριακά δεδομένα.</p>", unsafe_allow_html=True)

if st.button("⭐ Κλείστε Ξενάγηση στο Κτήμα"):
    st.balloons()

st.markdown("<p style='text-align:center; font-size:10px; color:#999; margin-top:15px;'>ΟΣΠΡΙΑ ΧΑΣΙΩΝ DPP v13.0</p>", unsafe_allow_html=True)
