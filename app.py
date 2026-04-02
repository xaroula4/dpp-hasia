import streamlit as st
import pandas as pd
import numpy as np

# Ρύθμιση Σελίδας
st.set_page_config(page_title="Hasia Beans DPP", page_icon="🌱", layout="wide")

# CSS ΓΙΑ ΤΟ ΣΩΣΤΟ LAYOUT ΧΩΡΙΣ ΚΑΘΕΤΑ ΓΡΑΜΜΑΤΑ
st.markdown("""
    <style>
    .main { background-color: #f8f9f5; }
    .stApp { max-width: 500px; margin: 0 auto; background: white; padding: 10px; border-radius: 20px; }
    
    .header-style { background-color: #2e7d32; color: white; padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 15px; }
    .section-header { background-color: #1b5e20; color: white; padding: 8px 15px; border-radius: 10px; margin-top: 15px; font-weight: bold; }
    .info-card { background-color: #ffffff; padding: 12px; border-radius: 10px; border: 1px solid #eee; margin-top: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    
    /* ΔΙΟΡΘΩΣΗ ΓΙΑ ΤΙΣ ΚΑΡΤΕΣ ΑΝΑΠΤΥΞΗΣ */
    .stats-container { display: flex; justify-content: space-around; gap: 5px; margin-top: 10px; }
    .stat-card { background: white; border: 1px solid #e0e0e0; border-radius: 12px; padding: 10px; text-align: center; flex: 1; min-width: 90px; }
    .stat-icon { font-size: 20px; display: block; margin-bottom: 5px; }
    .stat-label { font-size: 11px; color: #666; display: block; }
    .stat-value { font-size: 13px; font-weight: bold; color: #1b5e20; display: block; }

    .stButton>button { background-color: #2e7d32; color: white; border-radius: 20px; width: 100%; font-weight: bold; border: none; height: 45px; }
    </style>
    """, unsafe_allow_html=True)

# 1. Header
st.markdown('<div class="header-style"><h2>🌱 Ψηφιακό Διαβατήριο</h2><p style="margin:0;">Όσπρια Χασίων | Hasia Beans</p></div>', unsafe_allow_html=True)

# 2. Τοποθεσία & ID
st.markdown("📍 **Καρπερό, Χάσια** | 📦 **Φασόλια Γίγαντες**")
st.info("🆔 Διαβατήριο: #OX-01-070")

# 3. Πληροφορίες Παρτίδας
st.markdown('<div class="section-header">📋 Πληροφορίες Παρτίδας</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-card">
    <p style="margin:2px;">• <b>Αρ. Παρτίδας:</b> OX-01-070</p>
    <p style="margin:2px;">• <b>Έκταση:</b> 250 στρέμματα</p>
    <p style="margin:2px;">• <b>Συγκομιδή:</b> Σεπτέμβριος 2025</p>
    <p style="margin:2px;">• <b>Καλλιέργεια:</b> Βιολογική</p>
</div>
""", unsafe_allow_html=True)

# 4. Ψεκασμός με Drone
st.markdown('<div class="section-header">🚁 Ψεκασμός με Drone (UAV)</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-card" style="border-left: 5px solid #81c784;">
    <p style="margin:2px;">• <b>Τελευταίος Ψεκασμός:</b> 10 Ιουλίου 2025</p>
    <p style="margin:2px;">• <b>Σκεύασμα:</b> Βιολογικό Εντομοκτόνο</p>
    <p style="margin:2px;">• <b>Αρ. Πτήσεων:</b> 5 επιτυχείς</p>
</div>
""", unsafe_allow_html=True)

# 5. Ανάπτυξη Καλλιέργειας - Η ΔΙΟΡΘΩΣΗ ΕΔΩ
st.markdown('<div class="section-header">🌡️ Ανάπτυξη Καλλιέργειας</div>', unsafe_allow_html=True)
st.markdown("""
<div class="stats-container">
    <div class="stat-card">
        <span class="stat-icon">🌱</span>
        <span class="stat-label">Φάση</span>
        <span class="stat-value">Σπορά</span>
    </div>
    <div class="stat-card">
        <span class="stat-icon">💧</span>
        <span class="stat-label">Υγρασία</span>
        <span class="stat-value">26%</span>
    </div>
    <div class="stat-card">
        <span class="stat-icon">☀️</span>
        <span class="stat-label">Θερμ.</span>
        <span class="stat-value">29°C</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 6. Χάρτης
st.markdown('<div class="section-header">🗺️ Χάρτης Καλλιέργειας (250 στρ.)</div>', unsafe_allow_html=True)
map_data = pd.DataFrame(np.random.randn(1, 2) / [300, 300] + [39.95, 21.62], columns=['lat', 'lon'])
st.map(map_data)

# 7. Calculator
st.markdown('<div class="section-header">🍃 Περιβαλλοντικό Όφελος</div>', unsafe_allow_html=True)
acres = st.slider("Επιλέξτε Στρέμματα:", 1, 250, 100)
st.write(f"Μείωση πόρων: **{acres * 0.12:.2f} μονάδες**")

# 8. Button
if st.button("⭐ Book an Agrotourism Tour"):
    st.balloons()
    st.success("Registration Successful!")

st.markdown("<br><p style='text-align:center; font-size:12px; color:#999;'>Αρχική | Παρακολούθηση | Αναφορές | Προφίλ</p>", unsafe_allow_html=True)
