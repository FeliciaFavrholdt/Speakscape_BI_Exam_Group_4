import streamlit as st

st.set_page_config(page_title="SpeakScape", layout="wide")

st.title("Thanks for giving us feedback!")
st.markdown("""
This page allows you to share your feedback on the usability of SpeakScape based on real-world scenarios.
We appreciate your insights and experiences, which will help us improve the app for future users.
""")

st.image("images/image_3.jpg", caption="Stock Image 3", use_container_width=True)

# ---------- Feedback Section ----------
st.subheader("Fill out the feedback form below:")

st.markdown("""
We would love to hear your thoughts!  
Please share your experience with SpeakScape based on the scenarios above or your own use.  
Your feedback will help us improve the app for future users.
""")

# Create a session state list to store feedback entries
if "feedback_entries" not in st.session_state:
    st.session_state.feedback_entries = []

# Rating
satisfaction = st.radio("How satisfied are you with the usability of SpeakScape?", [1, 2, 3, 4, 5], index=4, horizontal=True)

# Free-text input
feedback_text = st.text_area("Please share any comments, suggestions, or personal experiences:")

# Submit button
if st.button("Submit Feedback"):
    if feedback_text.strip():
        entry = {
            "rating": satisfaction,
            "comment": feedback_text.strip()
        }
        st.session_state.feedback_entries.append(entry)
        st.success("Thank you for your feedback!")
    else:
        st.warning("Please write something before submitting.")

# Display stored feedback
if st.session_state.feedback_entries:
    st.markdown("### Submitted Feedback")
    for i, entry in enumerate(reversed(st.session_state.feedback_entries), 1):
        st.markdown(f"**Feedback #{i}** – ⭐️ {entry['rating']}/5")
        st.markdown(f"> {entry['comment']}")
        st.markdown("---")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle | Stock images from Unsplash")