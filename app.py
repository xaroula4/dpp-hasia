import streamlit as st
import pandas as pd

# Ρύθμιση σελίδας για εμφάνιση και εικονίδιο
st.set_page_config(page_title="Όσπρια Χασίων DPP", page_icon="🌱", layout="wide")

# Προσαρμοσμένο CSS για να φύγει η "μαυρίλα" και να γίνει πιο "αγροτικό"
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f1;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
    }
    h1 {
        color: #2e7d32;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stAlert {
        background-color: #e8f5e9;
        border: 1px solid #c8e6c9;
    }
    </style>
    """, unsafe_allow_html=True)

# Τίτλος και Storytelling Header
st.title("🌱 Digital Product Passport (DPP)")
st.header("Οικογένεια Χασίων: Από το 2015 με σεβασμό στη γη")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### 🚜 Η Παραγωγή μας
    Στα **250 ιδιόκτητα στρέμματά μας** στα Χάσια, συνδυάζουμε την παράδοση με την τεχνολογία. 
    Χρησιμοποιούμε **UAVs (Drones)** για τον ψεκασμό ακριβείας, εξασφαλίζοντας μηδενική σπατάλη πόρων.
    """)

with col2:
    st.info("📍 Τοποθεσία: Καρπερό Χασίων\n\n🛡️ Πιστοποίηση: ISO 22000")

st.divider()

# Δεδομένα από τον κατάλογό σου
data = {
    "Batch ID": ["OX-01-066", "OX-01-070", "OX-01-085"],
    "Προϊόν": ["Φακές Γρεβενών (500g)", "Φασόλια Γίγαντες (500g)", "Ρεβύθια Χοντρά (500g)"],
    "Καλλιέργεια": ["Συμβατική", "Βιολογική", "Συμβατική"],
    "Ημερ. Συγκομιδής": ["Αύγουστος 2025", "Σεπτέμβριος 2025", "Ιούλιος 2025"],
    "Πτήσεις Drone (UAV)": ["3 επιτυχείς", "5 επιτυχείς", "2 επιτυχείς"],
    "Ανάλυση Εδάφους": ["Άριστη", "Υψηλή Αζωτοδέσμευση", "Άριστη"]
}
df = pd.DataFrame(data)

# Αναζήτηση Παρτίδας
search_id = st.text_input("🔍 Σκανάρετε ή πληκτρολογήστε τον κωδικό παρτίδας (π.χ. OX-01-070):")

if search_id:
    res = df[df["Batch ID"] == search_id]
    if not res.empty:
        st.success(f"Βρέθηκαν στοιχεία για το προϊόν: **{res['Προϊόν'].values[0]}**")
        
        # Εμφάνιση στοιχείων σε κάρτες
        c1, c2, c3 = st.columns(3)
        c1.metric("Μέθοδος", res["Καλλιέργεια"].values[0])
        c2.metric("UAV Monitoring", res["Πτήσεις Drone (UAV)"].values[0])
        c3.metric("Ποιότητα Εδάφους", res["Ανάλυση Εδάφους"].values[0])
        
        st.write("### 📊 Πλήρης Ιχνηλασιμότητα")
        st.dataframe(res, use_container_width=True)
        
        st.write("### 🏺 Digital Storytelling & Αγροτουρισμός")
        st.write("Αυτό το προϊόν προέρχεται από το αγροτεμάχιο 'Λιβάδια'. Θέλετε να δείτε από κοντά τη συγκομιδή;")
        if st.button("Κλείστε μια ξενάγηση στο κτήμα"):
            st.balloons()
            st.write("Σας περιμένουμε στα Χάσια!")
    else:
        st.warning("Ο κωδικός δεν βρέθηκε. Δοκιμάστε OX-01-070")

st.sidebar.image("https://via.placeholder.com/150?text=Logo+Hasia", caption="Όσπρια Χασίων")
st.sidebar.markdown("---")
st.sidebar.write("© 2026 - Ψηφιακό Διαβατήριο Προϊόντος")
