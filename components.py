
import streamlit as st
from pathlib import Path

ICON_DIR = Path("assets/icons")


def load_icon(filename):
    with open(ICON_DIR / filename, "r", encoding="utf-8") as f:
        return f.read()

# ==========================================
# Data
# ==========================================

POPULAR_QUESTIONS = [
    {
        "icon": load_icon("Clipboard-check.svg"),
        "title": "Admission Process",
        "description": "Learn how to apply for admission.",
        "question": "What is the admission process?"
    },
    {
        "icon":load_icon("documents.svg"),
        "title": "Admission Documents",
        "description": "Required documents for admission.",
        "question": "What documents are required for admission?"
    },
    {
        "icon": load_icon("cap.svg"),
        "title": "Scholarships",
        "description": "Available scholarships and eligibility.",
        "question": "Are there any scholarships available?"
    },
    {
        "icon": load_icon("users.svg"),
        "title": "Clubs & Societies",
        "description": "Explore student clubs and activities.",
        "question": "Tell me about the clubs and societies."
    },
    {
        "icon": load_icon("book-open.svg"),
        "title": "Library",
        "description": "Library timings and facilities.",
        "question": "What are the library timings?"
    },
    {
        "icon": load_icon("house.svg"),
        "title": "Hostel Rules",
        "description": "Hostel regulations and policies.",
        "question": "What are the hostel regulations?"
    },
    {
        "icon": load_icon("wallet.svg"),
        "title": "Hostel Fee",
        "description": "Hostel fee structure.",
        "question": "What is the hostel fee?"
    }
]

# ==========================================
# Hero Section
# ==========================================

def hero_section():
    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-title">🎓 Student Support Portal</div>
            <div class="hero-description">
                Get instant answers from official college documents about admissions,
                academics, hostel, scholarships, library services, regulations,
                and campus life.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

  
# ==========================================
# Sidebar Heading
# ==========================================

def sidebar_heading(title):

    st.markdown(
        (
            f'<div class="sidebar-heading">'
            f'<span class="sidebar-dot"></span>'
            f'<span>{title}</span>'
            f'</div>'
        ),
        unsafe_allow_html=True,
    )

def sidebar_item(label, value):
    st.markdown(
        (
            '<div class="sidebar-content">'
            f'<div><strong>{label}</strong></div>'
            f'<div class="sidebar-value">{value}</div>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )
def sidebar_content(text):

    st.markdown(
        f'<div class="sidebar-content">{text}</div>',
        unsafe_allow_html=True,
    )
# ==========================================
# Feature Cards
# ==========================================

def feature_cards():

    features = [
    {
        "title": "Grounded Responses",
        "description": "Answers generated only from official college documents.",
        "color": "#4ade80",
    },
    {
        "title": "AI Powered",
        "description": "Semantic search combined with Cohere Command-A.",
        "color": "#60a5fa",
    },
    {
        "title": "Source Referenced",
        "description": "Every response includes supporting document sources.",
        "color": "#f59e0b",
    },
]

    cols = st.columns(3)

    for col, feature in zip(cols, features):
        with col:
           html = (
               f'<div class="feature-card">'
               f'<div class="feature-header">'
               f'<span class="feature-dot" style="background:{feature["color"]};"></span>'
               f'<div class="feature-title">{feature["title"]}</div>'
               f'</div>'
               f'<div class="feature-description">{feature["description"]}</div>'
               f'</div>'
            )
           st.markdown(html, unsafe_allow_html=True)


# ==========================================
# Question Cards
# ==========================================
# Custom QuestionCard component will be implemented next.

# ==========================================
# Question Card
# ==========================================

def question_card(item):
    html = (
        f'<div class="question-card">'
        f'<div class="question-icon">{item["icon"]}</div>'
        f'<div class="question-title">{item["title"]}</div>'
        f'<div class="question-description">{item["description"]}</div>'
        f'</div>')
    return html

# ==========================================
# Popular Questions
# ==========================================

def question_cards():

    st.subheader("🎓 Popular Student Questions")

    col1, col2 = st.columns(2)

    for i, item in enumerate(POPULAR_QUESTIONS):

        col = col1 if i % 2 == 0 else col2

        with col:

            st.markdown(
               question_card(item),
               unsafe_allow_html=True,
            )

            if st.button(
                "Ask Question →",
                key=f"question_{i}",
                use_container_width=True,
            ):
                return item["question"]