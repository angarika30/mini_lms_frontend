import streamlit as st

st.set_page_config(page_title="Course Editor", layout="wide")

st.markdown("## ✏ Course Editor")
st.caption("Edit course content (demo)")

title = st.text_input("Course Title")
description = st.text_area("Course Description")
duration = st.number_input("Duration (hours)", min_value=1, max_value=100)

if st.button("Save Changes"):
    st.success("✅ Course updated successfully (demo)")
