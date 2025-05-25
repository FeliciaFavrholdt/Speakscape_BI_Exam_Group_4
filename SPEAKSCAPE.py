import streamlit as st

st.set_page_config(page_title="SpeakScape", layout="wide")

st.title("Welcome to SpeakScape")

st.markdown("""
**SpeakScape** is a business intelligence application that provides data-driven feedback on presentation content, inspired by the language patterns of TED Talks. By analyzing transcripts and correlating linguistic features with audience engagement metrics, SpeakScape helps presenters improve clarity, emotional impact, and relevance.

It combines these insights to create a complete picture of presentation effectiveness, contributing to the final SpeakScape recommendation system that helps users improve their presentation skills based on proven patterns from successful TED Talks.
""")

st.markdown("""
### TED Talk Analysis  
- **Project Overview** – Learn the motivation, research questions, and hypotheses behind SpeakScape  
- **Technical Overview** – See the tools, libraries, and system architecture used  
- **SpeakScape Analysis Summary** – Explore what each notebook stage revealed  
- **Linguistic Visualisations** – View how sentence complexity, rhetorical devices, and tone evolve over time

### SpeakScape App  
- **TED Talk Search** – Find TED Talks based on topic, speaker, or tag  
- **Upload Your Speech** – Get personalized feedback on your uploaded script  
- **Insights** – Understand how linguistic metrics correlate with audience engagement
""")

st.markdown("""
            ### Created By:
Group 4 – Alberte, Felicia & Fatima  
CPH Business Academy – Lyngby  
Business Intelligence Exam Project 2025
""")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle")
