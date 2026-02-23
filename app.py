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
# LANGUAGE SWITCH
# =========================
language = st.radio("Language / ภาษา", ["English", "ไทย"], horizontal=True)

# =========================
# TEXT MAP
# =========================
TEXT = {
    "English": {
        "title": "Clarity Deck",
        "subtitle": "Structured reflection for decision clarity.",
        "mode": "Choose your reflection depth:",
        "reveal": "Reveal Reflection",
        "insight": "Structural Insight",
        "history": "Your Reflection Session",
        "no_history": "No reflections yet.",
        "reset": "Reset Session",
        "type": "Type"
    },
    "ไทย": {
        "title": "Clarity Deck",
        "subtitle": "ระบบสะท้อนความคิดเพื่อความชัดเจนในการตัดสินใจ",
        "mode": "เลือกระดับการสะท้อน:",
        "reveal": "เปิดการสะท้อน",
        "insight": "การวิเคราะห์โครงสร้าง",
        "history": "ประวัติการสะท้อนของคุณ",
        "no_history": "ยังไม่มีการสะท้อน",
        "reset": "รีเซ็ตเซสชัน",
        "type": "ประเภท"
    }
}

T = TEXT[language]

# =========================
# DECK (2 LANGUAGE)
# =========================
deck = [
    {
        "name": "FLOW",
        "type": {"English": "Movement", "ไทย": "การเคลื่อนไหว"},
        "meaning": {
            "English": "Momentum is building. Continue forward intentionally.",
            "ไทย": "แรงขับกำลังก่อตัว เดินหน้าต่ออย่างมีเจตนา"
        }
    },
    {
        "name": "ECHO",
        "type": {"English": "Reflection", "ไทย": "การสะท้อน"},
        "meaning": {
            "English": "Past patterns are resurfacing. Notice repetition.",
            "ไทย": "รูปแบบเดิมกำลังย้อนกลับมา สังเกตความซ้ำ"
        }
    },
    {
        "name": "FRACTURE",
        "type": {"English": "Tension", "ไทย": "ความตึงเครียด"},
        "meaning": {
            "English": "There is instability. Something needs restructuring.",
            "ไทย": "มีความไม่มั่นคง บางอย่างต้องปรับโครงสร้างใหม่"
        }
    },
    {
        "name": "GRAVITY",
        "type": {"English": "Reality", "ไทย": "ความจริง"},
        "meaning": {
            "English": "A hard truth requires your attention.",
            "ไทย": "ความจริงบางอย่างต้องการการยอมรับ"
        }
    }
]

# =========================
# FUNCTIONS
# =========================
def draw_cards(n):
    return random.sample(deck, n)

def analyze_structure(cards):
    types = [c["type"][language] for c in cards]
    dominant = Counter(types).most_common(1)[0][0]

    if language == "English":
        return f"Dominant theme: {dominant}. Reflect on its influence."
    else:
        return f"ธีมหลักคือ {dominant} พิจารณาว่ามันส่งผลอย่างไรต่อคุณ"

# =========================
# UI
# =========================
st.title(T["title"])
st.caption(T["subtitle"])

draw_mode = st.radio(T["mode"], ["1 Card", "3 Cards", "5 Cards"])

if st.button(T["reveal"]):

    n = int(draw_mode[0])
    cards = draw_cards(n)

    result_text = ""

    for card in cards:
        block = f"""
        <div class="card-box">
            <h3>{card['name']}</h3>
            <p><b>{T['type']}:</b> {card['type'][language]}</p>
            <p>{card['meaning'][language]}</p>
        </div>
        """
        st.markdown(block, unsafe_allow_html=True)
        result_text += f"{card['name']} - {card['meaning'][language]}\n"

    insight = analyze_structure(cards)

    st.markdown(f"### {T['insight']}")
    st.write(insight)

    entry = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mode": draw_mode,
        "result": result_text + "\n" + insight
    }

    st.session_state.history.append(entry)

# =========================
# HISTORY
# =========================
st.markdown("---")
st.markdown(f"## {T['history']}")

if st.session_state.history:
    for item in reversed(st.session_state.history):
        with st.expander(f"{item['timestamp']} — {item['mode']}"):
            st.write(item["result"])
else:
    st.info(T["no_history"])

if st.button(T["reset"]):
    st.session_state.history = []
    st.experimental_rerun()

st.markdown(
    f"<div class='footer'>Session ID: {st.session_state.session_id}</div>",
    unsafe_allow_html=True
)
