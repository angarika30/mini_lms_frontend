import streamlit as st

def render_sidebar(role: str):
    st.sidebar.markdown("## 📘 Mini LMS")
    st.sidebar.caption("Frontend Demo Mode")

    st.sidebar.markdown("---")

    if role == "student":
        st.sidebar.page_link("pages/student/dashboard.py", label="🎓 Dashboard")
        st.sidebar.page_link("pages/student/courses.py", label="📘 Courses")
        st.sidebar.page_link("pages/student/my_learning.py", label="📈 My Learning")
        st.sidebar.page_link("pages/student/quizzes.py", label="📝 Quizzes")
        st.sidebar.page_link("pages/student/forum.py", label="💬 Forum")

    elif role == "teacher":
        st.sidebar.page_link("pages/teacher/dashboard.py", label="👩‍🏫 Dashboard")
        st.sidebar.page_link("pages/teacher/manage_courses.py", label="📚 Manage Courses")
        st.sidebar.page_link("pages/teacher/course_editor.py", label="✏ Course Editor")
        st.sidebar.page_link("pages/teacher/lessons.py", label="📖 Lessons")
        st.sidebar.page_link("pages/teacher/quizzes.py", label="📝 Quizzes")
        st.sidebar.page_link("pages/teacher/students.py", label="👥 Students")
        st.sidebar.page_link("pages/teacher/forum_moderation.py", label="🛡 Forum Moderation")

    elif role == "admin":
        st.sidebar.page_link("pages/admin/dashboard.py", label="🛠 Dashboard")
        st.sidebar.page_link("pages/admin/user_management.py", label="👤 User Management")

    st.sidebar.markdown("---")
    st.sidebar.info("🚀 UI Demo Mode")
