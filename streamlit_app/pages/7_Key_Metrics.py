import streamlit as st

# Page setup
st.set_page_config(page_title="SpeakScape", layout="wide")

st.title("Key Metrics in SpeakScape")
st.markdown("This page explains the meaning behind the key metrics and visualizations used in SpeakScape.")

# Card styles
card_style = """
<style>
.metric-card {
    background-color: #f0f8ff;
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid #dbe9f4;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.03);
    margin-bottom: 1.5rem;
}
.metric-card h4 {
    margin-top: 0;
    margin-bottom: 0.8rem;
    color: #003366;
}
.metric-card ul {
    margin: 0;
    padding-left: 1rem;
}
</style>
"""
st.markdown(card_style, unsafe_allow_html=True)

# Metric cards
metrics = [
    {
        "title": "Average Sentence Length",
        "what": "The average number of words per sentence in a presentation script.",
        "why": "Shorter sentences generally improve clarity and readability. High-performing TED Talks tend to maintain an average sentence length between 15–20 words."
    },
    {
        "title": "Passive Voice Percentage",
        "what": "The proportion of sentences written in passive voice.",
        "why": "Active voice is more direct and engaging. Reducing passive constructions can make content more impactful and easier to follow."
    },
    {
        "title": "Rhetorical Questions",
        "what": "The frequency of rhetorical or open-ended questions.",
        "why": "Well-placed rhetorical questions can keep the audience engaged and encourage deeper reflection."
    },
    {
        "title": "Imperative Statements",
        "what": "The number of direct, action-driven sentences (e.g., “Consider this...”, “Think about...”)",
        "why": "Imperatives signal confidence and encourage audience participation or visualization, often improving emotional engagement."
    }
]

# Display cards in 2-column layout
cols = st.columns(2)
for idx, metric in enumerate(metrics):
    with cols[idx % 2]:
        st.markdown(f"""
        <div class="metric-card">
            <h4>{metric['title']}</h4>
            <ul>
                <li><strong>What it shows:</strong> {metric['what']}</li>
                <li><strong>Why it matters:</strong> {metric['why']}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle | Stock images from Unsplash")
