import streamlit as st
import pandas as pd
import numpy as np

# Ρύθμιση σελίδας
st.set_config(page_title="Hasia Beans DPP", page_icon="🚜", layout="wide")

# Custom CSS για επαγγελματικό Look
st.markdown("""
    <style>
    .main { background-color: #f0f2f0; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    h1, h2 { color: #1b5e20; font-family: 'Segoe UI', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Επιλογή Γλώσσας
lang = st.sidebar.radio("Γλώσσα / Language", ["Ελληνικά", "English"])

texts = {
    "Ελληνικά": {"title": "Ψηφιακό Διαβατήριο Προϊόντος", "desc": "Ιχνηλασιμότητα με χρήση UAVs & Drones", "btn": "Κράτηση Επίσκεψης"},
    "English": {"title": "Digital Product Passport", "desc": "Traceability via UAVs & Precision Farming", "btn": "Book a Tour"}
}

st.title(f"🌱 {texts[lang]['title']}")
st.write(f"**{texts[lang]['desc']}** | Όσπρια Χασίων - Από το 2015")

# --- SECTION 1: ΧΑΡΤΗΣ (Visual Aid) ---
st.subheader("📍 Τοποθεσία Καλλιέργειας (250 Στρέμματα)")
# Δημιουργία τυχαίων σημείων γύρω από το Καρπερό για το εφέ του χάρτη
map_data = pd.DataFrame(
    np.random.randn(5, 2) / [100, 100] + [39.95, 21.62],
    columns=['lat', 'lon']
)
st.map(map_data)

st.divider()

# --- SECTION 2: ΙΧΝΗΛΑΣΙΜΟΤΗΤΑ ---
col1, col2 = st.columns([1, 2])

with col1:
    st.write("### 🔍 Search Batch")
    search_id = st.text_input("Batch ID:", value="OX-01-070")
    
with col2:
    # Δεδομένα
    df = pd.DataFrame({
        "Batch ID": ["OX-01-066", "OX-01-070", "OX-01-085"],
        "Product": ["Lentils", "Giant Beans", "Chickpeas"],
        "UAV_Health_Index": ["98%", "95%", "92%"],
        "Water_Savings": ["20%", "25%", "18%"]
    })
    
    res = df[df["Batch ID"] == search_id]
    if not res.empty:
        c1, c2 = st.columns(2)
        c1.metric("Plant Health (UAV)", res["UAV_Health_Index"].values[0])
        c2.metric("Water Savings", res["Water_Savings"].values[0])
        st.table(res)

st.divider()

# --- SECTION 3: CALCULATOR (Απαιτείται από την εκφώνηση) ---
st.subheader("🧮 Υπολογιστής Περιβαλλοντικού Οφέλους")
acres = st.slider("Επιλέξτε Στρέμματα:", 1, 250, 100)
reduction = acres * 0.15 # Έστω 15% λιγότερο φάρμακο λόγω drones
st.write(f"Με τη χρήση UAV στα {acres} στρέμματα, μειώσατε τη χρήση πόρων κατά **{reduction:.2f} μονάδες**.")

if st.button(texts[lang]['btn']):
    st.balloons()
    st.success("Registration Successful!")
