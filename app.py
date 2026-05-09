
import streamlit as st
import qrcode
from PIL import Image   # ✅ OK (can keep, not causing issue)

st.title("Feedback App")
st.write("Scan the QR code of submit feedback below")

app_url = "https://feedbackapp-o7zojj5aw7mfuw5whdphg8.streamlit.app"

qr = qrcode.make(app_url)
qr.save("qr.png")  
# ✅ OPTIONAL FIX (recommended):
# Wrap the above two lines in:
# if not Path("qr.png").exists():

import csv
from pathlib import Path

DATA_FILE = Path("ratings.csv")

if not DATA_FILE.exists():
    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["rating"])

st.write("Scan QR of open this link")
st.code(app_url)
st.image("qr.png", width=250)

# ❌ FIX 1: REMOVE this entire block (session_state not needed anymore)
# if "ratings" not in st.session_state:
#     st.session_state.ratings = []

with st.form("feedback_form"):
    name = st.text_input("Your name")

    Confidence = st.slider("confidence", 1, 5, 1)
    bodylanguage = st.slider("bodylanguage", 1, 5, 1)
    language = st.slider("language", 1, 5, 1)

    submit = st.form_submit_button("Submit")

if submit:
    avg = (Confidence + bodylanguage + language) / 3

    with open(DATA_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([avg])

    st.success("✅ Feedback Submitted!")

# ❌ FIX 2: DELETE this line (it breaks logic)
# if st.session_state.ratings:

# ✅ FIX 3: ratings list MUST be outside any if
ratings = []

with open(DATA_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ratings.append(float(row["rating"]))

if ratings:
    st.subheader("📊 Overall Average Rating")
    st.write(f"{sum(ratings)/len(ratings):.2f} / 5")
