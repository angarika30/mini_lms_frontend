import streamlit as st

st.set_page_config(page_title="User Management", layout="wide")

st.markdown("## 👥 User Management")
st.caption("Manage users and roles (Demo UI)")

st.markdown("### ➕ Add New User")

col1, col2 = st.columns(2)

with col1:
    username = st.text_input("Username")
    email = st.text_input("Email")

with col2:
    role = st.selectbox("Role", ["Student", "Teacher", "Admin"])

if st.button("Create User"):
    if username and email:
        st.success(f"✅ User **{username}** created as **{role}** (demo)")
    else:
        st.warning("Please fill all fields")

st.markdown("---")

st.markdown("### 📋 Existing Users")

users = [
    ("Aarohi", "Student"),
    ("Rahul", "Teacher"),
    ("Sneha", "Student"),
    ("Admin01", "Admin")
]

for name, role in users:
    st.markdown(f"- 👤 **{name}** — `{role}`")
