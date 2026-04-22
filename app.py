import streamlit as st
import pandas as pd
import numpy as np

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
    .stat-card { background: #f1f8e9; border: 1px solid #e0e0e0; border-radius: 12px; padding: 10px; text-align: center; flex: 1; min-width: 90px; }
    .stButton>button { background-color: #2e7d32; color: white; border-radius: 20px; width: 100%; font-weight: bold; height: 45px; border: none; }
    .about-section { background-color: #e8f5e9; padding: 15px; border-radius: 15px; border-left: 5px solid #2e7d32; margin-top: 20px; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

# --- ΔΕΔΟΜΕΝΑ ΠΡΟΪΟΝΤΩΝ ---
products = {
    "Φακή Χασίων": {
        "id": "#OX-01-066", "origin": "Καρπερό, Γρεβενά", "type": "Βιολογική",
        "date": "Ιούλιος 2025", "drone_date": "05 Ιουνίου 2025", "drone_flights": "3 επιτυχείς", 
        "drone_tool": "Βιολογικό Εντομοκτόνο", "phase": "Ανάπτυξη", "hum": "22%", "temp": "31°C", 
        "health": "96%", "img": "fakes.JPEG", "lat": 39.941, "lon": 21.632,
        "video": "https://www.youtube.com/watch?v=m0md-5Wzp1E",
        "certs": "🛡️ Bio Hellas | 🌿 ISO 22000"
    },
    "Φασόλια Γίγαντες": {
        "id": "#OX-01-070", "origin": "Καστοριά", "type": "Συμβατική",
        "date": "Σεπτέμβριος 2025", "drone_date": "12 Ιουλίου 2025", "drone_flights": "6 επιτυχείς", 
        "drone_tool": "Εγκεκριμένο Σκεύασμα", "phase": "Ωρίμανση", "hum": "28%", "temp": "27°C", 
        "health": "98%", "img": "gigantes.png", "lat": 40.512, "lon": 21.261,
        "video": "https://www.youtube.com/watch?v=SKGdu1x0sxo",
        "certs": "🛡️ Global GAP | 🌿 ISO 22000"
    }
}

# 1. Header
st.markdown('<div class="header-style"><h2>🌱 Ψηφιακό Διαβατήριο</h2><p style="margin:0;">Όσπρια Χασίων | Hasia Beans</p></div>', unsafe_allow_html=True)

# 2. Επιλογή Προϊόντος
selected_prod = st.selectbox("Επιλέξτε Προϊόν:", list(products.keys()))
p = products[selected_prod]

# Εικόνα Συσκευασίας
st.image(p['img'], use_container_width=True)

# 3. Πληροφορίες Παρτίδας
st.markdown('<div class="section-header">📋 Πληροφορίες Παρτίδας</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="info-card">
    <p style="margin:2px;">• <b>ID:</b> {p['id']}</p>
    <p style="margin:2px;">• <b>Προέλευση:</b> {p['origin']}</p>
    <p style="margin:2px;">• <b>Καλλιέργεια:</b> {p['type']}</p>
    <p style="margin:2px;">• <b>Πιστοποιήσεις:</b> {p['certs']}</p>
</div>
""", unsafe_allow_html=True)

# 4. Βίντεο Ψεκασμού
st.markdown('<div class="section-header">🚁 Drone Spraying (Real Footage)</div>', unsafe_allow_html=True)
st.video(p['video'])

# 5. Live UAV Data
st.markdown('<div class="section-header">🌡️ Live UAV Data</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="stats-container">
    <div class="stat-card">🌱<br><small>Στάδιο</small><br><b>{p['phase']}</b></div>
    <div class="stat-card">❤️<br><small>Υγεία</small><br><b style="color:#2e7d32;">{p['health']}</b></div>
    <div class="stat-card">💧<br><small>Υγρασία</small><br><b>{p['hum']}</b></div>
</div>
""", unsafe_allow_html=True)

# 6. Χάρτης
st.markdown('<div class="section-header">🗺️ Χάρτης Αγροτεμαχίου</div>', unsafe_allow_html=True)
st.map(pd.DataFrame({'lat': [p['lat']], 'lon': [p['lon']]}))

# 7. Η ΙΣΤΟΡΙΑ ΜΑΣ (About Us)
st.markdown('<div class="section-header">🏠 Ποιοι Είμαστε</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="about-section">
    <b>Οικογένεια Χασίων</b><br>
    Από το 2015, καλλιεργούμε με μεράκι στα 250 στρέμματά μας στο Καρπερό. 
    Συνδυάζουμε την παράδοση με την τεχνολογία UAV για να φέρουμε στο πιάτο σας 
    όσπρια υψηλής θρεπτικής αξίας με μηδενικό περιβαλλοντικό αποτύπωμα.
</div>
""", unsafe_allow_html=True)

# 8. Button & Balloons
st.markdown("<br>", unsafe_allow_html=True)
if st.button("⭐ Κλείστε Ξενάγηση στο Κτήμα"):
    st.balloons()
    st.success("Η αίτηση εστάλη! Σας περιμένουμε στα Χάσια.")

st.markdown("<p style='text-align:center; font-size:11px; color:#999; margin-top:20px;'>Αρχική | Παρακολούθηση | Προφίλ</p>", unsafe_allow_html=True)
