import streamlit as st

st.set_page_config(page_title="Lessons", layout="wide")

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## 📖 Lessons")
st.caption("Manage lessons inside a course")

lesson_title = st.text_input("Lesson Title")
lesson_content = st.text_area("Lesson Content")

if st.button("Add Lesson"):
    if lesson_title:
        st.success("✅ Lesson added (demo)")
    else:
        st.warning("Please enter lesson title")

st.markdown("---")

st.markdown("### Existing Lessons")
st.markdown(
    """
    <div class="glass-card">
        <p>📌 Introduction</p>
        <p>📌 Basics</p>
        <p>📌 Advanced Topics</p>
    </div>
    """,
    unsafe_allow_html=True
)
