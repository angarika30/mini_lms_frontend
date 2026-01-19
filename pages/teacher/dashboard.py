import streamlit as st
from components.progress import progress_card

st.set_page_config(page_title="Teacher Dashboard", layout="wide")

with open("styles/theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## 👩‍🏫 Teacher Dashboard")
st.caption("Teaching overview & analytics")

col1, col2, col3 = st.columns(3)
with col1:
    progress_card("Courses Created", 4)
with col2:
    progress_card("Active Students", 120)
with col3:
    progress_card("Quizzes Published", 8)

st.markdown("### 📊 Performance Overview")
st.markdown(
    """
    <div class="glass-card">
        <p>📈 Average Course Completion: 74%</p>
        <p>📊 Quiz Pass Rate: 82%</p>
        <p>🧠 Engagement Score: High</p>
    </div>
    """,
    unsafe_allow_html=True
)
