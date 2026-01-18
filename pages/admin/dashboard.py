import streamlit as st

st.set_page_config(page_title="Admin Dashboard", layout="wide")

st.markdown("## 🛠 Admin Dashboard")
st.caption("System overview & platform control (Demo Mode)")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👤 Total Users", "320")

with col2:
    st.metric("🎓 Students", "240")

with col3:
    st.metric("👩‍🏫 Teachers", "68")

with col4:
    st.metric("📚 Courses", "32")

st.markdown("---")

st.subheader("📊 Platform Health")

st.progress(0.85)
st.success("System running smoothly with 99.9% uptime")

st.markdown("---")

st.info(
    "🔐 Admin has full control over users, courses, and platform configuration."
)
