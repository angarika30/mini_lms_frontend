import streamlit as st

st.set_page_config(page_title="Teacher Quizzes", layout="wide")

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## 📝 Quiz Management")
st.caption("Create and manage quizzes")

question = st.text_input("Question")
option_a = st.text_input("Option A")
option_b = st.text_input("Option B")
correct = st.selectbox("Correct Answer", ["Option A", "Option B"])

if st.button("Add Quiz"):
    if question:
        st.success("✅ Quiz added (demo)")
    else:
        st.warning("Please enter a question")

st.markdown("---")

st.markdown("### Existing Quizzes")
st.markdown(
    """
    <div class="glass-card">
        <p>📝 Python Quiz 1</p>
        <p>📝 Web Dev Quiz</p>
    </div>
    """,
    unsafe_allow_html=True
)
