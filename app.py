import streamlit as st
import random

st.set_page_config(
    page_title="CLARITY DECK — Sovereign",
    layout="centered"
)

# ---------------------
# CUSTOM CSS
# ---------------------
st.markdown("""
<style>
body {
    background-color: #0b0f1a;
}
.main {
    background: linear-gradient(180deg, #0b0f1a 0%, #111827 100%);
    color: #e5e7eb;
}
.card-box {
    padding: 20px;
    border-radius: 16px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.08);
}
.analysis-box {
    padding: 25px;
    border-radius: 20px;
    background: rgba(99,102,241,0.08);
    border: 1px solid rgba(99,102,241,0.3);
}
h1, h2, h3 {
    color: #f3f4f6;
}
</style>
""", unsafe_allow_html=True)

st.title("CLARITY DECK — SOVEREIGN")
st.caption("Structure > Story  |  Clarity > Comfort")

# ---------------------
# SESSION STATE
# ---------------------
if "draw_count" not in st.session_state:
    st.session_state.draw_count = {}

# ---------------------
# DECK STRUCTURE
# ---------------------
deck = {
    "LAW": ["GRAVITY", "ORDER", "CHAOS", "SYMMETRY"],
    "MOVEMENT": ["FLOW", "IMPACT", "RESONANCE"],
    "BOUNDARY": ["THRESHOLD", "HORIZON"],
    "SHADOW": ["SHADOW", "ECHO", "FRACTURE"],
    "META": ["THE VOID", "INFINITY"]
}

weights = {
    "LAW": 0.35,
    "MOVEMENT": 0.25,
    "BOUNDARY": 0.2,
    "SHADOW": 0.15,
    "META": 0.05
}

# ---------------------
# DRAW ENGINE
# ---------------------
def weighted_category():
    return random.choices(
        list(deck.keys()),
        weights=list(weights.values())
    )[0]

def draw_card():
    for _ in range(10):
        cat = weighted_category()
        card = random.choice(deck[cat])
        if st.session_state.draw_count.get(card, 0) < 2:
            st.session_state.draw_count[card] = \
                st.session_state.draw_count.get(card, 0) + 1
            return card, cat
    return None, None

# ---------------------
# ANALYZER
# ---------------------
def analyze(cards):
    categories = [c[1] for c in cards]
    dominant = max(set(categories), key=categories.count)

    if "BOUNDARY" in categories:
        pattern = "Transition Phase"
    elif categories.count("SHADOW") >= 2:
        pattern = "Reflection Loop"
    elif categories.count("LAW") >= 3:
        pattern = "Structural Pressure"
    else:
        pattern = "Mixed Signal"

    return dominant, pattern

# ---------------------
# UI CONTROLS
# ---------------------
mode = st.radio("Draw Mode", ["1 Card", "3 Cards", "5 Cards"])

if st.button("Reveal"):

    n = int(mode.split()[0])
    results = [draw_card() for _ in range(n)]

    st.divider()

    for card, cat in results:
        st.markdown(f"""
        <div class="card-box">
            <h3>{card}</h3>
            <small>Field: {cat}</small>
        </div>
        """, unsafe_allow_html=True)

    dominant, pattern = analyze(results)

    st.markdown(f"""
    <div class="analysis-box">
        <h2>Structural Analysis</h2>
        <p><strong>Dominant Field:</strong> {dominant}</p>
        <p><strong>Pattern:</strong> {pattern}</p>
        <p>Look at the structure, not the emotion.</p>
    </div>
    """, unsafe_allow_html=True)
