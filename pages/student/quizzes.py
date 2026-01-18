import streamlit as st

st.set_page_config(page_title="Quizzes", layout="wide")

st.markdown("## 📝 Quick Quiz")
st.caption("Frontend demo quiz")

question = "What is Streamlit mainly used for?"

answer = st.radio(
    question,
    [
        "Mobile App Development",
        "Data Visualization & Web Apps",
        "Game Development",
        "Operating Systems"
    ]
)

if st.button("Submit Answer"):
    if answer == "Data Visualization & Web Apps":
        st.success("✅ Correct! Well done 🎉")
    else:
        st.error("❌ Incorrect. Try again!")
