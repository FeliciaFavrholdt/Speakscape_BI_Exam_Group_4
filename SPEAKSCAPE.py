import streamlit as st

st.set_page_config(page_title="SpeakScape", layout="wide")

st.title("Welcome to SpeakScape")

st.markdown("""
**SpeakScape** is a business intelligence application that provides data-driven feedback on presentation content, inspired by the language patterns of TED Talks. 

By analyzing transcripts and correlating linguistic features with audience engagement metrics, SpeakScape helps presenters improve clarity, emotional impact, and relevance.
It combines these insights to create a complete picture of presentation effectiveness, contributing to the final SpeakScape recommendation system that helps users improve their presentation skills based on proven patterns from successful TED Talks.
""")

st.markdown("""
### TED Talk Analysis  
- **Project Overview** – Learn the motivation, research questions, and hypotheses behind SpeakScape  
- **Technical Overview** – See the tools, libraries, and system architecture used  
- **SpeakScape Notebook Summary** – Explore what each notebook stage revealed  
- **Linguistic Visualisations** – View how sentence complexity, rhetorical devices, and tone evolve over time
- **Analysis Models** – Understand the models used to analyze TED Talks and their impact on audience engagement

### SpeakScape App  
- **TED Talk Search** – Find TED Talks based on topic, speaker, or tag  
- **Upload Your Speech** – Get personalized feedback on your uploaded script  
- **Key Metrics** – Understand the key metrics used to evaluate presentations 
- **Upload Your Speech** – Get personalized feedback on your uploaded script
- **SpeakScape Assistant** – Ask questions and get real-time feedback on your presentation script
- **Usability Evaluation** – Participate in our usability study to help improve SpeakScape - share your thoughts and experiences
""")

st.markdown("""
            ### Created By:
Group 4 – Alberte, Felicia & Fatima  
CPH Business Academy – Lyngby  
Business Intelligence Exam Project 2025
""")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle")
