import streamlit as st

st.set_page_config(page_title="Manage Courses", layout="wide")

st.markdown("## 📚 Manage Courses")
st.caption("Create, edit, or archive courses")

course_name = st.text_input("Course Name")
course_level = st.selectbox("Difficulty Level", ["Beginner", "Intermediate", "Advanced"])

if st.button("Add Course"):
    if course_name:
        st.success(f"✅ Course '{course_name}' added (demo)")
    else:
        st.warning("Please enter course name")

st.markdown("---")

st.markdown("### Existing Courses")
st.info("📘 Python Fundamentals")
st.info("📘 Data Structures")
st.info("📘 Web Development")
