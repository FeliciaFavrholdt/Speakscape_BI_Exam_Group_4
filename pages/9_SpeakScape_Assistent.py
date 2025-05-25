import streamlit as st

st.set_page_config(page_title="SpeakScape", layout="wide")

st.title("SpeakScape Assistant")
st.markdown("Ask anything about the app, TED Talk analysis, or linguistic metrics.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Define basic responses
def basic_chatbot_response(user_input):
    user_input = user_input.lower()

    if "what is" in user_input and "speakscape" in user_input:
        return "SpeakScape is a BI and NLP tool that analyzes presentation scripts and compares them to successful TED Talks."
    elif "how do i upload" in user_input or "upload speech" in user_input:
        return "Go to 'Upload Your Speech' in the sidebar. You can paste text or upload a .txt, .docx, or .pdf file."
    elif "sentence length" in user_input:
        return "Average sentence length tells us how concise your speech is. TED Talks typically range between 15–20 words per sentence."
    elif "rhetorical" in user_input:
        return "Rhetorical questions engage the audience by prompting thought. SpeakScape highlights them in your speech feedback."
    elif "imperative" in user_input:
        return "Imperative statements are action-oriented phrases like 'Imagine this…' or 'Consider that…'. They're great for engaging listeners."
    elif "who made this" in user_input:
        return "SpeakScape was built by Group 4 — Alberte, Felicia & Fatima at CPH Business Academy."
    elif "technical" in user_input or "tools" in user_input:
        return "SpeakScape uses Python, Streamlit, TextBlob, NLTK, SpaCy, and scikit-learn."
    else:
        return "I'm still learning! Try asking about the app sections, metrics, or how to use SpeakScape."

# Chat input
user_input = st.chat_input("Ask me anything about SpeakScape...")

if user_input:
    # Store user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    # Generate and store bot response
    response = basic_chatbot_response(user_input)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle")
