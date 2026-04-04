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

# Hide ALL Streamlit chrome — only the portfolio should be visible
st.markdown("""
<style>
  #MainMenu, header, footer,
  [data-testid="stToolbar"],
  [data-testid="stDecoration"],
  [data-testid="stStatusWidget"],
  .viewerBadge_container__1QSob,
  .stDeployButton { display: none !important; }

  /* Remove all padding from Streamlit wrapper */
  .block-container {
    padding: 0 !important;
    max-width: 100% !important;
    margin: 0 !important;
  }
  .stApp { background: #FAF8F4; }
  section.main > div { padding: 0 !important; }

  /* Remove iframe border/shadow */
  iframe { border: none !important; display: block !important; }
</style>
""", unsafe_allow_html=True)

# Load portfolio HTML from same directory
html_path = os.path.join(os.path.dirname(__file__), "portfolio.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Height covers all sections without blank space
# Hero + Marquee + About + Projects + Skills + Education + Contact + Footer
components.html(html_content, height=5200, scrolling=True)
