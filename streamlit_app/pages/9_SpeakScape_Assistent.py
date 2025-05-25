import streamlit as st
import streamlit.components.v1 as components

# ---------------- Page Config ----------------
st.set_page_config(page_title="SpeakScape Assistant", layout="wide")

# ---------------- Custom CSS ----------------
custom_css = """
<style>
.chat-wrapper {
    background-color: #f0f8ff;
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid #dbe9f4;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
    margin-top: 2rem;
    margin-bottom: 2rem;
}

.chat-message {
    display: flex;
    align-items: flex-start;
    margin-bottom: 1.5rem;
    gap: 1rem;
}

.avatar {
    flex-shrink: 0;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #ccc;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    font-size: 16px;
    color: #fff;
}

.avatar.user {
    background-color: #007acc;
}

.avatar.assistant {
    background-color: #4caf50;
}

.bubble {
    padding: 1rem;
    border-radius: 10px;
    border: 1px solid #dcdcdc;
    max-width: 80%;
}

.bubble.user {
    background-color: #ffffff;
}

.bubble.assistant {
    background-color: #e9f1fb;
    border: 1px solid #dbe4f0;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---------------- Title ----------------
st.title("SpeakScape Assistant")
st.markdown("Ask anything about the app, TED Talk analysis, or linguistic metrics.")

# ---------------- State ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- Bot Logic ----------------
def basic_chatbot_response(user_input):
    user_input = user_input.lower()
    if "what is" in user_input and "speakscape" in user_input:
        return "SpeakScape is a BI and NLP tool that analyzes presentation scripts and compares them to successful TED Talks."
    elif "how do i upload" in user_input or "upload speech" in user_input:
        return "Go to **'Upload Your Speech'** in the sidebar. You can paste text or upload a `.txt`, `.docx`, or `.pdf` file."
    elif "sentence length" in user_input:
        return "Average sentence length tells us how concise your speech is. TED Talks typically range between 15–20 words per sentence."
    elif "rhetorical" in user_input:
        return "Rhetorical questions engage the audience by prompting thought. SpeakScape highlights them in your speech feedback."
    elif "imperative" in user_input:
        return "Imperative statements are action-oriented phrases like *'Imagine this…'* or *'Consider that…'*. They're great for engaging listeners."
    elif "who made this" in user_input or "who made it" in user_input:
        return "SpeakScape was built by **Group 4** — Alberte, Felicia & Fatima at CPH Business Academy."
    elif "when was it made" in user_input or "when is it made" in user_input:
        return "SpeakScape was created as a 2025 Business Intelligence Exam Project at CPH Business Academy."
    elif "technical" in user_input or "tools" in user_input:
        return "SpeakScape uses Python, Streamlit, TextBlob, NLTK, SpaCy, and scikit-learn."
    else:
        return "I'm still learning! Try asking about the app sections, metrics, or how to use SpeakScape."

# ---------------- Input ----------------
user_input = st.text_input("Ask me anything about SpeakScape:", placeholder="Ask me anything about SpeakScape...")

# ---------------- Clear Chat Button ----------------
if st.button("Clear Chat"):
    st.session_state.clear()
    st.session_state.chat_history = []  # Ensure key is reset

# ---------------- Process Input ----------------
if user_input and (len(st.session_state.chat_history) == 0 or st.session_state.chat_history[-1]["content"] != user_input):
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    bot_response = basic_chatbot_response(user_input)
    st.session_state.chat_history.append({"role": "assistant", "content": bot_response})

# ---------------- Chat Display ----------------
st.markdown('<div class="chat-wrapper">', unsafe_allow_html=True)

for msg in st.session_state.chat_history:
    role = msg["role"]
    bubble_class = "user" if role == "user" else "assistant"
    avatar_label = "U" if role == "user" else "A"

    st.markdown(f"""
    <div class="chat-message">
        <div class="avatar {bubble_class}">{avatar_label}</div>
        <div class="bubble {bubble_class}">{msg['content']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- Smooth Scroll to Bottom ----------------
components.html("""
<script>
  var chatContainer = window.parent.document.querySelector('.element-container div[data-testid="stMarkdownContainer"]');
  if (chatContainer) {
    chatContainer.scrollTop = chatContainer.scrollHeight;
  }
</script>
""", height=0)

# ---------------- Footer ----------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle | Stock images from Unsplash")
