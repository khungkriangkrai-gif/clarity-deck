import streamlit as st
import random
import uuid
import datetime
from collections import Counter

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Clarity Deck — Reflection Engine",
    page_icon="♜",
    layout="centered"
)

# =========================
# STYLE
# =========================
st.markdown("""
<style>
html, body, [class*="css"]  {
    background-color: #0e1117;
    color: #e6e6e6;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
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
    font-size: 0.9em;
    opacity: 0.8;
}
.footer {
    margin-top: 3em;
    font-size: 0.8em;
    opacity: 0.5;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION INIT
# =========================
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# DECK
# =========================
deck = [
    {"name": "FLOW", "type": "Movement", "meaning": "Momentum is building. Continue forward intentionally."},
    {"name": "ECHO", "type": "Reflection", "meaning": "Past patterns are resurfacing. Notice repetition."},
    {"name": "FRACTURE", "type": "Tension", "meaning": "There is instability. Something needs restructuring."},
    {"name": "GRAVITY", "type": "Reality", "meaning": "A hard truth requires your attention."},
    {"name": "INFINITY", "type": "Expansion", "meaning": "The situation is larger than your current frame."},
    {"name": "PIVOT", "type": "Movement", "meaning": "A directional shift may be necessary."},
    {"name": "MASK", "type": "Reflection", "meaning": "Something unseen is influencing outcomes."},
    {"name": "ANCHOR", "type": "Reality", "meaning": "Stability must be reclaimed before progress."},
]

# =========================
# FUNCTIONS
# =========================
def draw_cards(n):
    return random.sample(deck, n)

def analyze_structure(cards):
    types = [c["type"] for c in cards]
    count = Counter(types)
    dominant = count.most_common(1)[0][0]

    if dominant == "Movement":
        return "This phase is action-oriented. Movement energy dominates."
    elif dominant == "Reflection":
        return "Patterns and self-awareness dominate this moment."
    elif dominant == "Reality":
        return "Grounded truths require attention before progress."
    elif dominant == "Tension":
        return "Internal or structural conflict is present."
    else:
        return "Expansion and scale are emerging themes."

# =========================
# UI
# =========================
st.title("Clarity Deck")
st.caption("Structured reflection for decision clarity.")

draw_mode = st.radio("Choose your reflection depth:", ["1 Card", "3 Cards", "5 Cards"])

# =========================
# REVEAL BUTTON
# =========================
if st.button("Reveal Reflection"):

    if draw_mode == "1 Card":
        n = 1
    elif draw_mode == "3 Cards":
        n = 3
    else:
        n = 5

    cards = draw_cards(n)

    result_text = ""

    for card in cards:
        block = f"""
        <div class="card-box">
            <h3>{card['name']}</h3>
            <p><b>Type:</b> {card['type']}</p>
            <p>{card['meaning']}</p>
        </div>
        """
        st.markdown(block, unsafe_allow_html=True)
        result_text += f"{card['name']} ({card['type']}): {card['meaning']}\n"

    insight = analyze_structure(cards)

    st.markdown("### Structural Insight")
    st.write(insight)

    result_text += f"\nInsight: {insight}"

    # Save to session history
    entry = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mode": draw_mode,
        "result": result_text
    }

    st.session_state.history.append(entry)

# =========================
# SESSION HISTORY
# =========================
st.markdown("---")
st.markdown("## Your Reflection Session")

if st.session_state.history:
    for item in reversed(st.session_state.history):
        with st.expander(f"{item['timestamp']} — {item['mode']}"):
            st.write(item["result"])
else:
    st.info("No reflections yet.")

# =========================
# RESET
# =========================
if st.button("Reset Session"):
    st.session_state.history = []
    st.experimental_rerun()

# =========================
# FOOTER
# =========================
st.markdown(
    f"<div class='footer'>Session ID: {st.session_state.session_id}</div>",
    unsafe_allow_html=True
)
