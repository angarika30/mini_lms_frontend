import streamlit as st

def progress_card(label, value):
    st.markdown(
        f"""
        <div class="metric-glass">
            <h2>{value}</h2>
            <p>{label}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
