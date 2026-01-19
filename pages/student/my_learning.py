import streamlit as st

st.set_page_config(page_title="My Learning", layout="wide")

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## 📈 My Learning Progress")
st.caption("Track your course-wise progress")

courses = {
    "Python Basics": 60,
    "Web Development": 35,
    "Data Science": 20,
    "Cloud Computing": 10
}

for course, progress in courses.items():
    st.markdown(f"**{course}**")
    st.progress(progress)

st.markdown("### 🎯 Learning Goals")
st.markdown(
    """
    <div class="glass-card">
        <p>📌 Complete Python Basics</p>
        <p>📌 Attempt 3 Quizzes</p>
        <p>📌 Maintain Learning Streak</p>
    </div>
    """,
    unsafe_allow_html=True
)
