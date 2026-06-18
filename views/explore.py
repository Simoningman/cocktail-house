"""
views/explore.py
Mobile-friendly — uses st.pills for letter navigation.
"""

import streamlit as st
from data.cocktails_data import COCKTAILS, SPIRITS, FLAVORS
from utils.filters import filter_cocktails
from utils.glass_icons import get_glass_svg

PER_PAGE = 5

CARD_STYLE = """
<style>
div[data-testid="stButton"] button[kind="secondary"] {
    background: #161c26 !important;
    border: 1px solid #c9a84c22 !important;
    border-radius: 10px !important;
    color: #e8dcc8 !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    text-align: left !important;
    padding: 14px 16px !important;
    height: auto !important;
    width: 100% !important;
    margin-bottom: 4px !important;
}
div[data-testid="stButton"] button[kind="secondary"]:hover {
    border-color: #c9a84c88 !important;
    background: #1e2636 !important;
}
/* Pills styling */
div[data-testid="stPills"] {
    gap: 6px !important;
}
div[data-testid="stPills"] button {
    border-radius: 8px !important;
    font-size: 0.8rem !important;
    padding: 4px 10px !important;
    height: 30px !important;
    min-width: 32px !important;
}
</style>
"""


def _ingredients_preview(c):
    """Return all ingredient names as a comma-separated string."""
    return " · ".join(ing[1] for ing in c["ingredients"])


def _render_card(c, prefix, state_key, selected_id):
    """Render a single cocktail card with toggle behaviour."""
    selected = selected_id == c["id"]
    border   = "#c9a84c" if selected else "#c9a84c22"
    bg       = "#1e2636" if selected else "#161c26"
    glass_svg = get_glass_svg(c["glass"])
    ingredients_preview = _ingredients_preview(c)

    st.markdown(
        f'<div style="background:{bg};border:1px solid {border};border-radius:10px 10px 0 0;'
        f'padding:12px 16px 8px;display:flex;align-items:center;gap:14px;margin-bottom:0">'
        f'<div style="flex-shrink:0">{glass_svg}</div>'
        f'<div style="min-width:0">'
        f'<div style="color:#e8dcc8;font-weight:500;font-size:0.95rem">{c["name"]}</div>'
        f'<div style="color:#8a7f6e;font-size:0.75rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{ingredients_preview}</div>'
        f'</div></div>'
        f'<div style="background:{bg};border:1px solid {border};border-top:none;'
        f'border-radius:0 0 10px 10px;margin-bottom:8px">',
        unsafe_allow_html=True,
    )

    btn_label = "▾  Close recipe" if selected else "▸  View recipe"
    if st.button(btn_label, key=f"btn_{prefix}_{c['id']}", use_container_width=True):
        if selected:
            st.session_state[state_key] = None  # toggle off
        else:
            st.session_state[state_key] = c["id"]
            if hasattr(st.session_state, 'viewed'):
                st.session_state.viewed.add(c["id"])
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    if selected:
        _render_detail(state_key)
        st.divider()
        st.markdown("<div style='margin-bottom:48px'></div>", unsafe_allow_html=True)


def show():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)
    _render_az_list(COCKTAILS, prefix="all", state_key="selected_id_all")


