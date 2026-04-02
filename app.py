import streamlit as st
import pandas as pd

# =========================
# ΡΥΘΜΙΣΕΙΣ ΣΕΛΙΔΑΣ
# =========================
st.set_page_config(
    page_title="Digital Product Passport - Όσπρια Χασίων",
    page_icon="🌱",
    layout="wide"
)

# =========================
# ΔΕΔΟΜΕΝΑ ΠΑΡΤΙΔΩΝ
# =========================
batch_data = {
    "OX-2024": {
        "product_name": "Φασόλια Ορεινής Καλλιέργειας",
        "variety": "Μέτρια λευκή ποικιλία",
        "sowing_date": "2024-03-18",
        "location": "Χάσια, Γρεβενά",
        "area": "250 στρέμματα",
        "harvest_date": "2024-09-12",
        "uav_spraying_data": "Ψεκασμός UAV στις 2024-05-10, βιοδιεγέρτης φυλλώματος, ύψος πτήσης 3.2 μ.",
        "farmer_notes": "Καλλιέργεια με έμφαση στη βιωσιμότητα και την ορθολογική χρήση εισροών.",
        "traceability_table": pd.DataFrame(
            [
                ["2024-03-18", "Σπορά", "Αγροτεμάχιο Α1, Χάσια", "Πιστοποιημένος σπόρος"],
                ["2024-04-05", "Έλεγχος φυτρώματος", "Αγροτεμάχιο Α1, Χάσια", "Ομοιόμορφη εγκατάσταση"],
                ["2024-05-10", "Ψεκασμός UAV", "Αγροτεμάχιο Α1, Χάσια", "Βιοδιεγέρτης φυλλώματος"],
                ["2024-07-01", "Επιτόπιος έλεγχος", "Αγροτεμάχιο Α1, Χάσια", "Καλή φυτοϋγεία"],
                ["2024-09-12", "Συγκομιδή", "Αγροτεμάχιο Α1, Χάσια", "Υγρασία εντός ορίων"],
            ],
            columns=["Ημερομηνία", "Ενέργεια", "Τοποθεσία", "Σημειώσεις"]
        )
    },
    "FA-2024": {
        "product_name": "Φακές Παραδοσιακής Καλλιέργειας",
        "variety": "Μικρόσπερμη",
        "sowing_date": "2024-02-28",
        "location": "Χάσια, Γρεβενά",
        "area": "250 στρέμματα",
        "harvest_date": "2024-07-22",
        "uav_spraying_data": "Ψεκασμός UAV στις 2024-04-18, διαφυλλική θρέψη, ύψος πτήσης 2.8 μ.",
        "farmer_notes": "Παρακολούθηση καλλιέργειας με σύγχρονες πρακτικές γεωργίας ακριβείας.",
        "traceability_table": pd.DataFrame(
            [
                ["2024-02-28", "Σπορά", "Αγροτεμάχιο Β2, Χάσια", "Καλή προετοιμασία εδάφους"],
                ["2024-03-20", "Πρώτη αξιολόγηση", "Αγροτεμάχιο Β2, Χάσια", "Κανονική ανάπτυξη"],
                ["2024-04-18", "Ψεκασμός UAV", "Αγροτεμάχιο Β2, Χάσια", "Διαφυλλική θρέψη"],
                ["2024-06-10", "Έλεγχος ωρίμανσης", "Αγροτεμάχιο Β2, Χάσια", "Ομοιομορφία στο χωράφι"],
                ["2024-07-22", "Συγκομιδή", "Αγροτεμάχιο Β2, Χάσια", "Ποιοτικά χαρακτηριστικά πολύ καλά"],
            ],
            columns=["Ημερομηνία", "Ενέργεια", "Τοποθεσία", "Σημειώσεις"]
        )
    },
    "RE-2024": {
        "product_name": "Ρεβίθια Ξηρικής Καλλιέργειας",
        "variety": "Παραδοσιακή ελληνική",
        "sowing_date": "2024-03-10",
        "location": "Χάσια, Γρεβενά",
        "area": "250 στρέμματα",
        "harvest_date": "2024-08-30",
        "uav_spraying_data": "Ψεκασμός UAV στις 2024-05-03, θρεπτικό διάλυμα ιχνοστοιχείων, ύψος πτήσης 3.0 μ.",
        "farmer_notes": "Στόχος η παραγωγή σταθερής ποιότητας με διαφάνεια σε όλα τα στάδια.",
        "traceability_table": pd.DataFrame(
            [
                ["2024-03-10", "Σπορά", "Αγροτεμάχιο Γ3, Χάσια", "Ελεγχόμενη σπορά"],
                ["2024-04-02", "Παρακολούθηση ανάπτυξης", "Αγροτεμάχιο Γ3, Χάσια", "Ικανοποιητική εικόνα"],
                ["2024-05-03", "Ψεκασμός UAV", "Αγροτεμάχιο Γ3, Χάσια", "Ιχνοστοιχεία"],
                ["2024-07-15", "Προ συγκομιστικός έλεγχος", "Αγροτεμάχιο Γ3, Χάσια", "Καλή ωρίμανση"],
                ["2024-08-30", "Συγκομιδή", "Αγροτεμάχιο Γ3, Χάσια", "Έτοιμο για τυποποίηση"],
            ],
            columns=["Ημερομηνία", "Ενέργεια", "Τοποθεσία", "Σημειώσεις"]
        )
    }
}

