"""
views/quiz.py
Quiz tab — 5 random questions from a bank of 50.
"""

import random
import streamlit as st
from data.quiz_data import QUIZ_QUESTIONS


def _init_session():
    defaults = {
        "quiz_questions": [],
        "quiz_index":     0,
        "quiz_answered":  False,
        "quiz_score":     0,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def _start_quiz():
    st.session_state.quiz_questions = random.sample(QUIZ_QUESTIONS, min(5, len(QUIZ_QUESTIONS)))
    st.session_state.quiz_index    = 0
    st.session_state.quiz_answered = False
    st.session_state.quiz_score    = 0
    # Clear previous answer states
    for key in list(st.session_state.keys()):
        if key.startswith("options_") or key.startswith("result_"):
            del st.session_state[key]


def _show_start_screen():
    st.markdown("""
    <div style="text-align:center;padding:48px 20px">
        <div style="font-size:3rem;margin-bottom:16px">🧠</div>
        <div style="font-family:serif;font-size:2rem;color:#c9a84c;margin-bottom:8px">Test your knowledge</div>
        <div style="color:#8a7f6e;font-size:0.95rem;margin-bottom:32px">5 random questions about cocktail theory and technique</div>
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("Start quiz →", type="primary", use_container_width=True):
            _start_quiz()
            st.rerun()


def _show_result():
    score = st.session_state.quiz_score
    total = len(st.session_state.quiz_questions)
    pct   = round(score / total * 100)

    st.session_state.quiz_correct += score
    st.session_state.quiz_total   += total

    if pct >= 80:
        icon, title, msg = "🏆", "Excellent!", "You think like a bartender."
    elif pct >= 60:
        icon, title, msg = "🍸", "Well done!", "You're learning fast."
    else:
        icon, title, msg = "🌱", "Keep going!", "Every expert was once a beginner."

    st.markdown(f"""
    <div style="text-align:center;padding:48px 20px">
        <div style="font-size:3.5rem;margin-bottom:16px">{icon}</div>
        <div style="font-family:serif;font-size:2rem;color:#c9a84c;margin-bottom:8px">{title}</div>
        <div style="font-size:3rem;font-family:serif;color:#e8dcc8;margin-bottom:4px">{score}/{total}</div>
        <div style="font-size:1.1rem;color:#8a7f6e;margin-bottom:24px">{msg}</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("Play again →", type="primary", use_container_width=True):
            _start_quiz()
            st.rerun()


def _show_question():
    idx   = st.session_state.quiz_index
    total = len(st.session_state.quiz_questions)
    q     = st.session_state.quiz_questions[idx]

    # Progress
    st.markdown(
        f"<div style='font-size:0.65rem;letter-spacing:3px;text-transform:uppercase;"
        f"color:#8a7f6e;margin-bottom:12px'>Question {idx+1} of {total}</div>",
        unsafe_allow_html=True)

    # Progress bar
    progress_pct = idx / total * 100
    st.markdown(
        f"<div style='background:#1e2636;border-radius:100px;height:4px;margin-bottom:28px;overflow:hidden'>"
        f"<div style='width:{progress_pct}%;height:100%;background:linear-gradient(90deg,#7a6230,#c9a84c);border-radius:100px'></div>"
        f"</div>",
        unsafe_allow_html=True)

    # Question
    st.markdown(
        f"<div style='font-family:serif;font-size:1.5rem;color:#e8dcc8;margin-bottom:28px;line-height:1.4'>"
        f"{q['question']}</div>",
        unsafe_allow_html=True)

    options_key = f"options_{idx}"
    if options_key not in st.session_state:
        options = [q["answer"]] + q["wrong"]
        random.shuffle(options)
        st.session_state[options_key] = options
    options = st.session_state[options_key]

    result_key = f"result_{idx}"

    if not st.session_state.quiz_answered:
        for opt in options:
            if st.button(opt, key=f"opt_{idx}_{opt}", use_container_width=True):
                st.session_state.quiz_answered = True
                correct = opt == q["answer"]
                if correct:
                    st.session_state.quiz_score += 1
                st.session_state[result_key] = ("correct" if correct else "wrong", opt)
                st.rerun()
    else:
        result, chosen = st.session_state.get(result_key, ("", ""))
        for opt in options:
            if opt == q["answer"]:
                st.success(f"✅  {opt}")
            elif opt == chosen and result == "wrong":
                st.error(f"❌  {opt}")
            else:
                st.button(opt, disabled=True, use_container_width=True, key=f"dis_{idx}_{opt}")

        if result == "correct":
            st.markdown(
                f"<div style='background:#1a2a1e;border:1px solid #6abf8a33;border-radius:10px;"
                f"padding:16px 20px;margin-top:16px;color:#e8dcc8;font-size:0.9rem;line-height:1.6'>"
                f"✅ <b>Correct!</b> {q['fact']}</div>",
                unsafe_allow_html=True)
        else:
            st.markdown(
                f"<div style='background:#2a1a1a;border:1px solid #bf6a6a33;border-radius:10px;"
                f"padding:16px 20px;margin-top:16px;color:#e8dcc8;font-size:0.9rem;line-height:1.6'>"
                f"❌ <b>Not quite.</b> {q['fact']}</div>",
                unsafe_allow_html=True)

        st.markdown("<div style='margin-top:16px'></div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,1,1])
        with col2:
            label = "See results →" if idx + 1 >= total else "Next question →"
            if st.button(label, type="primary", use_container_width=True):
                st.session_state.quiz_index   += 1
                st.session_state.quiz_answered = False
                st.rerun()


def show():
    _init_session()

    # Quiz CSS
    st.markdown("""
    <style>
    /* Quiz answer buttons */
    div[data-testid="stButton"] button[kind="secondary"] {
        background: #161c26 !important;
        border: 1px solid #c9a84c22 !important;
        border-radius: 10px !important;
        color: #e8dcc8 !important;
        font-size: 0.9rem !important;
        padding: 12px 20px !important;
        height: auto !important;
        text-align: left !important;
        margin-bottom: 8px !important;
        transition: border-color 0.2s !important;
    }
    div[data-testid="stButton"] button[kind="secondary"]:hover {
        border-color: #c9a84c88 !important;
        background: #1e2636 !important;
    }
    div[data-testid="stButton"] button[kind="secondary"]:disabled {
        opacity: 0.35 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    if not st.session_state.quiz_questions:
        _show_start_screen()
    elif st.session_state.quiz_index >= len(st.session_state.quiz_questions):
        _show_result()
    else:
        _show_question()
