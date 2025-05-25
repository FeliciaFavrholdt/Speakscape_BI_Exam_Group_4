import streamlit as st

st.set_page_config(page_title="SpeakScape Assistant", layout="wide")

st.title("Scenario Usability Evaluation")
st.markdown("""
This page evaluates the usability of SpeakScape through a real-world scenario.
The scenario demonstrates how a user can effectively utilize the app to improve their presentation script based on TED Talk benchmarks.
""")
st.subheader("Scenario: University Lecturer Preparing a Keynote Speech")

st.markdown("""
**User Role:** University Lecturer  
**Use Case:** Preparing a keynote speech for an education summit

**Steps Taken:**  
1. Uploaded the draft script to SpeakScape  
2. Feedback indicated that sentence length exceeded TED averages by 25% and rhetorical questions were underused  
3. Revised the text by shortening complex sentences and adding thoughtful questions to better engage the audience
""")

st.markdown("""
> “This process helped me reframe my message to be more accessible to a wider audience.” – User Feedback
""")

st.subheader("Scenario: Student Presenting Research Findings")
st.markdown("""
**User Role:** University Student
**Use Case:** Presenting research findings at a conference
            
**Steps Taken:**
1. Uploaded the research presentation script to SpeakScape
2. Received feedback indicating a high passive voice percentage and low rhetorical question usage
3. Revised the script by converting passive sentences to active voice and incorporating rhetorical questions to enhance engagement
""")
st.markdown("""
> “The feedback helped me make my research more engaging and easier to understand for the audience.” – User Feedback
""")

st.subheader("Scenario: Comedian Preparing a Stand-Up Routine")
st.markdown("""
**User Role:** Stand-Up Comedian
**Use Case:** Preparing a stand-up routine for a comedy club
            
**Steps Taken:**
1. Uploaded the draft routine to SpeakScape
2. Feedback indicated that the average sentence length was too long for comedic timing
3. Revised the routine by shortening sentences and adding more punchlines to improve comedic impact
""")
st.markdown("""
> “The feedback helped me tighten my routine and deliver jokes more effectively.” – User Feedback
""")

st. subheader("Scenario: User Preparing a Business Presentation")
st.markdown("""
**User Role:** Business Professional
**Use Case:** Preparing a business presentation for a client meeting
            
**Steps Taken:**
1. Added text directly to SpeakScape via the text input box
2. Received feedback indicating a high passive voice percentage and low rhetorical question usage
3. Revised the script by converting passive sentences to active voice and incorporating rhetorical questions to enhance engagement
""")
st.markdown("""
> “The feedback helped me make my presentation more engaging and persuasive for the client.” – User Feedback
""")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle")
