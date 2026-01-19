import streamlit as st

def course_card(title, description, progress=0):
    st.markdown(
        f"""
        <div class="glass-card">
            <h3>📘 {title}</h3>
            <p>{description}</p>
            <p><b>Progress:</b> {progress}%</p>
            <div style="height:8px;background:#1f2933;border-radius:6px;">
                <div style="
                    width:{progress}%;
                    height:8px;
                    background:linear-gradient(90deg,#38bdf8,#6366f1);
                    border-radius:6px;
                    transition:width 1s ease;
                "></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
