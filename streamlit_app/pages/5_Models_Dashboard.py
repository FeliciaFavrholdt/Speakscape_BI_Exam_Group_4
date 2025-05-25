import streamlit as st

# Page setup
st.set_page_config(page_title="SpeakScape", layout="wide")

st.title("Models Dashboard")

st.markdown("""
This dashboard displays the models used in the TED Talk analysis and feedback generation.  
Each model includes a summary explaining its role and contribution to the overall SpeakScape system.
""")

# ---------- Card Styling ----------
model_card_style = """
<style>
.model-card {
    background-color: #f0f8ff;
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid #dbe9f4;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.03);
    margin-bottom: 1.5rem;
}
.model-card h4 {
    margin-top: 0;
    color: #003366;
}
</style>
"""
st.markdown(model_card_style, unsafe_allow_html=True)

# ---------- Example Models ----------
models = [
    {
        "name": "TextBlob Sentiment Analyzer",
        "summary": "This model analyzes the sentiment of the speech by classifying sentences as positive, negative, or neutral. It helps determine the emotional tone and progression of the talk."
    },
    {
        "name": "SpaCy Named Entity Recognizer",
        "summary": "Identifies named entities (e.g., people, places, organizations) mentioned in the speech. Useful for detecting topical relevance and personal references."
    },
    {
        "name": "Custom Rhetorical Device Detector",
        "summary": "A rule-based pattern matcher developed to highlight rhetorical questions, repetition, and parallel structure. These elements influence engagement and retention."
    },
    {
        "name": "Passive Voice Classifier",
        "summary": "This logistic regression model detects passive sentence structures. It enables SpeakScape to provide advice on making writing more direct and engaging."
    }
]

# ---------- Display Models in Cards ----------
for model in models:
    st.markdown(f"""
    <div class="model-card">
        <h4>{model['name']}</h4>
        <p>{model['summary']}</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("Data source: TED Talk transcripts processed and analyzed by SpeakScape.")
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle | Stock images from Unsplash")
