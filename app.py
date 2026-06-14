"""
app.py — Cocktail Academy
Entry point. Imports and renders the different views.

Run with: streamlit run app.py
"""

import streamlit as st
from data.cocktails_data import COCKTAILS
from views import explore, quiz

# Page config
st.set_page_config(
    page_title="Cocktail House",
    page_icon="🍸",
    layout="wide",
)

# Custom styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap');

    #MainMenu, footer, header { visibility: hidden; }

    .stApp {
        background: linear-gradient(135deg, #0d1117 0%, #0d1117 70%, #1a3a2e22 100%);
    }

    .block-container {
        padding-top: 2rem;
        max-width: 1200px;
    }

    /* All general text bright and readable */
    p, span, div, label, li {
        color: #e8dcc8 !important;
    }

    /* Expander cards */
    .stExpander {
        background: #161c26 !important;
        border: 1px solid #c9a84c44 !important;
        border-radius: 12px !important;
        margin-bottom: 8px;
    }
    .stExpander:hover {
        border-color: #c9a84caa !important;
    }

    /* Expander header text — cocktail name */
    .stExpander summary p {
        color: #e8dcc8 !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
    }

    /* Radio buttons label text */
    .stRadio label p {
        color: #e8dcc8 !important;
    }

    /* Section headings like "Choose spirit" */
    .stMarkdown p strong {
        color: #c9a84c !important;
        font-size: 0.75rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* Caption text (cocktail count) */
    .stCaptionContainer p {
        color: #8a7f6e !important;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background: #161c26;
        border: 1px solid #c9a84c33;
        border-radius: 12px;
        padding: 16px 20px;
    }
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        color: #c9a84c !important;
    }
    [data-testid="stMetricLabel"] {
        color: #8a7f6e !important;
        font-size: 0.75rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab"] {
        font-size: 0.9rem;
        letter-spacing: 1px;
        color: #8a7f6e !important;
        padding: 10px 24px;
    }
    .stTabs [aria-selected="true"] {
        color: #c9a84c !important;
        border-bottom-color: #c9a84c !important;
    }

    /* Search input */
    .stTextInput input {
        background: #161c26 !important;
        border: 1px solid #c9a84c44 !important;
        border-radius: 8px !important;
        color: #e8dcc8 !important;
        padding: 12px 16px;
    }
    .stTextInput input::placeholder { color: #4a4540 !important; }
    .stTextInput input:focus {
        border-color: #c9a84c !important;
        box-shadow: 0 0 0 1px #c9a84c44 !important;
    }

    /* Multiselect — make it match the dark theme */
    .stMultiSelect [data-baseweb="select"] > div {
        background: #161c26 !important;
        border: 1px solid #c9a84c44 !important;
        border-radius: 8px !important;
    }
    .stMultiSelect [data-baseweb="select"] > div:focus-within {
        border-color: #c9a84c !important;
        box-shadow: 0 0 0 1px #c9a84c44 !important;
    }
    .stMultiSelect span { color: #e8dcc8 !important; }
    .stMultiSelect [data-baseweb="select"] input { color: #e8dcc8 !important; }
    /* Placeholder text in multiselect */
    .stMultiSelect [data-baseweb="select"] [data-testid="stMarkdownContainer"] p { color: #4a4540 !important; }
    div[data-baseweb="select"] > div { background-color: #161c26 !important; }
    /* Dropdown popup list */
    ul[data-baseweb="menu"] {
        background-color: #161c26 !important;
        border: 1px solid #c9a84c44 !important;
    }
    ul[data-baseweb="menu"] li {
        background-color: #161c26 !important;
        color: #e8dcc8 !important;
    }
    ul[data-baseweb="menu"] li:hover,
    ul[data-baseweb="menu"] li[aria-selected="true"] {
        background-color: #c9a84c22 !important;
        color: #c9a84c !important;
    }
    /* The popup container itself */
    [data-baseweb="popover"] > div,
    [data-baseweb="popover"] ul {
        background-color: #161c26 !important;
    }
    div[role="listbox"] {
        background-color: #161c26 !important;
    }
    div[role="option"] {
        background-color: #161c26 !important;
        color: #e8dcc8 !important;
    }
    div[role="option"]:hover {
        background-color: #c9a84c22 !important;
        color: #c9a84c !important;
    }
    /* Selected tags inside multiselect */
    [data-baseweb="tag"] {
        background: #c9a84c22 !important;
        border: 1px solid #c9a84c44 !important;
    }
    [data-baseweb="tag"] span { color: #c9a84c !important; }

    /* Progress bars */
    .stProgress > div > div {
        background: linear-gradient(90deg, #7a6230, #c9a84c) !important;
        border-radius: 100px;
    }
    /* Progress bar background track */
    .stProgress > div {
        background-color: #2a3040 !important;
        border-radius: 100px;
    }
    /* Progress bar text */
    .stProgress p { color: #e8dcc8 !important; font-size: 0.8rem !important; }

    /* Code blocks (ingredient amounts) */
    code {
        background: #c9a84c22 !important;
        color: #c9a84c !important;
        border: 1px solid #c9a84c33 !important;
        border-radius: 4px !important;
        padding: 1px 6px !important;
        font-size: 0.8rem !important;
    }

    /* Info box (did you know) */
    [data-testid="stNotification"] {
        background: #1a2a1e !important;
        border-left-color: #6abf8a !important;
    }
    [data-testid="stNotification"] p { color: #e8dcc8 !important; }

    /* Warning box (bartender tip) */
    div[data-baseweb="notification"] {
        background: #2a2010 !important;
    }

    /* Markdown inside expanders */
    .stExpander .stMarkdown p { color: #e8dcc8 !important; }
    .stExpander .stMarkdown li { color: #e8dcc8 !important; }
    .stExpander .stMarkdown strong { color: #c9a84c !important; }

    /* Divider */
    hr { border-color: #c9a84c22 !important; }

    /* Info / warning boxes */
    .stAlert { border-radius: 10px !important; }
    .stAlert p { color: #e8dcc8 !important; }

    /* Quiz buttons */
    .stButton > button {
        background: #161c26 !important;
        border: 1px solid #c9a84c44 !important;
        color: #e8dcc8 !important;
        border-radius: 8px !important;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        border-color: #c9a84c !important;
        color: #c9a84c !important;
    }
    .stButton > button[kind="primary"] {
        background: #c9a84c !important;
        color: #0d1117 !important;
        border: none !important;
        border-radius: 100px !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# Global session state
if "viewed" not in st.session_state:
    st.session_state.viewed = set()
if "quiz_correct" not in st.session_state:
    st.session_state.quiz_correct = 0
if "quiz_total" not in st.session_state:
    st.session_state.quiz_total = 0

# Header
st.markdown(
    "<h1 style='text-align:center; font-family:\"Playfair Display\",serif; color:#c9a84c; font-size:3rem'>🍸 Cocktail House</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align:center; color:#8a7f6e; letter-spacing:3px; text-transform:uppercase; font-size:0.8rem'>Find your next drink</p>",
    unsafe_allow_html=True,
)
st.markdown("<br>", unsafe_allow_html=True)

# Bartender Pick — random on each page load
import random
if "bartenders_pick" not in st.session_state:
    st.session_state.bartenders_pick = random.choice(COCKTAILS)
featured = st.session_state.bartenders_pick

from utils.glass_icons import get_glass_svg
glass_svg = get_glass_svg(featured["glass"])

html = (
    '<div style="' +
    'background:linear-gradient(135deg,#161c26 0%,#1a2a1e 100%);' +
    'border:1px solid #c9a84c33;border-radius:16px;padding:24px;">' +
    '<div style="font-size:0.65rem;letter-spacing:3px;text-transform:uppercase;color:#8a7f6e;margin-bottom:12px">🍸 Bartender Pick</div>' +
    '<div style="display:flex;align-items:center;gap:16px;margin-bottom:12px">' +
    f'<div style="flex-shrink:0">{glass_svg}</div>' +
    f'<div style="font-family:serif;font-size:clamp(1.2rem,5vw,2rem);color:#c9a84c;font-weight:700;line-height:1.1">{featured["name"]}</div>' +
    '</div>' +
    f'<div style="color:#8a7f6e;font-size:0.82rem;margin-bottom:10px">{featured["spirit_label"]}  ·  {featured["glass"]}</div>' +
    f'<div style="color:#e8dcc8;font-size:0.88rem;line-height:1.65">{featured["fun_fact"]}</div>' +
    '</div>'
)
st.markdown(html, unsafe_allow_html=True)
st.divider()

# Tabs
tab_explore, tab_find, tab_quiz = st.tabs(["🍸 All", "🔍 Find", "🧠 Quiz"])

with tab_explore:
    explore.show()

with tab_find:
    explore.show_find()

with tab_quiz:
    quiz.show()
