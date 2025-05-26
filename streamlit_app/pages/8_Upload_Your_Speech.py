import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob
from docx import Document
import PyPDF2
import os
import joblib
import re
from textstat import flesch_reading_ease, flesch_kincaid_grade

# Page config
st.set_page_config(page_title="Predict Engagement", layout="wide")
st.title("Predict Your Talk's Engagement Level")

st.markdown("""
Upload your script or paste your speech below.  
We'll analyze the text and use a machine learning model to predict the engagement level based on TED Talk benchmarks.
""")

# Upload and input
uploaded_file = st.file_uploader("Upload a .txt, .docx, or .pdf file", type=["txt", "docx", "pdf"])
manual_text = st.text_area("Or paste your speech here:")
duration = st.slider("Approximate talk duration (in seconds)", min_value=60, max_value=3600, step=60, value=600)

# Tags
available_tags = [
    "Technology", "Education", "Science", "Health",
    "Design", "Business", "Global_Issues", "Culture",
    "Art", "Innovation"
]
selected_tags = st.multiselect("Select relevant TED-style tags:", available_tags)

# Run/reset
col1, col2 = st.columns([1, 1])
run_analysis = col1.button("Run Engagement Prediction")
reset = col2.button("Clear Inputs")

if reset:
    st.session_state.clear()
    st.rerun()

# Text extract helpers
def extract_text_from_docx(file):
    try:
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    except:
        return None

def extract_text_from_pdf(file):
    try:
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    except:
        return None

# Feature extractor
def extract_features(transcript: str, tags: list, duration: int, training_features: list) -> pd.DataFrame:
    words = re.findall(r'\b\w+\b', transcript)
    sentences = re.split(r'[.!?]+', transcript)

    word_count = len(words)
    sentence_count = len([s for s in sentences if s.strip()])
    avg_word_length = np.mean([len(word) for word in words]) if words else 0
    avg_sentence_length = word_count / sentence_count if sentence_count else 0
    lexical_diversity = len(set(words)) / word_count if word_count else 0
    flesch_score = flesch_reading_ease(transcript)
    kincaid_score = flesch_kincaid_grade(transcript)

    numeric_features = {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "duration": duration,
        "avg_word_length": avg_word_length,
        "avg_sentence_length": avg_sentence_length,
        "lexical_diversity": lexical_diversity,
        "flesch_reading_ease": flesch_score,
        "flesch_kincaid_grade": kincaid_score
    }

    tag_cols = [
        'tag_technology', 'tag_education', 'tag_science', 'tag_health',
        'tag_design', 'tag_business', 'tag_global_issues', 'tag_culture',
        'tag_art', 'tag_innovation'
    ]
    tag_features = {col: 0 for col in tag_cols}
    for tag in tags:
        col_name = f"tag_{tag.lower()}"
        if col_name in tag_features:
            tag_features[col_name] = 1

    full_features = {**numeric_features, **tag_features}
    df = pd.DataFrame([full_features])
    return df[training_features]  # enforce correct order

# Text input logic
user_text = None
if uploaded_file:
    ext = uploaded_file.name.lower().split(".")[-1]
    if ext == "txt":
        user_text = uploaded_file.read().decode("utf-8")
    elif ext == "docx":
        user_text = extract_text_from_docx(uploaded_file)
    elif ext == "pdf":
        user_text = extract_text_from_pdf(uploaded_file)
elif manual_text.strip():
    user_text = manual_text.strip()

# Run prediction
if user_text and run_analysis:
    st.markdown("### Transcript Preview")
    st.text_area("Speech", user_text, height=200)

    try:
        model, training_features = joblib.load("files/random_forest_model.pkl")
        scaler = joblib.load("files/feature_scaler.pkl")
    except Exception as e:
        st.error(f"Failed to load model or scaler: {e}")
        st.stop()

    # Extract features
    feature_df = extract_features(user_text, selected_tags, duration, training_features)

    # Scale only numeric
    numeric_cols = feature_df.select_dtypes(include=["float64", "int64"]).columns
    feature_df[numeric_cols] = scaler.transform(feature_df[numeric_cols])

    # Predict
    pred = model.predict(feature_df)[0]
    proba = model.predict_proba(feature_df)[0]

    label = "High Engagement" if pred == 1 else "Low Engagement"
    confidence = round(proba[pred] * 100, 1)

    st.success(f"**Predicted: {label}** with **{confidence}% confidence**")

    st.markdown("---")
    st.markdown("### Key Metrics")
    st.metric("Word Count", feature_df['word_count'].values[0])
    st.metric("Sentence Count", feature_df['sentence_count'].values[0])
    st.metric("Average Sentence Length", round(feature_df['avg_sentence_length'].values[0], 2))
    st.metric("Flesch Reading Ease", round(feature_df['flesch_reading_ease'].values[0], 2))

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle | Stock images from Unsplash")
