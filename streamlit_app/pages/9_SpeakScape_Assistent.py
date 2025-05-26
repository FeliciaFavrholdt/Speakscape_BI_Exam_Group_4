import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import re
import random

# ---------------- Page Config ----------------
st.set_page_config(page_title="SpeakScape Assistant", layout="wide")
st.title("SpeakScape Assistant")
st.subheader("Ask about TED Talks, data insights, or try one of the suggestions below.")


# ---------------- Load Dataset ----------------
@st.cache_data(show_spinner=False)
def load_combined_data():
    try:
        return pd.read_csv("data/processed/combined_dataset.csv")
    except:
        return pd.DataFrame()

data = load_combined_data()

# ---------------- Chat Memory ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- Prompt Help System ----------------
example_prompts = [
    "Most viewed TED Talks",
    "Show talks by maira kalman",
    "Talks from event TED2020",
    "Talks recorded in 2020",
    "Talks with the tag AI",
    "Average sentence length",
    "Funniest talk",
    "Suggest a funny talk",
    "Talks by speakers with occupation designer",
    "Talks that mention climate",
    "Talks with low completeness",
    "Compare average views by event"
]

col1, col2, col3 = st.columns([4, 2, 2])

with col1:
    selected_example = st.selectbox("💡 Try an example question:", [""] + example_prompts, index=0)
    if selected_example:
        st.session_state.user_input_value = selected_example

with col2:
    if st.button("🎲 Generate Random Prompt"):
        st.session_state.user_input_value = random.choice(example_prompts)

with col3:
    if st.button("🔁 Repeat Last Prompt"):
        last_user_input = [m for m in st.session_state.chat_history if m["role"] == "user"]
        if last_user_input:
            st.session_state.user_input_value = last_user_input[-1]["content"]

# ---------------- Helper Functions ----------------
def get_average_sentence_length():
    if not data.empty and "transcript" in data.columns:
        return round(data["transcript"].dropna().apply(lambda x: len(str(x).split())).mean(), 2)
    return None

def get_average_duration():
    if not data.empty and "duration" in data.columns:
        return round(data["duration"].dropna().astype(float).mean(), 2)
    return None

def get_most_viewed_talks(n=3):
    if not data.empty and "views" in data.columns:
        return data.sort_values(by="views", ascending=False).head(n)
    return None

def get_first_n_talks(n=10):
    return data[["title", "speaker", "duration", "event"]].head(n) if not data.empty else None

def get_speaker_stats():
    if not data.empty and "speaker" in data.columns:
        return data["speaker"].value_counts().head(5)
    return None

def get_talks_by_speaker(name):
    if not data.empty and "speaker" in data.columns:
        return data[data["speaker"].str.lower() == name.lower()]
    return pd.DataFrame()

def get_talks_by_event(keyword):
    if not data.empty and "event" in data.columns:
        return data[data["event"].str.lower().str.contains(keyword.lower())]
    return pd.DataFrame()

def basic_chatbot_response(user_input):
    user_input = user_input.lower()

    if "average sentence length" in user_input:
        avg = get_average_sentence_length()
        return f"Average sentence length is {avg} words." if avg else "No data available."

    elif "average duration" in user_input:
        avg = get_average_duration()
        return f"Average duration is {avg} seconds." if avg else "No data available."

    elif "most viewed" in user_input:
        df = get_most_viewed_talks()
        if df is not None:
            st.dataframe(df[["title", "views"]])
            return "Top most viewed TED Talks:"
        return "No view data available."

    elif "show talks by" in user_input:
        name = user_input.split("show talks by")[-1].strip()
        df = get_talks_by_speaker(name)
        if not df.empty:
            st.dataframe(df[["title", "event", "views"]])
            return f"Talks by {name.title()}"
        return "No talks found."

    elif "talks from event" in user_input:
        keyword = user_input.split("event")[-1].strip()
        df = get_talks_by_event(keyword)
        if not df.empty:
            st.dataframe(df[["title", "event"]])
            return f"Talks from event: {keyword.title()}"
        return "No matching talks found."

    elif "tag" in user_input:
        match = re.search(r"tag (.+)", user_input)
        if match:
            tag = match.group(1)
            df = data[data["tags"].str.lower().str.contains(tag.lower(), na=False)]
            if not df.empty:
                st.dataframe(df[["title", "tags"]])
                return f"Talks with tag '{tag}'"
            return "No matching talks."

    elif "talks recorded in 2020" in user_input:
        df = data[data["recorded_date"].str.startswith("2020", na=False)]
        if not df.empty:
            st.dataframe(df[["title", "recorded_date"]])
            return "Talks from 2020"
        return "No 2020 talks found."

    elif "compare average views" in user_input:
        df = data.groupby("event")["views"].mean().sort_values(ascending=False)
        st.dataframe(df.round(2))
        return "Average views per event:"

    elif "funny" in user_input or "suggest" in user_input:
        if "transcript" in data.columns:
            df = data[data["transcript"].str.contains("laughter", case=False, na=False)]
            if not df.empty:
                talk = df.sample(1).iloc[0]
                return f"Try this funny talk: [{talk['title']}]({talk['url']})"
        return "No funny talks found."

    return "I'm still learning – try asking about views, duration, or speaker info."

# ---------------- Input Field ----------------
user_input = st.text_input(
    "Ask me anything about SpeakScape:",
    value=st.session_state.get("user_input_value", ""),
    placeholder="e.g., What is the average duration?",
    key="text_input_box"
)

# ---------------- Clear Chat ----------------
if st.button("Clear Chat"):
    st.session_state.clear()
    st.session_state.chat_history = []

# ---------------- Chat Handling ----------------
if user_input and (len(st.session_state.chat_history) == 0 or st.session_state.chat_history[-1]["content"] != user_input):
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    response = basic_chatbot_response(user_input)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# ---------------- Chat UI ----------------
st.markdown("""
<style>
.chat-wrapper {
    background-color: #f0f8ff;
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid #dbe9f4;
    margin-top: 2rem;
}
.chat-message {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.2rem;
}
.avatar {
    background-color: #4caf50;
    border-radius: 50%;
    width: 36px;
    height: 36px;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
}
.avatar.user { background-color: #007acc; }
.bubble {
    background-color: #eaf4ff;
    padding: 1rem;
    border-radius: 10px;
    max-width: 80%;
    border: 1px solid #dbe4f0;
}
.bubble.user {
    background-color: white;
    border: 1px solid #ccc;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="chat-wrapper">', unsafe_allow_html=True)

for msg in st.session_state.chat_history:
    role = msg["role"]
    initial = "U" if role == "user" else "A"
    bubble_class = "user" if role == "user" else "assistant"
    st.markdown(f"""
    <div class="chat-message">
        <div class="avatar {bubble_class}">{initial}</div>
        <div class="bubble {bubble_class}">{msg['content']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- Scroll Script ----------------
components.html("""
<script>
var chatContainer = window.parent.document.querySelector('.element-container div[data-testid="stMarkdownContainer"]');
if (chatContainer) { chatContainer.scrollTop = chatContainer.scrollHeight; }
</script>
""", height=0)

# ---------------- Footer ----------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | SpeakScape — Group 4 | Alberte, Felicia & Fatima")
