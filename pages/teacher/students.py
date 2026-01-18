import streamlit as st

st.set_page_config(page_title="Students", layout="wide")

st.markdown("## 👥 Enrolled Students")
st.caption("View students enrolled in your courses")

students = [
    "Aarohi",
    "Rahul",
    "Sneha",
    "Karthik",
    "Meena"
]

for student in students:
    st.markdown(f"- 🎓 {student}")
