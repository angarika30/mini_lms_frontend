import streamlit as st

def render_sidebar():
    st.sidebar.markdown("## 📘 Mini LMS")
    st.sidebar.caption("Frontend Demo Mode")

    st.sidebar.markdown("---")

    role = st.sidebar.selectbox("🎭 Select Role", ["Student", "Teacher", "Admin"])

    if role == "Student":
        page = st.sidebar.radio(
            "📂 Student Menu",
            ["Dashboard", "Courses", "My Learning", "Quizzes", "Forum"]
        )
    elif role == "Teacher":
        page = st.sidebar.radio(
            "📂 Teacher Menu",
            ["Dashboard", "Manage Courses", "Course Editor", "Lessons", "Quizzes", "Students", "Forum Moderation"]
        )
    else:
        page = st.sidebar.radio(
            "📂 Admin Menu",
            ["Dashboard", "User Management"]
        )

    return role, page
