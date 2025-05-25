import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Technical Overview", layout="wide")

st.title("Technical Overview")

st.subheader("Technologies Used")
st.markdown("""
The following tools and libraries were used throughout the development of the SpeakScape platform:

- **Python** – Core programming language for data handling and NLP tasks  
- **Jupyter Notebook** – For exploratory data analysis and model experimentation  
- **Streamlit** – Used to build the interactive user interface  
- **Pandas** – For data cleaning, transformation, and feature preparation  
- **Matplotlib & Seaborn** – For generating statistical visualizations  
- **Scikit-learn** – Used in feature engineering and statistical modeling  
- **SpaCy** – Applied for tokenization and part-of-speech tagging  
- **NLTK** – Used for rhetorical device detection and text parsing  
- **JSON/CSV** – Format of source and processed TED Talk datasets
""")

st.subheader("System Architecture")
st.markdown("""
SpeakScape follows a modular and iterative data pipeline structure:

- **Data Collection & Integration**: Merged TED 2017 and 2020 datasets into a unified source  
- **Data Cleaning**: Removed duplicates, standardized columns, recovered missing transcripts  
- **Feature Engineering**:
  - Sentence length and structure metrics
  - Passive voice detection
  - Rhetorical and imperative phrase frequency  
- **Benchmarking Module**: Compared user speech against linguistic benchmarks from top TED Talks  
- **Dashboard Interface**: Visualized trends and metrics with interactive filtering
""")

st.subheader("Architecture Diagram")
mermaid_code = """
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

<div class="mermaid">
flowchart TD
    A[TED Talk Datasets] --> B[Cleaning & Integration]
    B --> C[Feature Extraction]
    F[User Speech Upload] --> G[Text Parsing & Feature Extraction]
    C --> D[Benchmarking Engine]
    G --> D
    D --> E[Feedback & Recommendations]
    E --> H[Streamlit Interface]
</div>
"""

components.html(mermaid_code, height=500)

st.header("Application Outputs")
st.markdown("""
- **TED Talk Visual Dashboard** – Allows users to explore linguistic trends and filters by tag or year  
- **Speech Upload Tool** – Accepts user input via file or text area and performs structural and sentiment analysis  
- **Feedback Engine** – Generates real-time recommendations based on statistical alignment with TED performance data
""")
