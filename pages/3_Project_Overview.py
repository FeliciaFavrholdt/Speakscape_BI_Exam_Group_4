import streamlit as st


st.set_page_config(page_title="Project Overview", layout="wide")


st.title("Project Overview")

st.header("Problem Formulation")
st.markdown("""
How can SpeakScape provide actionable, data-driven feedback to users by analyzing their presentation text against TED Talk benchmarks to identify impactful linguistic patterns?
""")
st.markdown("""
- What specific linguistic features—such as sentence complexity, pronoun usage, and rhetorical devices—are most predictive of audience engagement in TED Talks?  
            
- How can we effectively correlate these linguistic features with engagement metrics (views, ratings, comments) to identify successful presentation strategies? 
             
- How can we establish personalized benchmarks that provide tailored feedback to users based on successful talks in similar categories?
""")

st.subheader("Context and Purpose")
st.markdown("""
SpeakScape addresses a critical gap in presentation development by replacing vague, subjective feedback with accessible, personalized, and evidence-based recommendations.
""")

st.subheader("The Challenge")
st.markdown("""
While various presentation feedback tools exist, most focus on delivery mechanics or slides—not content. SpeakScape fills this gap by providing structured, linguistic-based recommendations.
""")

st.subheader("Our Approach")
st.markdown("""
SpeakScape uses NLP and BI techniques to analyze TED Talk transcripts. User-submitted scripts are benchmarked against high-performing talks by category, producing personalized, data-driven suggestions.
""")

st.subheader("Beyond Text Analysis")
st.markdown("""
Future enhancements will include:
- Speech delivery metrics (pauses, pacing)  
- Slide content analysis  
- Audio tone and sentiment analysis
""")

st.subheader("Research Questions")
st.markdown("""
- Which linguistic patterns correlate most with engagement?  
- What metrics best represent effective speech structure?    
- How can these metrics be used to generate actionable feedback?
""")

st.subheader("Hypothesis")
st.markdown("""
TED Talks with higher engagement show measurable linguistic traits. These traits can be modeled and used to guide speakers in improving clarity, emotional connection, and persuasiveness.
""")

st.subheader("Differentiation from Existing Solutions")
st.markdown("""
SpeakScape combines:
- Domain-specific benchmarking  
- Data-driven linguistic recommendations  
- Contextual feedback by category and purpose  
- Focus on structure and rhetorical strategy (not just delivery)
""")

st.subheader("Project Annotation")
st.markdown("""
SpeakScape demonstrates that NLP-driven benchmarking against TED Talks can offer meaningful presentation feedback. This approach is scalable and adaptable across industries and presentation types.
""")


st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle")
