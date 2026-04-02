import streamlit as st
import pandas as pd
import numpy as np

# Ρύθμιση Σελίδας
st.set_page_config(page_title="Hasia Beans DPP", page_icon="🌱", layout="wide")

# ΠΛΗΡΕΣ CUSTOM CSS ΓΙΑ MOBILE APP LOOK
st.markdown("""
    <style>
    .main { background-color: #f4f7f1; }
    .app-header { background-color: #2e7d32; padding: 20px; border-radius: 0 0 20px 20px; color: white; text-align: center; margin-bottom: 20px; }
    .card { background-color: white; padding: 15px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 15px; border-left: 5px solid #2e7d32; }
    .metric-box { text-align: center; padding: 10px; background: #fff; border-radius: 10px; border: 1px solid #e0e0e0; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; border-radius: 25px; height: 50px; font-weight: bold; }
    h3 { color: #1b5e20; font-size: 1.1rem; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<div class="app-header"><h1>🌱 Ψηφιακό Διαβατήριο Οσπρίων</h1><p>Hasia Beans - Traceability System</p></div>', unsafe_allow_html=True)

# Κύριο Περιεχόμενο
col_main = st.columns([1])[0]

with col_main:
    # 1. Βασικές Πληροφορίες (Πάνω μέρος εικόνας)
    st.markdown(f"""
    <div class="card">
        <h3>📍 Τοποθεσία: Καρπερό, Χάσια</h3>
        <p><b>🆔 Διαβατήριο:</b> #OX-01-070 | <b>📦 Προϊόν:</b> Φασόλια Γίγαντες</p>
    </div>
    """, unsafe_allow_html=True)

    # 2. Πληροφορίες Παρτίδας
    st.markdown("""
    <div class="card">
        <h3>📋 Πληροφορίες Παρτίδας</h3>
        <p>• <b>Έκταση:</b> 250 στρέμματα</p>
        <p>• <b>Συγκομιδή:</b> Σεπτέμβριος 2025</p>
        <p>• <b>Αγροτεμάχιο:</b> 'Λιβάδια'</p>
        <p>• <b>Καλλιέργεια:</b> Βιολογική</p>
    </div>
    """, unsafe_allow_html=True)

    # 3. Ψεκασμός με Drone (Με "εικονικό" εικονίδιο)
    st.markdown("""
    <div class="card" style="border-left-color: #81c784;">
        <h3>🚁 Ψεκασμός με Drone (UAV)</h3>
        <p>• <b>Τελευταίος Ψεκασμός:</b> 10 Ιουλίου 2025</p>
        <p>• <b>Σκεύασμα:</b> Βιολογικό Εντομοκτόνο</p>
        <p>• <b>Αρ. Πτήσεων:</b> 5 επιτυχείς</p>
    </div>
    """, unsafe_allow_html=True)

    # 4. Ανάπτυξη Καλλιέργειας (3 Στήλες για Καιρό/Υγρασία)
    st.write("### 🌡️ Συνθήκες Καλλιέργειας")
    m1, m2, m3 = st.columns(3)
    with m1: st.markdown('<div class="metric-box">🌿<br><small>Φάση</small><br><b>Σπορά</b></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="metric-box">💧<br><small>Υγρασία</small><br><b>26%</b></div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="metric-box">☀️<br><small>Θερμ.</small><br><b>29°C</b></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 5. Χάρτης και Calculator (Τα ζήτησες να μείνουν!)
    st.write("### 🗺️ Χάρτης & Περιβάλλον")
    map_data = pd.DataFrame(np.random.randn(1, 2) / [200, 200] + [39.95, 21.62], columns=['lat', 'lon'])
    st.map(map_data)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    acres = st.slider("Υπολογισμός Οφέλους (Στρέμματα):", 1, 250, 100)
    benefit = acres * 0.12
    st.write(f"🍃 Μείωση πόρων: **{benefit:.2f} μονάδες**")
    st.markdown('</div>', unsafe_allow_html=True)

    # 6. Κουμπί Αγροτουρισμού
    if st.button("⭐ Book an Agrotourism Tour"):
        st.balloons()
        st.success("Η αίτηση εστάλη! Σας περιμένουμε στα Χάσια.")

# Footer πλοήγησης (για εφέ mobile app)
st.markdown("---")
st.caption("🏠 Αρχική | 📈 Παρακολούθηση | 📄 Αναφορές | 👤 Προφίλ")
