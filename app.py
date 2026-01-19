import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
from components.course_card import course_card
from components.progress import progress_card

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Mini LMS",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ LOAD THEME ------------------
with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown(
    """
    <h1>🚀 Mini Learning Management System</h1>
    <p style="color:#94a3b8;">Frontend Demo Mode (Authentication Disabled)</p>
    """,
    unsafe_allow_html=True
)

st.write("This is a **frontend-only prototype** of a Learning Management System.")
st.write("Use the role selector below to preview different dashboards.")

# ------------------ ROLE SELECTOR ------------------
role = st.selectbox("🎭 Select Role", ["student", "teacher", "admin"])

st.divider()

# ==================================================
# STUDENT DASHBOARD
# ==================================================
if role == "student":
    st.subheader("🎓 Student Dashboard")

    col1, col2, col3 = st.columns(3)
    with col1:
        progress_card("Courses Enrolled", 5)
    with col2:
        progress_card("Completed", 2)
    with col3:
        progress_card("Pending", 3)

    st.markdown("### 📘 My Courses")
    course_card("Python Basics", "Learn Python from scratch", 60)
    course_card("Web Development", "HTML, CSS, JavaScript fundamentals", 35)
    course_card("Data Science", "Intro to ML & Data Analysis", 20)

    st.markdown("### 🧠 Quizzes")
    course_card("Python Quiz 1", "Variables, Loops & Functions", 80)
    course_card("Web Dev Quiz", "HTML & CSS Basics", 50)

    st.markdown("### 💬 Forum Activity")
    st.markdown(
        """
        <div class="glass-card">
            <p>🗨 <b>New Discussion:</b> "Best Python IDE?"</p>
            <p>🗨 <b>Reply:</b> "Use VS Code with extensions"</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==================================================
# TEACHER DASHBOARD
# ==================================================
elif role == "teacher":
    st.subheader("👩‍🏫 Teacher Dashboard")

    col1, col2, col3 = st.columns(3)
    with col1:
        progress_card("Courses Created", 4)
    with col2:
        progress_card("Active Students", 120)
    with col3:
        progress_card("Quizzes Published", 8)

    st.markdown("### 📚 Manage Courses")
    course_card("Advanced Python", "OOP, Decorators, Async", 90)
    course_card("React JS", "Frontend Framework", 70)

    st.markdown("### 📝 Create Lesson")
    st.markdown(
        """
        <div class="glass-card">
            <p>📌 <b>Lesson Title:</b> Python Functions</p>
            <p>📌 <b>Status:</b> Draft</p>
            <button>Create Lesson</button>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 👨‍🎓 Students")
    st.markdown(
        """
        <div class="glass-card">
            <p>👤 John Doe — 78%</p>
            <p>👤 Jane Smith — 92%</p>
            <p>👤 Alex Johnson — 64%</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==================================================
# ADMIN DASHBOARD
# ==================================================
elif role == "admin":
    st.subheader("🛠 Admin Dashboard")

    col1, col2, col3 = st.columns(3)
    with col1:
        progress_card("Total Users", 240)
    with col2:
        progress_card("Total Courses", 18)
    with col3:
        progress_card("Reports", 6)

    st.markdown("### 👥 User Management")
    st.markdown(
        """
        <div class="glass-card">
            <p>👤 John Doe — Student</p>
            <p>👤 Jane Smith — Teacher</p>
            <p>👤 Admin User — Admin</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 📊 System Analytics")
    st.markdown(
        """
        <div class="glass-card">
            <p>📈 Daily Active Users: 58</p>
            <p>📉 Bounce Rate: 22%</p>
            <p>📊 Completion Rate: 74%</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------ FOOTER ------------------
st.divider()
st.caption("✨ Mini LMS — Frontend Demo for Academic Project")
