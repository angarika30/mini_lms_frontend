import streamlit as st

st.set_page_config(page_title="Mini LMS", layout="wide")

# --- THEME LOAD ---
with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🚀 Mini Learning Management System")
st.caption("Frontend Demo Mode (Authentication Disabled)")

role = st.selectbox("Select Role", ["Student", "Teacher", "Admin"])

st.markdown("---")

# =======================
# STUDENT UI
# =======================
if role == "Student":
    st.header("🎓 Student Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Courses Enrolled", "5")
    col2.metric("Lessons Completed", "28")
    col3.metric("Progress", "62%")

    st.subheader("📘 My Courses")
    st.info("Python Basics")
    st.info("Data Structures")
    st.info("Cloud Fundamentals")

    st.progress(0.62)

    st.subheader("📝 Quizzes")
    st.write("Upcoming quiz: Python Fundamentals")

    st.subheader("💬 Forum")
    st.write("Ask questions, discuss topics")

# =======================
# TEACHER UI
# =======================
elif role == "Teacher":
    st.header("👩‍🏫 Teacher Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Courses Created", "4")
    col2.metric("Students Enrolled", "128")
    col3.metric("Quizzes Created", "12")

    st.subheader("📚 Manage Courses")
    course_name = st.text_input("New Course Name")
    if st.button("Add Course"):
        st.success(f"Course '{course_name}' added (demo)")

    st.subheader("📖 Lessons")
    lesson = st.text_input("New Lesson Title")
    if st.button("Add Lesson"):
        st.success(f"Lesson '{lesson}' added (demo)")

    st.subheader("👥 Students")
    for s in ["Aarohi", "Rahul", "Sneha", "Meena"]:
        st.markdown(f"- {s}")

    st.subheader("🛡 Forum Moderation")
    st.warning("Flagged post: Inappropriate content")

# =======================
# ADMIN UI
# =======================
elif role == "Admin":
    st.header("🛠 Admin Dashboard")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Users", "320")
    col2.metric("Students", "240")
    col3.metric("Teachers", "68")
    col4.metric("Courses", "32")

    st.subheader("👥 User Management")
    username = st.text_input("Username")
    role_select = st.selectbox("Assign Role", ["Student", "Teacher", "Admin"])
    if st.button("Create User"):
        st.success(f"User '{username}' created as {role_select} (demo)")

    st.subheader("📊 Platform Health")
    st.progress(0.87)
    st.success("System operating normally")
