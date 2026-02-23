import streamlit as st
import os

from domain.models import DecisionContext
from infrastructure.gpt_client import GPTInsightClient
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

    gpt = GPTInsightClient(api_key=st.secrets["OPENAI_API_KEY"])
    deck_repo = DeckRepository()
    use_case = RunReadingUseCase(deck_repo, gpt)

    reading, analysis = use_case.execute(context, num_cards)

    st.divider()
    st.header("Cards Drawn")

    for card in reading.cards:
        st.markdown(f"### {card.name}")
        st.write(card.meaning)

    st.divider()
    st.header("AI Strategic Insight")
    st.write(analysis)
