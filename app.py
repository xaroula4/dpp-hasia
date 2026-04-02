import streamlit as st
import pandas as pd
import numpy as np

# Ρύθμιση Σελίδας
st.set_page_config(page_title="Hasia Beans DPP", page_icon="🌱", layout="wide")

# ΠΡΟΧΩΡΗΜΕΝΟ CSS ΓΙΑ ΕΠΑΓΓΕΛΜΑΤΙΚΟ UI
st.markdown("""
    <style>
    .main { background-color: #f8f9f5; }
    .stApp { max-width: 500px; margin: 0 auto; border: 1px solid #ddd; border-radius: 30px; padding: 10px; background: white; } /* Mobile Frame Εφέ */
    .header-style { background-color: #2e7d32; color: white; padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 15px; }
    .section-header { background-color: #1b5e20; color: white; padding: 8px 15px; border-radius: 10px; margin-top: 15px; font-size: 14px; font-weight: bold; }
    .info-card { background-color: #ffffff; padding: 12px; border-radius: 10px; border: 1px solid #eee; margin-top: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .metric-container { display: flex; justify-content: space-between; margin-top: 10px; }
    .metric-card { background: #fff; border: 1px solid #e0e0e0; border-radius: 12px; padding: 10px; text-align: center; width: 31%; }
    .stButton>button { background-color: #2e7d32; color: white; border-radius: 20px; border: none; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 1. Header (Όπως στην εικόνα)
st.markdown('<div class="header-style"><h2>🌱 Ψηφιακό Διαβατήριο</h2><p style="margin:0;">Όσπρια Χασίων | Hasia Beans</p></div>', unsafe_allow_html=True)

# 2. Τοποθεσία & ID (Quick Info)
col_a, col_b = st.columns(2)
with col_a: st.caption("📍 Καρπερό, Χάσια")
with col_b: st.caption("📦 Φασόλια Γίγαντες")
st.markdown("**🆔 Διαβατήριο: #OX-01-070**")

# 3. Πληροφορίες Παρτίδας (Section)
st.markdown('<div class="section-header">📋 Πληροφορίες Παρτίδας</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-card">
    <p style="margin:2px;">• <b>Αρ. Παρτίδας:</b> OX-01-070</p>
    <p style="margin:2px;">• <b>Έκταση:</b> 250 στρέμματα</p>
    <p style="margin:2px;">• <b>Συγκομιδή:</b> Σεπτέμβριος 2025</p>
    <p style="margin:2px;">• <b>Καλλιέργεια:</b> Βιολογική</p>
</div>
""", unsafe_allow_html=True)

# 4. Ψεκασμός με Drone (Section)
st.markdown('<div class="section-header">🚁 Ψεκασμός με Drone (UAV)</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-card" style="border-left: 5px solid #81c784;">
    <p style="margin:2px;">• <b>Τελευταίος Ψεκασμός:</b> 10 Ιουλίου 2025</p>
    <p style="margin:2px;">• <b>Σκεύασμα:</b> Βιολογικό Εντομοκτόνο</p>
    <p style="margin:2px;">• <b>Αρ. Πτήσεων:</b> 5 επιτυχείς</p>
</div>
""", unsafe_allow_html=True)

# 5. Ανάπτυξη Καλλιέργειας (Metrics)
st.markdown('<div class="section-header">🌡️ Ανάπτυξη Καλλιέργειας</div>', unsafe_allow_html=True)
m1, m2, m3 = st.columns(3)
with m1: st.markdown('<div class="metric-card"><span style="font-size:20px;">🌱</span><br><small>Φάση</small><br><b>Σπορά</b></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="metric-card"><span style="font-size:20px;">💧</span><br><small>Υγρασία</small><br><b>26%</b></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="metric-card"><span style="font-size:20px;">☀️</span><br><small>Θερμ.</small><br><b>29°C</b></div>', unsafe_allow_html=True)

# 6. Χάρτης & Calculator (Τα διατηρούμε για την εργασία)
st.markdown('<div class="section-header">🗺️ Χάρτης Καλλιέργειας (250 στρ.)</div>', unsafe_allow_html=True)
map_data = pd.DataFrame(np.random.randn(1, 2) / [250, 250] + [39.95, 21.62], columns=['lat', 'lon'])
st.map(map_data)

st.markdown('<div class="section-header">🍃 Περιβαλλοντικό Όφελος</div>', unsafe_allow_html=True)
acres = st.slider("Επιλέξτε Στρέμματα:", 1, 250, 100)
st.write(f"Μείωση πόρων: **{acres * 0.12:.2f} μονάδες**")

# 7. Κουμπί Αγροτουρισμού (Μπαλόνια!)
if st.button("⭐ Book an Agrotourism Tour"):
    st.balloons()
    st.success("Registration Successful!")

# Mobile-like Footer
st.markdown("<br><p style='text-align:center; font-size:12px; color:#999;'>Αρχική | Παρακολούθηση | Αναφορές | Προφίλ</p>", unsafe_allow_html=True)
