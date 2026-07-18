import streamlit as st

from chain import ask_question
from components import (
    hero_section,
    feature_cards,
    question_cards,
    sidebar_heading,
    sidebar_item,
    sidebar_content,
)

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Student Support AI",
    page_icon="🎓",
    layout="wide",
)


# ==========================================
# Load CSS
# ==========================================

def load_css():
    with open("styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )


load_css()


# ==========================================
# Sidebar
# ==========================================

with st.sidebar:

    st.title("Student Support AI")

    sidebar_heading("System Status")

    sidebar_item("Documents", "8")
    sidebar_item("Knowledge Chunks", "1050")

    sidebar_heading("Embedding Model")
    sidebar_content("all-MiniLM-L6-v2")
    

    sidebar_heading("LLM")
    sidebar_content("Cohere Command-A")


    st.divider()

    sidebar_heading("Grounded AI")

    st.info(
        "This assistant answers questions only from official college documents. "
        "If the requested information is unavailable, it will let you know rather than guessing."
    )

    st.divider()

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ==========================================
# Session State
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==========================================
# Main UI
# ==========================================

hero_section()

feature_cards()


# ==========================================
# Popular Questions
# ==========================================

if not st.session_state.messages:
    selected_question = question_cards()
else:
    selected_question = None


# ==========================================
# Conversation History
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            sources = message.get("sources", [])

            if sources:
                with st.expander("📄 Sources"):
                    for source in sources:
                        st.write(f"• {source}")


# ==========================================
# Chat Input
# ==========================================

typed_question = st.chat_input(
    "Ask about admissions, hostel, fees, scholarships..."
)

# Question card selection takes priority over typed input
query = selected_question or typed_question


# ==========================================
# Process Query
# ==========================================

if query:

    # User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query,
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    # Assistant Message
    with st.chat_message("assistant"):

        with st.spinner("Looking through official college documents..."):
            result = ask_question(query)

        st.markdown(result["answer"])

        if result["sources"]:
            with st.expander("📄 Sources"):
                for source in result["sources"]:
                    st.write(f"• {source}")

    # Save Assistant Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"],
            "sources": result["sources"],
        }
    )

    # Hide question cards after first interaction
    st.rerun()