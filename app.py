import streamlit as st
import datetime

from domain.deck import DECK
from application.engine import draw_cards, analyze_structure
from infrastructure.session import init_session, add_history, reset
from config.i18n import LANGUAGES

st.set_page_config(page_title="Clarity Deck", layout="centered")

init_session()

lang_key = st.radio(
    "Language / ภาษา",
    options=list(LANGUAGES.keys()),
    format_func=lambda x: LANGUAGES[x]["label"],
    horizontal=True
)

T = LANGUAGES[lang_key]

st.title(T["title"])
st.caption(T["subtitle"])

draw_mode = st.radio(T["mode"], ["1 Card", "3 Cards", "5 Cards"])

if st.button(T["reveal"]):

    n = int(draw_mode[0])
    cards = draw_cards(DECK, n)

    result_text = ""

    for card in cards:
        st.subheader(card["name"])
        st.write(f"{T['type']}: {card['type'][lang_key]}")
        st.write(card["meaning"][lang_key])
        result_text += card["meaning"][lang_key] + "\n"

    insight = analyze_structure(cards, lang_key)

    st.markdown(f"### {T['insight']}")
    st.write(insight)

    add_history({
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mode": draw_mode,
        "result": result_text + insight
    })

st.markdown("---")
st.markdown(f"## {T['history']}")

if st.session_state.history:
    for item in reversed(st.session_state.history):
        with st.expander(f"{item['timestamp']} — {item['mode']}"):
            st.write(item["result"])
else:
    st.info(T["no_history"])

if st.button(T["reset"]):
    reset()
    st.experimental_rerun()
