import streamlit as st

st.set_page_config(page_title="Lessons", layout="wide")

st.markdown("## 📖 Lessons")
st.caption("Manage lessons inside a course")

lesson_title = st.text_input("Lesson Title")
lesson_content = st.text_area("Lesson Content")

if st.button("Add Lesson"):
    if lesson_title:
        st.success("✅ Lesson added (demo)")
    else:
        st.warning("Enter lesson title")

st.markdown("---")
st.info("Lesson 1: Introduction")
st.info("Lesson 2: Basics")
