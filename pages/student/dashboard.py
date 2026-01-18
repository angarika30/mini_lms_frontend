import streamlit as st

st.set_page_config(page_title="Student Dashboard", layout="wide")

st.markdown("## 🎓 Student Dashboard")
st.caption("Overview of your learning progress")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📘 Courses", "6")

with col2:
    st.metric("📖 Lessons Completed", "28")

with col3:
    st.metric("📝 Quizzes", "9")

with col4:
    st.metric("🏆 Progress", "68%")

st.markdown("---")

st.success("🚀 Keep going! You're doing great.")
