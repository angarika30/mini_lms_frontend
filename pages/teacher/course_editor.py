import streamlit as st

st.set_page_config(page_title="Course Editor", layout="wide")

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## ✏ Course Editor")
st.caption("Edit course content")

title = st.text_input("Course Title")
overview = st.text_area("Course Overview")
duration = st.number_input("Duration (hours)", min_value=1, max_value=200)

if st.button("Save Changes"):
    if title:
        st.success("✅ Course updated successfully (demo)")
    else:
        st.warning("Please enter course title")
