import streamlit as st

st.set_page_config(page_title="Forum Moderation", layout="wide")

st.markdown("## 🛡 Forum Moderation")
st.caption("Monitor and moderate discussions")

st.warning("🚨 Inappropriate content flagged")
st.info("💬 Question about exam pattern")
st.info("💬 Request for extra materials")

if st.button("Resolve Issues"):
    st.success("✅ Issues resolved (demo)")
