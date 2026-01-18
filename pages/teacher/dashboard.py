import streamlit as st

st.set_page_config(page_title="Teacher Dashboard", layout="wide")

st.markdown("## 👩‍🏫 Teacher Dashboard")
st.caption("Teaching overview & analytics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📚 Courses Created", "4")

with col2:
    st.metric("👥 Students Enrolled", "128")

with col3:
    st.metric("📝 Quizzes Created", "12")

st.markdown("---")
st.success("You are managing your courses effectively 🚀")
