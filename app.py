import streamlit as st
import random
from collections import Counter

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="Clarity Deck — Sovereign",
    page_icon="♜",
    layout="centered"
)

# =============================
# CUSTOM STYLE
# =============================
st.markdown("""
<style>
html, body, [class*="css"]  {
    background-color: #0e1117;
    color: #e6e6e6;
    font-family: 'Inter', sans-serif;
}
h1 {
    font-weight: 700;
    letter-spacing: 1px;
}
.stButton>button {
    border-radius: 12px;
    padding: 0.6em 1.4em;
    font-weight: 600;
    background-color: #1f2937;
    color: white;
    border: 1px solid #333;
}
.stButton>button:hover {
    background-color: #111827;
}
.card-box {
    padding: 1.2em;
    border-radius: 14px;
    border: 1px solid #2a2a2a;
    background-color: #111827;
    margin-bottom: 1em;
}
.history-box {
    font-size: 0.85em;
    opacity: 0.7;
}
</style>
""", unsafe_allow_html=True)

# =============================
# DECK STRUCTURE
# =============================
deck = [
    {"name": "FLOW", "type": "Movement", "meaning": "Momentum is building. Continue forward."},
    {"name": "ECHO", "type": "Reflection", "meaning": "Past actions are resurfacing."},
    {"name": "FRACTURE", "type": "Tension", "meaning": "There is structural instability."},
    {"name": "GRAVITY", "type": "Reality", "meaning": "Face what is heavy and unavoidable."},
    {"name": "INFINITY", "type": "Expansion", "meaning": "This is bigger than you think."},
    {"name": "PIVOT", "type": "Movement", "meaning": "Change direction intentionally."},
    {"name": "MASK", "type": "Reflection", "meaning": "Something hidden is influencing outcomes."},
    {"name": "ANCHOR", "type": "Reality", "meaning": "Stability must be reclaimed."},
]

# =============================
# SESSION MEMORY
# =============================
if "history" not in st.session_state:
    st.session_state.history = []

# =============================
# TITLE
# =============================
st.title("CLARITY DECK — SOVEREIGN")
st.caption("Structure > Story | Clarity > Comfort")

mode = st.radio("Draw Mode", ["1 Card", "3 Cards", "5 Cards"])

# =============================
# DRAW FUNCTION
# =============================
def draw_cards(n):
    return random.sample(deck, n)

# =============================
# STRUCTURAL INTELLIGENCE
# =============================
def analyze_structure(cards):
    types = [c["type"] for c in cards]
    count = Counter(types)

    dominant = count.most_common(1)[0][0]

    if dominant == "Movement":
        insight = "Momentum dominates. This is an active phase."
    elif dominant == "Reflection":
        insight = "Reflection dominates. Patterns are repeating."
    elif dominant == "Reality":
        insight = "Reality dominates. Hard truths require attention."
    elif dominant == "Tension":
        insight = "Tension dominates. Internal conflict is present."
    else:
        insight = "Expansion theme. Boundaries are dissolving."

    return insight

# =============================
# REVEAL
# =============================
if st.button("Reveal"):

    if mode == "1 Card":
        num = 1
    elif mode == "3 Cards":
        num = 3
    else:
        num = 5

    cards = draw_cards(num)

    for card in cards:
        st.session_state.history.append(card["name"])
        st.markdown(f"""
        <div class="card-box">
            <h3>{card['name']}</h3>
            <p><b>Type:</b> {card['type']}</p>
            <p>{card['meaning']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Structural Insight")
    st.write(analyze_structure(cards))

# =============================
# HISTORY PANEL
# =============================
if st.session_state.history:
    st.markdown("---")
    st.markdown("### Session History")
    st.markdown(
        f"<div class='history-box'>{' → '.join(st.session_state.history)}</div>",
        unsafe_allow_html=True
    )
