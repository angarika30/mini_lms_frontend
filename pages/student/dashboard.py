import streamlit as st
from components.course_card import course_card
from components.progress import progress_card

st.set_page_config(page_title="Student Dashboard", layout="wide")

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## 🎓 Student Dashboard")
st.caption("Your learning overview")

col1, col2, col3 = st.columns(3)
with col1:
    progress_card("Courses Enrolled", 5)
with col2:
    progress_card("Lessons Completed", 28)
with col3:
    progress_card("Overall Progress", "62%")

st.markdown("### 📘 Active Courses")
course_card("Python Basics", "Learn Python from scratch", 60)
course_card("Web Development", "HTML, CSS & JavaScript fundamentals", 35)
course_card("Data Science", "Intro to ML & Data Analysis", 20)

st.markdown("### 🏆 Achievements")
st.markdown(
    """
    <div class="glass-card">
        <p>🥇 Completed 20+ Lessons</p>
        <p>🥈 5 Quizzes Passed</p>
        <p>🥉 7-Day Learning Streak</p>
    </div>
    """,
    unsafe_allow_html=True
)
