import streamlit as st
import random

st.set_page_config(page_title="Celestial Biscuit", page_icon="🌌", layout="centered")

hide_streamlit_style = """
    <style>
    /* Hide Streamlit's default header */
    header[data-testid="stHeader"] {
        background: none !important;
        height: 0px;
    }

    /* Hide the footer ("Made with Streamlit") */
    footer {visibility: hidden;}

    /* Optional: also hide the top hamburger menu */
    #MainMenu {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

CLUES = {
    "it": ["it - clue1", "it - clue2", "it - clue3"],
    "ece": ["ece - clue1", "ece - clue2", "ece - clue3"],
    "canteen": ["canteen - clue1", "canteen - clue2", "canteen - clue3"],
    "badminton": ["badminton - clue1", "badminton - clue2", "badminton - clue3"],
    "architecture": ["architecture - clue1", "architecture - clue2", "architecture - clue3"],
}

def pick_clues():
    chosen = [random.choice(v) for v in CLUES.values()]  
    random.shuffle(chosen)                             
    return chosen

if "clues" not in st.session_state:
    st.session_state.clues = pick_clues()

css = """
<style>
/* Try to override Streamlit default with !important */
html, body, .stApp {
  background: radial-gradient(circle at 10% 10%, #03041a 0%, #071633 25%, #0b2540 60%, #071225 100%) !important;
  color: #eaf2ff;
}

/* Inner card that contains the content */
.app-container {
  max-width: 920px;
  margin: 10px auto;
  padding: 32px;
  border-radius: 16px;
  background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
  border: 1px solid rgba(140,160,255,0.05);
  box-shadow: 0 12px 40px rgba(10,20,60,0.6), inset 0 1px 0 rgba(255,255,255,0.02);
}

/* Title */
.title {
  font-size: 44px;
  font-weight: 800;
  text-align: center;
  margin-bottom: 6px;
  color: #cfe3ff;
  text-shadow: 0 3px 22px rgba(120,70,255,0.25);
}

.midtitle {
  font-size: 28px;   /* between 44px title and 14px subtitle */
  font-weight: 600;
  text-align: center;
  margin-bottom: 12px;
  color: #d4e0ff;
  text-shadow: 0 2px 12px rgba(140,180,255,0.25);
}

/* Subtitle */
.subtitle {
  text-align:center;
  color: #b8d6ff;
  margin-bottom: 20px;
  font-size: 14px;
}

/* Clue cards */
.clue {
  background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
  border-radius: 12px;
  padding: 16px 22px;
  margin: 12px 0;
  font-size: 18px;
  text-align: center;
  color: #eaf3ff;
  border: 1px solid rgba(130,170,255,0.06);
  box-shadow: 0 10px 24px rgba(60,110,255,0.06), 0 0 36px rgba(80,130,255,0.03);
}

/* small responsive tweaks */
@media (max-width: 700px) {
  .title { font-size: 32px; }
  .clue { font-size: 16px; padding: 14px; }
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

html = '<div class="app-container">'
html += '<div class="title">🌠 Celestial Biscuit</div>'
html += '<div class="midtitle">Big Bang Hunt</div>'
html += '<div class="subtitle">Go to the locations given in these clues and look for planets 🌍</div>'

for c in st.session_state.clues:
    html += f'<div class="clue">{c}</div>'

html += '</div>'

st.markdown(html, unsafe_allow_html=True)
