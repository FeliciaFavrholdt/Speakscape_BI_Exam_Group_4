import streamlit as st


st.set_page_config(page_title="SpeakScape", layout="wide")

st.title("Project Overview")
st.markdown("""
This project is designed as data analytics experimental research and development of BI implementation
solution. It involves systematic and creative work of finding novel, uncertain, and reproducible results by
applying modern BI and artificial intelligence (AI) technologies in a context.


SpeakScape is an innovative tool designed to enhance public speaking by providing personalized, data-driven feedback based on TED Talk benchmarks.
By analyzing linguistic patterns in TED Talk transcripts, SpeakScape offers actionable insights to help users improve their presentation skills, focusing on clarity, emotional impact, and audience engagement.
""")

st.subheader("Context and Purpose")
st.markdown("""
SpeakScape addresses a critical gap in presentation development by replacing vague, subjective feedback with accessible, personalized, and evidence-based recommendations.  
While various presentation feedback tools exist, most focus on delivery mechanics or slides—not content. SpeakScape fills this gap by providing structured, linguistic-based recommendations.
""")

st.subheader("Problem Formulation")
st.markdown("""
How can SpeakScape provide actionable, data-driven feedback to users by analyzing their presentation text against TED Talk benchmarks to identify impactful linguistic patterns?
""")
st.markdown("""
- What specific linguistic features—such as sentence complexity, pronoun usage, and rhetorical devices—are most predictive of audience engagement in TED Talks?  
            
- How can we effectively correlate these linguistic features with engagement metrics to identify successful presentation strategies? 
             
- How can we establish personalized benchmarks that provide tailored feedback to users based on successful talks in similar categories?
""")

st.subheader("Research Questions")
st.markdown("""
- Which linguistic patterns correlate most with engagement?  
- What metrics best represent effective speech structure?    
- How can these metrics be used to generate actionable feedback?
""")

st.subheader("Our Approach")
st.markdown("""
SpeakScape uses NLP and BI techniques to analyze TED Talk transcripts. User-submitted scripts are benchmarked against high-performing talks by category, producing personalized, data-driven suggestions.

**SpeakScape combines**:
- Domain-specific benchmarking  
- Data-driven linguistic recommendations  
- Contextual feedback by category and purpose  
- Focus on structure and rhetorical strategy (not just delivery)
""")

st.subheader("Beyond Text Analysis")
st.markdown("""
Future enhancements will include:
- Speech delivery metrics (pauses, pacing)  
- Slide content analysis  
- Audio tone and sentiment analysis
""")

st.subheader("Project Annotation")
st.markdown("""
SpeakScape demonstrates that NLP-driven benchmarking against TED Talks can offer meaningful presentation feedback. This approach is scalable and adaptable across industries and presentation types.
""")


st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle | Stock images from Unsplash")