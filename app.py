import streamlit as st

from domain.models import DecisionContext
from infrastructure.gpt_client import GPTClient
from infrastructure.deck_repository import DeckRepository
from application.use_cases import RunReadingUseCase


st.set_page_config(page_title="Clarity Deck AI", layout="centered")

st.title("Clarity Deck — AI Insight Engine")
st.subheader("1. Define Your Decision Context")

topic = st.text_input("Topic")
situation = st.text_area("Current Situation")
goal = st.text_input("Desired Goal")
fear = st.text_input("Main Fear")

num_cards = st.radio("Number of Cards", [1, 3, 5])

if st.button("Generate AI Insight"):

    context = DecisionContext(
        topic=topic,
        situation=situation,
        goal=goal,
        fear=fear,
    )

    deck_repo = DeckRepository()
    gpt = GPTClient()
    use_case = RunReadingUseCase(deck_repo, gpt)

    reading, analysis = use_case.execute(context, num_cards)

    # ---------- Premium CSS ----------
    st.markdown("""
    <style>
    .card-box {
        background-color: #111827;
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 20px;
        border: 1px solid #1f2937;
        box-shadow: 0 4px 20px rgba(0,0,0,0.25);
    }
    .card-title {
        font-size: 22px;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .card-description {
        font-size: 15px;
        opacity: 0.85;
        line-height: 1.6;
    }
    .insight-box {
        background-color: #0f172a;
        padding: 28px;
        border-radius: 18px;
        margin-top: 30px;
        border: 1px solid #1e293b;
        box-shadow: 0 6px 30px rgba(0,0,0,0.35);
    }
    </style>
    """, unsafe_allow_html=True)

    st.divider()
    st.subheader("Cards Drawn")

    for card in reading.cards:

        if isinstance(card, dict):
            title = card.get("title", "Untitled Card")
            description = card.get("description", "")
        else:
            title = str(card)
            description = ""

        st.markdown(f"""
        <div class="card-box">
            <div class="card-title">{title}</div>
            <div class="card-description">{description}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="insight-box">', unsafe_allow_html=True)
    st.subheader("AI Strategic Insight")
    st.write(analysis)
    st.markdown('</div>', unsafe_allow_html=True)
