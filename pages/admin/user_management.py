import streamlit as st

st.set_page_config(page_title="User Management", layout="wide")

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## 👥 User Management")
st.caption("Create, edit and manage platform users")

st.markdown("### ➕ Add New User")

col1, col2 = st.columns(2)

with col1:
    username = st.text_input("Username")
    email = st.text_input("Email")

with col2:
    role = st.selectbox("Assign Role", ["Student", "Teacher", "Admin"])

if st.button("Create User"):
    if username and email:
        st.success(f"✅ User '{username}' created as {role} (demo)")
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
    st.markdown(
        f"""
        <div class="glass-card">
            <p>👤 <b>{name}</b></p>
            <p>Role: {role}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