def show_find():
    st.markdown(CARD_STYLE, unsafe_allow_html=True)

    search = st.text_input("Search", placeholder="cocktail, flavor, spirit...",
                           label_visibility="collapsed", autocomplete="off")

    # Spirit pills
    st.markdown("<div style='font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;color:#8a7f6e;margin:12px 0 6px'>SPIRIT</div>", unsafe_allow_html=True)
    spirit_options = list(SPIRITS.values())
    if "selected_spirit" not in st.session_state:
        st.session_state["selected_spirit"] = None

    chosen_spirit_pill = st.pills(
        "Spirit", spirit_options, selection_mode="single",
        label_visibility="collapsed", key="spirit_pills"
    )
    if chosen_spirit_pill != st.session_state["selected_spirit"]:
        st.session_state["selected_spirit"] = chosen_spirit_pill
        st.rerun()
    chosen_spirit = chosen_spirit_pill or "All"

    # Flavor pills
    st.markdown("<div style='font-size:0.7rem;letter-spacing:2px;text-transform:uppercase;color:#8a7f6e;margin:12px 0 6px'>FLAVOR</div>", unsafe_allow_html=True)
    if "selected_flavors" not in st.session_state:
        st.session_state["selected_flavors"] = []

    chosen_flavors = st.pills(
        "Flavor", FLAVORS, selection_mode="multi",
        label_visibility="collapsed", key="flavor_pills"
    )
    if chosen_flavors != st.session_state["selected_flavors"]:
        st.session_state["selected_flavors"] = chosen_flavors
        st.rerun()

    st.divider()

    filtered = filter_cocktails(chosen_spirit, chosen_flavors, search)

    if chosen_spirit == "All" and not chosen_flavors and not search:
        st.markdown(
            f"<div style='color:#4a4540;font-size:0.85rem;padding:16px 0;text-align:center'>"
            f"Select a spirit or flavor  ·  <span style='font-size:0.7rem'>{len(COCKTAILS)} cocktails</span></div>",
            unsafe_allow_html=True)
        return

    if not filtered:
        st.markdown("<div style='color:#4a4540;padding:24px 0'>No cocktails matched.</div>", unsafe_allow_html=True)
        return

    state_key  = "selected_id_find"
    page_key   = "page_find"
    if page_key not in st.session_state:
        st.session_state[page_key] = 0

    sorted_filtered = sorted(filtered, key=lambda c: c["name"].upper())
    total       = len(sorted_filtered)
    total_pages = (total - 1) // PER_PAGE + 1
    page        = max(0, min(st.session_state[page_key], total_pages - 1))
    start       = page * PER_PAGE
    page_items  = sorted_filtered[start:start + PER_PAGE]

    st.markdown(
        f"<div style='color:#8a7f6e;font-size:0.7rem;margin:8px 0 12px'>"
        f"<span style='color:#c9a84c'>{total}</span> cocktail{'s' if total > 1 else ''} matched  ·  "
        f"Page {page+1} of {total_pages}</div>",
        unsafe_allow_html=True)

    selected_id = st.session_state.get(state_key)
    for c in page_items:
        _render_card(c, "find", state_key, selected_id)

    if total_pages > 1:
        p1, p2, p3 = st.columns([1, 2, 1])
        with p1:
            if page > 0:
                if st.button("← Prev", key="prev_find", use_container_width=True):
                    st.session_state[page_key] = page - 1
                    st.rerun()
        with p2:
            st.markdown(
                f"<div style='text-align:center;color:#8a7f6e;font-size:0.75rem;padding-top:8px'>"
                f"{start+1}–{min(start+PER_PAGE,total)} of {total}</div>",
                unsafe_allow_html=True)
        with p3:
            if page < total_pages - 1:
                if st.button("Next →", key="next_find", use_container_width=True):
                    st.session_state[page_key] = page + 1
                    st.rerun()


