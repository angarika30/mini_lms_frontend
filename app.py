import streamlit as st
from components.sidebar import render_sidebar

# Page config
st.set_page_config(
    page_title="Mini LMS",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header
st.title("🚀 Mini Learning Management System")
st.caption("Frontend Demo Mode (Authentication Disabled)")

# Role selector
role = st.sidebar.selectbox(
    "Select Role",
    ["student", "teacher", "admin"]
)

st.session_state["role"] = role

# Render sidebar safely
render_sidebar(role)

# Landing content
st.markdown("""
### Welcome 👋

This is a **high-fidelity frontend prototype** of a Learning Management System.

✨ Features:
- Role-based dashboards  
- Animated UI  
- Modular architecture  
- Backend-ready  

⬅ Use the **sidebar** to navigate pages.
""")

st.success(f"Viewing as **{role.capitalize()}**")
