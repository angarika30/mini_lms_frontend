import streamlit as st

st.set_page_config(page_title="Student Quizzes", layout="wide")

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## 📝 Quizzes")
st.caption("Attempt quizzes and test your knowledge")

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
        st.success("✅ Correct! Great job 🎉")
    else:
        st.error("❌ Incorrect. Try again!")

st.markdown("### 📊 Quiz History")
st.markdown(
    """
    <div class="glass-card">
        <p>✔ Python Quiz 1 — Passed</p>
        <p>✔ Web Dev Quiz — Passed</p>
        <p>❌ Data Science Quiz — Failed</p>
    </div>
    """,
    unsafe_allow_html=True
)