# =========================
# STYLING
# =========================
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.3rem;
        font-weight: 700;
        color: #2e5e3e;
        margin-bottom: 0.3rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 1.5rem;
    }
    .info-card {
        background-color: #f7fbf7;
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #dcebdc;
        margin-bottom: 1rem;
    }
    .section-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #2e5e3e;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# HEADER
# =========================
st.markdown('<div class="main-title">🌱 Digital Product Passport, Όσπρια Χασίων</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Διαφάνεια, ιχνηλασιμότητα και ιστορία παραγωγής για κάθε παρτίδα προϊόντος.</div>',
    unsafe_allow_html=True
)

# =========================
# SIDEBAR
# =========================
st.sidebar.header("Αναζήτηση Παρτίδας")
batch_number = st.sidebar.text_input("Εισαγωγή Batch Number", value="OX-2024")
st.sidebar.markdown("Δοκίμασε: `OX-2024`, `FA-2024`, `RE-2024`")

st.sidebar.markdown("---")
st.sidebar.subheader("Σχετικά με την εφαρμογή")
st.sidebar.write(
    "Η εφαρμογή παρουσιάζει πληροφορίες ιχνηλασιμότητας, στοιχεία καλλιέργειας και το ψηφιακό αφήγημα της οικογενειακής επιχείρησης."
)

# =========================
# ΑΝΑΖΗΤΗΣΗ BATCH
# =========================
batch = batch_data.get(batch_number.strip().upper())

if batch:
    st.success(f"Βρέθηκε η παρτίδα: {batch_number.strip().upper()}")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="section-title">📦 Στοιχεία Προϊόντος</div>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="info-card">
                <b>Προϊόν:</b> {batch['product_name']}<br>
                <b>Ποικιλία:</b> {batch['variety']}<br>
                <b>Τοποθεσία:</b> {batch['location']}<br>
                <b>Έκταση:</b> {batch['area']}<br>
                <b>Ημερομηνία Σποράς:</b> {batch['sowing_date']}<br>
                <b>Ημερομηνία Συγκομιδής:</b> {batch['harvest_date']}<br>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown('<div class="section-title">🚁 Δεδομένα Ψεκασμού από UAV</div>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="info-card">
                {batch['uav_spraying_data']}
            </div>
            """,
            unsafe_allow_html=True
        )

    # =========================
    # ΙΧΝΗΛΑΣΙΜΟΤΗΤΑ
    # =========================
    st.markdown('<div class="section-title">🔎 Ενότητα Ιχνηλασιμότητας</div>', unsafe_allow_html=True)

    st.dataframe(
        batch["traceability_table"],
        use_container_width=True,
        hide_index=True
    )

    # =========================
    # EXTRA ΠΛΗΡΟΦΟΡΙΕΣ
    # =========================
    st.markdown('<div class="section-title">📝 Σημειώσεις Παραγωγού</div>', unsafe_allow_html=True)
    st.info(batch["farmer_notes"])

else:
    st.error("Δεν βρέθηκε παρτίδα με αυτόν τον Batch Number.")
    st.write("Δοκίμασε έναν από τους διαθέσιμους κωδικούς: `OX-2024`, `FA-2024`, `RE-2024`")

# =========================
# DIGITAL STORYTELLING
# =========================
st.markdown('<div class="section-title">📖 Digital Storytelling</div>', unsafe_allow_html=True)

story_col1, story_col2 = st.columns([1.4, 1])

with story_col1:
    st.markdown(
        """
        <div class="info-card">
        Η οικογένειά μας καλλιεργεί τη γη στα Χάσια εδώ και γενιές, με σεβασμό στην παράδοση,
        αλλά και με το βλέμμα στραμμένο στο αύριο. Στα 250 στρέμματα της εκμετάλλευσης,
        η παραγωγή οσπρίων συνδυάζει γνώση, εμπειρία και σύγχρονα εργαλεία, όπως η παρακολούθηση
        καλλιεργειών και οι εφαρμογές UAV.

        Κάθε παρτίδα προϊόντος αποκτά τη δική της ψηφιακή ταυτότητα. Έτσι, ο καταναλωτής μπορεί
        να γνωρίζει από πού προέρχεται το προϊόν, πότε σπάρθηκε, πώς παρακολουθήθηκε και ποια ήταν
        η διαδρομή του από το χωράφι μέχρι τη συσκευασία.

        Με αυτόν τον τρόπο, το προϊόν δεν είναι απλώς ένα σακουλάκι με όσπρια. Είναι μια ιστορία,
        ένα χωράφι, μια οικογένεια, ένας τόπος.
        </div>
        """,
        unsafe_allow_html=True
    )

with story_col2:
    st.markdown("#### Φωτογραφίες από την καλλιέργεια")
    st.caption("Αν προσθέσεις δικές σου εικόνες στον φάκελο `images/`, θα εμφανιστούν εδώ.")

    # Προσπάθεια φόρτωσης τοπικών εικόνων
    image_files = [
        "images/field_1.jpg",
        "images/field_2.jpg",
        "images/family_story.jpg"
    ]

    shown_any_image = False
    for img_path in image_files:
        try:
            st.image(img_path, use_container_width=True)
            shown_any_image = True
        except Exception:
            pass

    if not shown_any_image:
        st.warning("Δεν βρέθηκαν εικόνες. Πρόσθεσε αρχεία εικόνας στον φάκελο `images/`.")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Digital Product Passport για επιχείρηση οσπρίων, Streamlit demo εφαρμογή.")
