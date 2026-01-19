import streamlit as st

st.set_page_config(page_title="Student Forum", layout="wide")

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## 💬 Student Forum")
st.caption("Ask questions and discuss topics")

username = st.text_input("Your Name")
message = st.text_area("Your Message")

if st.button("Post Message"):
    if username and message:
        st.success("✅ Message posted (demo)")
    else:
        st.warning("Please enter your name and message")

st.markdown("---")

st.markdown("### 🧵 Recent Discussions")
st.markdown(
    """
    <div class="glass-card">
        <p>💡 Best resources for Python?</p>
        <p>💡 How to prepare for quizzes?</p>
        <p>💡 Tips for learning Cloud Computing</p>
    </div>
    """,
    unsafe_allow_html=True
)
