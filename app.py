import streamlit as st
import qrcode
from PIL import Image

st.title("Feedback App")

st.write("Scan the QR code of submit feedback below")

app_url = "https://your-app.streamlit.app"
qr = qrcode.make(app_url)
qr.save("qr.png")

st.write("Scan QR of open this link")
st.code(app_url)
st.image("feedback_qr.png", width=250)
if "ratings" not in st.session_state:
    st.session_state.ratings = []


with st.form("feedback_form"):

    name = st.text_input("Your name")

    Confidence = st.slider("confidence",
                    min_value = 1,
                    max_value = 5,
                    step=1
                    )
    bodylanguage = st.slider("bodylanguage",
                    min_value = 1,
                    max_value = 5,
                    step=1
                    )
    language = st.slider("language",
                    min_value = 1,
                    max_value = 5,
                    step=1
                    )
    submit = st.form_submit_button("Submit")
if submit:
    avg = (Confidence + bodylanguage + language)/3
    st.session_state.ratings.append(avg)

    st.success("Feedback Submitted!")

    st.write("### Submitted Feedback")

if st.session_state.ratings:

    overall_avg = sum(st.session_state.ratings) / len(st.session_state.ratings)

    st.subheader("📊 Overall Average Rating")

    st.metric("Average Score", round(overall_avg, 2))

    st.write("Total responses:", len(st.session_state.ratings))