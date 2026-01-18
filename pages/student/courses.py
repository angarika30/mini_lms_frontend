import streamlit as st

st.set_page_config(page_title="My Courses", layout="wide")

st.markdown("## 📘 My Courses")
st.caption("Browse your enrolled courses")

courses = [
    {"title": "Python Fundamentals", "level": "Beginner"},
    {"title": "Data Structures", "level": "Intermediate"},
    {"title": "Web Development", "level": "Intermediate"},
    {"title": "Cloud Computing", "level": "Beginner"},
]

for course in courses:
    with st.container():
        st.markdown(
            f"""
            <div style="
                padding:20px;
                margin-bottom:15px;
                border-radius:14px;
                background:linear-gradient(135deg,#1f2937,#020617);
                box-shadow:0 0 18px rgba(99,102,241,0.15);
            ">
                <h4>{course['title']}</h4>
                <p>Level: {course['level']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
