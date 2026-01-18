import streamlit as st

st.set_page_config(page_title="My Learning", layout="wide")

st.markdown("## 📈 My Learning Progress")
st.caption("Track your course completion")

progress_data = {
    "Python Fundamentals": 80,
    "Data Structures": 60,
    "Web Development": 40,
    "Cloud Computing": 20
}

for course, value in progress_data.items():
    st.markdown(f"**{course}**")
    st.progress(value)
