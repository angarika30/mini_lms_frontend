import streamlit as st
from components.progress import progress_card

st.set_page_config(page_title="Admin Dashboard", layout="wide")

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## 🛠 Admin Dashboard")
st.caption("Platform overview & system control")

col1, col2, col3, col4 = st.columns(4)
with col1:
    progress_card("Total Users", 320)
with col2:
    progress_card("Students", 240)
with col3:
    progress_card("Teachers", 68)
with col4:
    progress_card("Courses", 32)

st.markdown("---")

st.markdown("### 📊 Platform Analytics")
st.markdown(
    """
    <div class="glass-card">
        <p>📈 Daily Active Users: 58</p>
        <p>📉 Bounce Rate: 22%</p>
        <p>📊 Course Completion Rate: 74%</p>
        <p>⚡ System Uptime: 99.9%</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("### 🔔 System Alerts")
st.markdown(
    """
    <div class="glass-card">
        <p>🟢 All services running normally</p>
        <p>🟡 2 pending teacher approvals</p>
        <p>🔴 1 reported forum post</p>
    </div>
    """,
    unsafe_allow_html=True
)