def _render_az_list(cocktails, prefix, state_key=None):
    if state_key is None:
        state_key = f'selected_id_{prefix}'
    sorted_cocktails = sorted(cocktails, key=lambda c: c["name"].upper())
    groups = {}
    for c in sorted_cocktails:
        letter = c["name"][0].upper()
        groups.setdefault(letter, []).append(c)
    letters = sorted(groups.keys())
    if not letters:
        return

    active_key = f"active_letter_{prefix}"
    page_key   = f"page_{prefix}"
    if active_key not in st.session_state:
        st.session_state[active_key] = None
    if page_key not in st.session_state:
        st.session_state[page_key] = 0

    active = st.session_state[active_key]

    chosen_letter = st.pills(
        "Letter", letters, selection_mode="single",
        label_visibility="collapsed", key=f"letter_pills_{prefix}"
    )

    if chosen_letter != active:
        st.session_state[active_key] = chosen_letter
        st.session_state[page_key] = 0
        st.session_state[state_key] = None
        st.rerun()

    if not chosen_letter or chosen_letter not in groups:
        st.markdown(
            f"<div style='color:#4a4540;font-size:0.85rem;padding:16px 0;text-align:center'>"
            f"Select a letter  ·  <span style='font-size:0.7rem'>{len(cocktails)} cocktails</span></div>",
            unsafe_allow_html=True)
        return

    items       = groups[chosen_letter]
    total       = len(items)
    page        = max(0, min(st.session_state[page_key], (total - 1) // PER_PAGE))
    total_pages = (total - 1) // PER_PAGE + 1
    start       = page * PER_PAGE
    page_items  = items[start:start + PER_PAGE]

    st.markdown(
        f"<div style='color:#8a7f6e;font-size:0.7rem;margin:8px 0 12px'>"
        f"<b style='color:#c9a84c'>{chosen_letter}</b>  ·  {total} cocktail{'s' if total>1 else ''}  ·  "
        f"Page {page+1} of {total_pages}</div>", unsafe_allow_html=True)

    selected_id = st.session_state.get(state_key)

    for c in page_items:
        _render_card(c, prefix, state_key, selected_id)

    if total_pages > 1:
        p1, p2, p3 = st.columns([1, 2, 1])
        with p1:
            if page > 0:
                if st.button("← Prev", key=f"prev_{prefix}", use_container_width=True):
                    st.session_state[page_key] = page - 1
                    st.rerun()
        with p2:
            st.markdown(
                f"<div style='text-align:center;color:#8a7f6e;font-size:0.75rem;padding-top:8px'>"
                f"{start+1}–{min(start+PER_PAGE,total)} of {total}</div>",
                unsafe_allow_html=True)
        with p3:
            if page < total_pages - 1:
                if st.button("Next →", key=f"next_{prefix}", use_container_width=True):
                    st.session_state[page_key] = page + 1
                    st.rerun()


def _render_detail(state_key="selected_id_all"):
    selected_id = st.session_state.get(state_key)
    if not selected_id:
        return

    c = next((x for x in COCKTAILS if x["id"] == selected_id), None)
    if not c:
        return

    st.markdown("<div style='margin-top:8px'></div>", unsafe_allow_html=True)
    glass_svg = get_glass_svg(c["glass"])
    st.markdown(
        f"<div style='display:flex;align-items:center;gap:16px;margin:8px 0 4px'>"
        f"<div>{glass_svg}</div>"
        f"<h2 style='color:#c9a84c;font-family:serif;margin:0'>{c['name']}</h2></div>",
        unsafe_allow_html=True)
    st.markdown(f"<div style='color:#8a7f6e;font-size:0.85rem;margin-bottom:16px'>{c['glass']}</div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Recipe", "Steps", "Tips"])

    with tab1:
        for amount, item in c["ingredients"]:
            st.markdown(f"- `{amount}` {item}")

    with tab2:
        for j, step in enumerate(c["steps"], 1):
            st.markdown(f"**{j}.** {step}")

    with tab3:
        st.markdown("**📊 Flavor profile**")
        for label, value in c["flavor_profile"].items():
            st.markdown(
                f"<div style='margin-bottom:10px'>"
                f"<div style='font-size:0.78rem;color:#8a7f6e;margin-bottom:4px'>{label}</div>"
                f"<div style='background:#1e2636;border-radius:100px;height:8px;overflow:hidden'>"
                f"<div style='width:{value}%;height:100%;background:linear-gradient(90deg,#7a6230,#c9a84c);border-radius:100px'></div>"
                f"</div></div>", unsafe_allow_html=True)
        st.markdown("---")
        st.info(f"💡 **Did you know?** {c['fun_fact']}")
        st.warning(f"🥂 **Bartender tip:** {c['tip']}")
