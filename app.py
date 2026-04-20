import streamlit as st
import pandas as pd
import numpy as np

# Ρύθμιση Σελίδας
st.set_page_config(page_title="Hasia Beans DPP", page_icon="🌱", layout="wide")

# ΠΡΟΧΩΡΗΜΕΝΟ CSS
st.markdown("""
    <style>
    .main { background-color: #f8f9f5; }
    .stApp { max-width: 500px; margin: 0 auto; background: white; padding: 10px; border-radius: 20px; box-shadow: 0px 0px 20px rgba(0,0,0,0.1); }
    .header-style { background-color: #2e7d32; color: white; padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 15px; }
    .section-header { background-color: #1b5e20; color: white; padding: 8px 15px; border-radius: 10px; margin-top: 15px; font-weight: bold; font-size: 14px; }
    .info-card { background-color: #ffffff; padding: 12px; border-radius: 10px; border: 1px solid #eee; margin-top: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .stats-container { display: flex; justify-content: space-around; gap: 5px; margin-top: 10px; }
    .stat-card { background: white; border: 1px solid #e0e0e0; border-radius: 12px; padding: 10px; text-align: center; flex: 1; }
    .stButton>button { background-color: #2e7d32; color: white; border-radius: 20px; width: 100%; font-weight: bold; height: 45px; }
    </style>
    """, unsafe_allow_html=True)

# --- ΔΕΔΟΜΕΝΑ ΠΡΟΪΟΝΤΩΝ ---
products = {
    "Φακή Χασίων": {
        "id": "#OX-01-066", "origin": "Καρπερό, Γρεβενά", "type": "Βιολογική",
        "date": "Ιούλιος 2025", "drone_flights": "3", "hum": "22%", "temp": "31°C",
        "story": "Καλλιεργείται στα 600μ. υψόμετρο με παραδοσιακές μεθόδους.",
        "img": "https://images.unsplash.com/photo-1515942400420-2b98fed1f515?w=400",
        "lat": 39.941, "lon": 21.632, "health_data": [85, 88, 92, 95, 98]
    },
    "Φασόλια Γίγαντες": {
        "id": "#OX-01-070", "origin": "Καστοριά", "type": "Συμβατική",
        "date": "Σεπτέμβριος 2025", "drone_flights": "6", "hum": "28%", "temp": "27°C",
        "story": "Οι περίφημοι γίγαντες Καστοριάς, γνωστοί για τη βραστερότητά τους.",
        "img": "https://images.unsplash.com/photo-1551462147-37885acc3c41?w=400",
        "lat": 40.512, "lon": 21.261, "health_data": [90, 89, 92, 91, 95]
    }
}

# 1. Header
st.markdown('<div class="header-style"><h2>🌱 Ψηφιακό Διαβατήριο</h2><p style="margin:0;">Όσπρια Χασίων | Hasia Beans</p></div>', unsafe_allow_html=True)

# 2. Επιλογή Προϊόντος
selected_prod = st.selectbox("Επιλέξτε Προϊόν:", list(products.keys()))
p = products[selected_prod]

# Φωτογραφία Προϊόντος
st.image(p['img'], use_container_width=True, caption=f"Προέλευση: {p['origin']}")

# 3. Πληροφορίες Παρτίδας
st.markdown('<div class="section-header">📋 Στοιχεία Προϊόντος</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="info-card">
    <p style="margin:2px;">• <b>ID:</b> {p['id']}</p>
    <p style="margin:2px;">• <b>Προέλευση:</b> {p['origin']}</p>
    <p style="margin:2px;">• <b>Συγκομιδή:</b> {p['date']}</p>
    <p style="margin:2px;">• <b>Τύπος:</b> {p['type']}</p>
    <hr>
    <p style="font-style: italic; font-size: 13px;">{p['story']}</p>
</div>
""", unsafe_allow_html=True)

# 4. Γράφημα Υγείας Καλλιέργειας (Από UAV)
st.markdown('<div class="section-header">📈 Υγεία Καλλιέργειας (UAV Monitoring)</div>', unsafe_allow_html=True)
chart_data = pd.DataFrame(p['health_data'], columns=["Δείκτης Υγείας %"])
st.line_chart(chart_data)

# 5. Ανάπτυξη Καλλιέργειας (Metrics)
st.markdown('<div class="stats-container">', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m1: st.markdown(f'<div class="stat-card">🌱<br><small>Drones</small><br><b>{p["drone_flights"]}</b></div>', unsafe_allow_html=True)
with m2: st.markdown(f'<div class="stat-card">💧<br><small>Υγρασία</small><br><b>{p["hum"]}</b></div>', unsafe_allow_html=True)
with m3: st.markdown(f'<div class="stat-card">☀️<br><small>Θερμ.</small><br><b>{p["temp"]}</b></div>', unsafe_allow_html=True)

# 6. Χάρτης
st.markdown('<div class="section-header">🗺️ Χάρτης Αγροτεμαχίου</div>', unsafe_allow_html=True)
st.map(pd.DataFrame({'lat': [p['lat']], 'lon': [p['lon']]}))

# 7. Περιβαλλοντικό Όφελος
st.markdown('<div class="section-header">🍃 Eco-Calculator</div>', unsafe_allow_html=True)
acres = st.slider("Στρέμματα:", 1, 250, 100)
st.write(f"Μείωση αποτυπώματος: **{acres * 0.12:.2f} units**")

# 8. Button
if st.button("⭐ Book an Agrotourism Tour"):
    st.balloons()
    st.success("Registration Successful!")

st.markdown("<br><p style='text-align:center; font-size:11px; color:#999;'>© 2026 Hasia Beans Digital Systems</p>", unsafe_allow_html=True)
