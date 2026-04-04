# ============================================================
# app.py — Abbas Ali · AI Portfolio · Streamlit Entry Point
# ============================================================
import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Abbas Ali — AI Engineer",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide all default Streamlit chrome
st.markdown("""
<style>
  #MainMenu, header, footer, [data-testid="stToolbar"],
  [data-testid="stDecoration"], [data-testid="stStatusWidget"],
  .viewerBadge_container__1QSob, .stDeployButton { display:none !important; }
  .block-container { padding:0 !important; max-width:100% !important; }
  .stApp { background: #FAF8F4; }
  section.main > div { padding:0 !important; }
</style>
""", unsafe_allow_html=True)

# Load portfolio HTML
html_path = os.path.join(os.path.dirname(__file__), "portfolio.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Render full portfolio — tall enough for all sections to scroll
components.html(html_content, height=6800, scrolling=True)