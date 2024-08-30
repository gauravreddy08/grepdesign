from src.GreptileProcessor import Greptile
from src.LLM import LLM
import streamlit as st

st.title("GrepDesign")
st.markdown("###### Made by Gaurav Tadkapally")

repo = st.sidebar.text_input("Enter repository", placeholder="owner/repository-name")
branch = st.sidebar.text_input("Enter branch", value="main")
submit = st.sidebar.button("Submit")

if submit and repo:
    if "repo" not in st.session_state:
        st.session_state.repo = repo

if "repo" in st.session_state:
    if branch is None: branch = 'main'

    if "messages" not in st.session_state:
        st.session_state.messages = []

        st.session_state.greptile = Greptile(repository=st.session_state.repo,
                            branch=branch)
        st.session_state.llm = LLM(greptile=st.session_state.greptile)

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input(f"Message GrepDesign"):

        st.session_state.messages.append({"role": "user", "content": prompt})  
        with st.chat_message("user"):
            st.markdown(prompt)

        response = st.session_state.llm.call(prompt)

        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)