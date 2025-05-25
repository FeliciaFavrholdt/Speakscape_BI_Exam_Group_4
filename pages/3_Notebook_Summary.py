import streamlit as st

st.set_page_config(page_title="SpeakScape Analysis Summary", layout="wide")

st.title("SpeakScape Analysis Summary")

st.markdown("""
This page summarizes the analytical stages and key findings from the SpeakScape project, documented across Jupyter notebooks.
Each notebook addresses a specific part of the workflow—from raw data loading to linguistic feature analysis and metric modeling. We have collected and processed data from TED Talks to create a comprehensive analysis of presentation effectiveness. The notebooks are designed to be modular, allowing for easy updates and extensions as new data or methods become available. A summary of each notebook is provided below, along with links to view the full notebooks on GitHub.
""")

# Notebook Overview Table
st.header("Notebook Overview")

notebooks = {
    "01 - Data Loading & Exploration": {
        "link": "https://github.com/your-repo/speakscape/blob/main/notebooks/01_data_loading_and_exploration.ipynb",
        "summary": "Initial exploration of TED_2017 and TED_2020 datasets to understand structure, schema, and tag coverage."
    },
    "02 - Data Cleaning": {
        "link": "https://github.com/your-repo/speakscape/blob/main/notebooks/02_data_cleaning.ipynb",
        "summary": "Cleaned and standardized text, recovered missing transcripts, and prepared the datasets for integration."
    },
    "03 - Dataset Integration": {
        "link": "https://github.com/your-repo/speakscape/blob/main/notebooks/03_dataset_integration.ipynb",
        "summary": "Merged TED_2017 and TED_2020 into a unified dataset. Ensured schema consistency and resolved duplicates."
    },
    "04 - Exploratory Analysis": {
        "link": "https://github.com/your-repo/speakscape/blob/main/notebooks/04_exploratory_analysis.ipynb",
        "summary": "Investigated temporal trends, tag distributions, and content structure. Supported strategic visualizations."
    },
    "05 - Feature Extraction": {
        "link": "https://github.com/your-repo/speakscape/blob/main/notebooks/05_feature_extraction.ipynb",
        "summary": "Extracted sentence-level, lexical, and readability features. Created foundational feature matrix."
    },
    "06 - Metric Extraction": {
        "link": "https://github.com/your-repo/speakscape/blob/main/notebooks/06_metric_extraction.ipynb",
        "summary": "Generated advanced metrics such as concreteness, narrative flow, and emotional tone for deeper analysis."
    },
    "07 - Sentence Structure Analysis": {
        "link": "https://github.com/your-repo/speakscape/blob/main/notebooks/07_sentence_structure_analysis.ipynb",
        "summary": "Analyzed sentence complexity, rhetorical devices, and question usage in transcripts. Linked to engagement metrics."
    },
    "08 - Linguistic Feature Analysis": {
        "link": "https://github.com/your-repo/speakscape/blob/main/notebooks/08_linguistic_feature_analysis.ipynb",
        "summary": "Analyzed deeper rhetorical and stylistic features across TED Talks, including emphasis patterns and sentence diversity."
    },
    "09 - Pronoun Usage Analysis": {
        "link": "https://github.com/your-repo/speakscape/blob/main/notebooks/09_pronoun_usage_analysis.ipynb",
        "summary": "Investigated personal vs. impersonal language trends and how pronoun choices affect audience connection and clarity."
    },
}

for title, info in notebooks.items():
    st.markdown(f"### {title}")
    st.markdown(f"[View Notebook]({info['link']})")
    st.markdown(f"*{info['summary']}*")


st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle")
