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
        "name": "Some title",
        "summary": "some summary of the model. This model is used to analyze the TED Talk transcripts and provide insights into the content."
    },
    {
        "name": "Some title",
        "summary": "some summary of the model. This model is used to analyze the TED Talk transcripts and provide insights into the content."
    },
    {
        "name": "Some title",
        "summary": "some summary of the model. This model is used to analyze the TED Talk transcripts and provide insights into the content."
    },
    {
        "name": "Some title",
        "summary": "some summary of the model. This model is used to analyze the TED Talk transcripts and provide insights into the content."
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
