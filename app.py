import sys
import os
import streamlit as st

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from components.sidebar import render_sidebar
from components.course_card import course_card
from components.progress import progress_card

st.set_page_config(page_title="Mini LMS", layout="wide")

# Load Theme
with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar Navigation
role, page = render_sidebar()

# Header
st.markdown(
    "<h1>🚀 Mini Learning Management System</h1>"
    "<p style='color:#94a3b8;'>Frontend Demo Mode (Authentication Disabled)</p>",
    unsafe_allow_html=True
)

st.divider()

# ============================
# STUDENT NAVIGATION
# ============================
if role == "Student":

    if page == "Dashboard":
        st.subheader("🎓 Student Dashboard")

        col1, col2, col3 = st.columns(3)
        with col1:
            progress_card("Courses Enrolled", 5)
        with col2:
            progress_card("Lessons Completed", 28)
        with col3:
            progress_card("Overall Progress", "62%")

        course_card("Python Basics", "Learn Python from scratch", 60)
        course_card("Web Development", "HTML, CSS & JavaScript fundamentals", 35)
        course_card("Data Science", "Intro to ML & Data Analysis", 20)

    elif page == "Courses":
        st.subheader("📘 My Courses")
        course_card("Python Basics", "Core Python concepts", 60)
        course_card("Web Development", "Frontend fundamentals", 35)
        course_card("Data Science", "Intro to machine learning", 20)
        course_card("Cloud Computing", "AWS & Azure basics", 10)

    elif page == "My Learning":
        st.subheader("📈 My Learning Progress")

        courses = {
            "Python Basics": 60,
            "Web Development": 35,
            "Data Science": 20,
            "Cloud Computing": 10
        }

        for course, progress in courses.items():
            st.markdown(f"**{course}**")
            st.progress(progress)

    elif page == "Quizzes":
        st.subheader("📝 Quizzes")

        question = "What is Streamlit mainly used for?"

        answer = st.radio(
            question,
            [
                "Mobile App Development",
                "Data Visualization & Web Apps",
                "Game Development",
                "Operating Systems"
            ]
        )

        if st.button("Submit Answer"):
            if answer == "Data Visualization & Web Apps":
                st.success("✅ Correct! Great job 🎉")
            else:
                st.error("❌ Incorrect. Try again!")

    elif page == "Forum":
        st.subheader("💬 Student Forum")

        username = st.text_input("Your Name")
        message = st.text_area("Your Message")

        if st.button("Post Message"):
            if username and message:
                st.success("✅ Message posted (demo)")
            else:
                st.warning("Please enter your name and message")

# ============================
# TEACHER NAVIGATION
# ============================
elif role == "Teacher":

    if page == "Dashboard":
        st.subheader("👩‍🏫 Teacher Dashboard")

        col1, col2, col3 = st.columns(3)
        with col1:
            progress_card("Courses Created", 4)
        with col2:
            progress_card("Active Students", 120)
        with col3:
            progress_card("Quizzes Published", 8)

    elif page == "Manage Courses":
        st.subheader("📚 Manage Courses")

        course_name = st.text_input("Course Name")
        difficulty = st.selectbox("Difficulty Level", ["Beginner", "Intermediate", "Advanced"])

        if st.button("Add Course"):
            st.success(f"Course '{course_name}' added (demo)")

    elif page == "Course Editor":
        st.subheader("✏ Course Editor")

        title = st.text_input("Course Title")
        overview = st.text_area("Course Overview")

        if st.button("Save Changes"):
            st.success("Course updated (demo)")

    elif page == "Lessons":
        st.subheader("📖 Lessons")

        lesson_title = st.text_input("Lesson Title")
        lesson_content = st.text_area("Lesson Content")

        if st.button("Add Lesson"):
            st.success("Lesson added (demo)")

    elif page == "Quizzes":
        st.subheader("📝 Quiz Management")

        question = st.text_input("Question")

        if st.button("Add Quiz"):
            st.success("Quiz added (demo)")

    elif page == "Students":
        st.subheader("👥 Students")

        for s in ["Aarohi", "Rahul", "Sneha", "Karthik", "Meena"]:
            st.markdown(f"- {s}")

    elif page == "Forum Moderation":
        st.subheader("🛡 Forum Moderation")
        st.warning("🚨 Inappropriate content flagged")
        st.info("💬 Question about exam pattern")

# ============================
# ADMIN NAVIGATION
# ============================
elif role == "Admin":

    if page == "Dashboard":
        st.subheader("🛠 Admin Dashboard")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            progress_card("Total Users", 320)
        with col2:
            progress_card("Students", 240)
        with col3:
            progress_card("Teachers", 68)
        with col4:
            progress_card("Courses", 32)

    elif page == "User Management":
        st.subheader("👥 User Management")

        username = st.text_input("Username")
        role_select = st.selectbox("Assign Role", ["Student", "Teacher", "Admin"])

        if st.button("Create User"):
            st.success(f"User '{username}' created as {role_select} (demo)")

# Footer
st.divider()
st.caption("✨ Mini LMS — Frontend Demo")
