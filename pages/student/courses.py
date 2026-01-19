import streamlit as st
from components.course_card import course_card

st.set_page_config(page_title="My Courses", layout="wide")

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## 📘 My Courses")
st.caption("Browse all your enrolled courses")

course_card("Python Basics", "Core Python concepts", 60)
course_card("Web Development", "Frontend fundamentals", 35)
course_card("Data Science", "Intro to machine learning", 20)
course_card("Cloud Computing", "AWS & Azure basics", 10)
