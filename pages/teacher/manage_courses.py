import streamlit as st

st.set_page_config(page_title="Manage Courses", layout="wide")

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## 📚 Manage Courses")
st.caption("Create, edit, or archive courses")

course_name = st.text_input("Course Name")
difficulty = st.selectbox("Difficulty Level", ["Beginner", "Intermediate", "Advanced"])
description = st.text_area("Course Description")

if st.button("Add Course"):
    if course_name:
        st.success(f"✅ Course '{course_name}' added (demo)")
    else:
        st.warning("Please enter course name")

st.markdown("---")

st.markdown("### Existing Courses")
st.markdown(
    """
    <div class="glass-card">
        <p>📘 Python Fundamentals</p>
        <p>📘 Web Development</p>
        <p>📘 Data Science</p>
    </div>
    """,
    unsafe_allow_html=True
)
