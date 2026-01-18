import streamlit as st

st.set_page_config(page_title="Student Forum", layout="wide")

st.markdown("## 💬 Student Forum")
st.caption("Ask questions & discuss topics")

username = st.text_input("Your Name")
message = st.text_area("Your Message")

if st.button("Post"):
    if username and message:
        st.success("✅ Message posted (demo)")
    else:
        st.warning("Please enter name and message")

st.markdown("---")

st.markdown("### 🧵 Recent Discussions")
st.info("💡 How to prepare for quizzes?")
st.info("💡 Best resources for Python?")
