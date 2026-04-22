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
    
    /* Header Διορθωμένο */
    .header-style { background-color: #2e7d32; color: white; padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 15px; }
    .section-header { background-color: #1b5e20; color: white; padding: 8px 15px; border-radius: 10px; margin-top: 15px; font-weight: bold; font-size: 14px; }
    .info-card { background-color: #ffffff; padding: 12px; border-radius: 10px; border: 1px solid #eee; margin-top: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    
    /* ΔΙΟΡΘΩΣΗ ΚΑΡΤΩΝ */
    .stats-container { display: flex; justify-content: space-around; gap: 5px; margin-top: 10px; }
    .stat-card { background: white; border: 1px solid #e0e0e0; border-radius: 12px; padding: 10px; text-align: center; flex: 1; min-width: 90px; }
    .stat-icon { font-size: 20px; display: block; margin-bottom: 5px; }
    .stat-label { font-size: 11px; color: #666; display: block; }
    .stat-value { font-size: 13px; font-weight: bold; color: #1b5e20; display: block; }
    .stButton>button { background-color: #2e7d32; color: white; border-radius: 20px; width: 100%; font-weight: bold; border: none; height: 45px; }
    </style>
    """, unsafe_allow_html=True)

# --- ΔΕΔΟΜΕΝΑ ΠΡΟΪΟΝΤΩΝ ---
products = {
    "Φακή Χασίων": {
        "id": "#OX-01-066", "origin": "Καρπερό, Γρεβενά", "type": "Βιολογική",
        "date": "Ιούλιος 2025", "drone_flights": "3 επιτυχείς", "hum": "22%", "temp": "31°C",
        "img": "fakes.JPEG", "bio_logo": "Image.jpg", # Προσθήκη σήματος
        "lat": 39.941, "lon": 21.632
    },
    "Φασόλια Γίγαντες": {
        "id": "#OX-01-070", "origin": "Καστοριά", "type": "Συμβατική",
        "date": "Σεπτέμβριος 2025", "drone_flights": "6 επιτυχείς", "hum": "28%", "temp": "27°C",
        "img": "gigantes.png", "bio_logo": None, # Δεν έχει σήμα
        "lat": 40.512, "lon": 21.261
    }
}

# 1. Header (Εδώ εμφανίζεται σωστά το Όσπρια Χασίων)
st.markdown('<div class="header-style"><h2>🌱 Ψηφιακό Διαβατήριο</h2><p style="margin:0;">Όσπρια Χασίων | Hasia Beans</p></div>', unsafe_allow_html=True)

# 2. Επιλογή Προϊόντος
selected_prod = st.selectbox("Επιλέξτε Προϊόν:", list(products.keys()))
p = products[selected_prod]

# 3. Εικόνες (Συσκευασία + Σήμα Bio)
# Χρησιμοποιούμε στήλες για να βάλουμε το σήμα BioHellas δίπλα στη συσκευασία
col_img, col_bio = st.columns([3, 1])
with col_img:
    try:
        st.image(p['img'], use_container_width=True)
    except:
        st.error(f"⚠️ Ανεβάστε το αρχείο {p['img']} στο GitHub.")
with col_bio:
    if p['bio_logo'] and os.path.exists(p['bio_logo']):
        st.image(p['bio_logo'], caption="GR-BIO-007", use_container_width=True)

# 4. Πληροφορίες Παρτίδας
st.markdown('<div class="section-header">📋 Πληροφορίες Παρτίδας</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="info-card">
    <p style="margin:2px;">• <b>ID:</b> {p['id']}</p>
    <p style="margin:2px;">• <b>Προέλευση:</b> {p['origin']}</p>
    <p style="margin:2px;">• <b>Συγκομιδή:</b> {p['date']}</p>
    <p style="margin:2px;">• <b>Καλλιέργεια:</b> {p['type']}</p>
</div>
""", unsafe_allow_html=True)

# 5. Ανάπτυξη Καλλιέργειας (Σωστό Layout)
st.markdown('<div class="section-header">🌡️ Ανάπτυξη Καλλιέργειας</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="stats-container">
    <div class="stat-card">
        <span class="stat-icon">🌱</span>
        <span class="stat-label">Drones</span>
        <span class="stat-value">{p['drone_flights']}</span>
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

# 6. Χάρτης (Ενημερώνεται βάσει προϊόντος)
st.markdown('<div class="section-header">🗺️ Χάρτης Αγροτεμαχίου</div>', unsafe_allow_html=True)
map_data = pd.DataFrame({'lat': [p['lat']], 'lon': [p['lon']]})
st.map(map_data)

# 7. Button
if st.button("⭐ Book an Agrotourism Tour"):
    st.balloons()
    st.success("Registration Successful!")

st.markdown("<br><p style='text-align:center; font-size:11px; color:#999;'>Αρχική | Παρακολούθηση | Αναφορές | Προφίλ</p>", unsafe_allow_html=True)
