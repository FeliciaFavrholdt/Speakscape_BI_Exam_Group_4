import streamlit as st


st.set_page_config(page_title="SpeakScape", layout="wide")

st.title("Key Metrics in SpeakScape")
st.markdown("This page explains the meaning behind the key metrics and visualizations used in SpeakScape.")

st.subheader("Average Sentence Length")
st.markdown("""
- **What it shows:** The average number of words per sentence in a presentation script.
- **Why it matters:** Shorter sentences generally improve clarity and readability. High-performing TED Talks tend to maintain an average sentence length between 15–20 words.
""")

st.subheader("Passive Voice Percentage")
st.markdown("""
- **What it shows:** The proportion of sentences written in passive voice.
- **Why it matters:** Active voice is more direct and engaging. Reducing passive constructions can make content more impactful and easier to follow.
""")

st.subheader("Rhetorical Questions")
st.markdown("""
- **What it shows:** The frequency of rhetorical or open-ended questions.
- **Why it matters:** Well-placed rhetorical questions can keep the audience engaged and encourage deeper reflection.
""")

st.subheader("Imperative Statements")
st.markdown("""
- **What it shows:** The number of direct, action-driven sentences (e.g., “Consider this...”, “Think about...”).
- **Why it matters:** Imperatives signal confidence and encourage audience participation or visualization, often improving emotional engagement.
""")


st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle")
