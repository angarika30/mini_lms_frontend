import streamlit as st

def render_sidebar(role: str):
    st.sidebar.markdown("## 📘 Mini LMS")
    st.sidebar.caption("Frontend Demo Mode")

    st.sidebar.markdown("---")

    if role == "student":
        st.sidebar.page_link("student/dashboard.py", label="🎓 Dashboard")
        st.sidebar.page_link("student/courses.py", label="📘 Courses")
        st.sidebar.page_link("student/my_learning.py", label="📈 My Learning")
        st.sidebar.page_link("student/quizzes.py", label="📝 Quizzes")
        st.sidebar.page_link("student/forum.py", label="💬 Forum")

    elif role == "teacher":
        st.sidebar.page_link("teacher/dashboard.py", label="👩‍🏫 Dashboard")
        st.sidebar.page_link("teacher/manage_courses.py", label="📚 Manage Courses")
        st.sidebar.page_link("teacher/course_editor.py", label="✏ Course Editor")
        st.sidebar.page_link("teacher/lessons.py", label="📖 Lessons")
        st.sidebar.page_link("teacher/quizzes.py", label="📝 Quizzes")
        st.sidebar.page_link("teacher/students.py", label="👥 Students")
        st.sidebar.page_link("teacher/forum_moderation.py", label="🛡 Forum Moderation")

    elif role == "admin":
        st.sidebar.page_link("admin/dashboard.py", label="🛠 Dashboard")
        st.sidebar.page_link("admin/user_management.py", label="👤 User Management")

    st.sidebar.markdown("---")
    st.sidebar.info("🚀 UI Demo Mode")
