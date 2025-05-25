import streamlit as st

st.set_page_config(page_title="SpeakScape", layout="wide")

st.title("Scenarios for SpeakScape Usability")

st.markdown("""
This page evaluates the usability of SpeakScape through real-world scenarios.  
Each scenario illustrates how different users leverage SpeakScape to enhance their speeches, presentations, or performances.
""")

# ---------- Light Blue Card Style ----------
card_style = """
<style>
.card {
    background-color: #f0f8ff; /* Light blue */
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    margin-bottom: 2rem;
    border: 1px solid #dbe9f4;
}
.card h4 {
    margin-top: 0;
    color: #003366;
}
</style>
"""
st.markdown(card_style, unsafe_allow_html=True)

# ---------- Cards in Columns ----------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h4>University Lecturer – Keynote Speech</h4>
        <p><strong>User Role:</strong> University Lecturer<br>
        <strong>Use Case:</strong> Preparing a keynote speech for an education summit</p>
        <ul>
            <li>Uploaded the draft script to SpeakScape</li>
            <li>Feedback showed sentence length exceeded TED averages by 25%</li>
            <li>Revised sentences and added rhetorical questions for engagement</li>
        </ul>
        <p><em>“This process helped me reframe my message to be more accessible to a wider audience.”</em></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>Student – Research Presentation</h4>
        <p><strong>User Role:</strong> University Student<br>
        <strong>Use Case:</strong> Presenting research findings at a conference</p>
        <ul>
            <li>Uploaded research presentation to SpeakScape</li>
            <li>Identified high passive voice and low rhetorical question usage</li>
            <li>Switched to active voice and added questions for clarity</li>
        </ul>
        <p><em>“The feedback helped me make my research more engaging and easier to understand for the audience.”</em></p>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="card">
        <h4>Comedian – Stand-Up Routine</h4>
        <p><strong>User Role:</strong> Stand-Up Comedian<br>
        <strong>Use Case:</strong> Preparing a stand-up routine for a comedy club</p>
        <ul>
            <li>Uploaded draft to SpeakScape</li>
            <li>Feedback flagged long sentences impacting comedic timing</li>
            <li>Shortened sentences and added punchlines for impact</li>
        </ul>
        <p><em>“The feedback helped me tighten my routine and deliver jokes more effectively.”</em></p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h4>Business Professional – Client Presentation</h4>
        <p><strong>User Role:</strong> Business Professional<br>
        <strong>Use Case:</strong> Presenting a business proposal in a client meeting</p>
        <ul>
            <li>Pasted speech directly into SpeakScape</li>
            <li>Feedback showed excessive passive voice and low rhetorical usage</li>
            <li>Refined script with active phrasing and engagement questions</li>
        </ul>
        <p><em>“The feedback helped me make my presentation more persuasive and client-focused.”</em></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle | Stock images from Unsplash")
