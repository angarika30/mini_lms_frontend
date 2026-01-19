import streamlit as st

st.set_page_config(page_title="Students", layout="wide")

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## 👥 Enrolled Students")
st.caption("View students enrolled in your courses")

students = [
    ("Aarohi", "78%"),
    ("Rahul", "92%"),
    ("Sneha", "64%"),
    ("Karthik", "85%"),
    ("Meena", "71%")
]

st.markdown("### Student List")

for name, progress in students:
    st.markdown(
        f"""
        <div class="glass-card">
            <p>👤 <b>{name}</b></p>
            <p>Progress: {progress}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
