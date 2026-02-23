import uuid
import streamlit as st

def init_session():
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    if "history" not in st.session_state:
        st.session_state.history = []

def add_history(entry):
    st.session_state.history.append(entry)

def reset():
    st.session_state.history = []
