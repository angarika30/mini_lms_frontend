import streamlit as st

st.set_page_config(page_title="Forum Moderation", layout="wide")

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## 🛡 Forum Moderation")
st.caption("Monitor and moderate discussions")

st.warning("🚨 Inappropriate content flagged")
st.info("💬 Question about exam pattern")
st.info("💬 Request for extra materials")

if st.button("Resolve Issues"):
    st.success("✅ Issues resolved (demo)")
