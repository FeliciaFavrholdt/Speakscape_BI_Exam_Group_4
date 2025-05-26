import pandas as pd
import numpy as np
import re
import textstat
import joblib

# Define columns as used in training
TRAINING_TAG_COLUMNS = [
    'tag_technology', 'tag_education', 'tag_science', 'tag_health',
    'tag_design', 'tag_business', 'tag_global_issues', 'tag_culture',
    'tag_art', 'tag_innovation'
]

# Path to the saved model and scaler
MODEL_PATH = "models/random_forest_model.pkl"
SCALER_PATH = "models/feature_scaler.pkl"

# Load model and scaler
model, training_features = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def extract_features(transcript: str, tags: list, duration: int) -> pd.DataFrame:
    # Clean transcript
    transcript_clean = transcript.strip()
    
    # Extract numeric linguistic features
    words = re.findall(r'\b\w+\b', transcript_clean)
    sentences = re.split(r'[.!?]+', transcript_clean)
    
    word_count = len(words)
    sentence_count = len([s for s in sentences if s.strip() != ''])
    avg_word_length = np.mean([len(word) for word in words]) if words else 0
    avg_sentence_length = word_count / sentence_count if sentence_count else 0
    lexical_diversity = len(set(words)) / word_count if word_count else 0
    flesch_reading_ease = textstat.flesch_reading_ease(transcript_clean)
    flesch_kincaid_grade = textstat.flesch_kincaid_grade(transcript_clean)

    numeric_data = {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "duration": duration,
        "avg_word_length": avg_word_length,
        "avg_sentence_length": avg_sentence_length,
        "lexical_diversity": lexical_diversity,
        "flesch_reading_ease": flesch_reading_ease,
        "flesch_kincaid_grade": flesch_kincaid_grade
    }

    # Prepare tag columns (initialize to 0)
    tag_data = {col: 0 for col in TRAINING_TAG_COLUMNS}
    for tag in tags:
        col_name = f"tag_{tag.lower()}"
        if col_name in tag_data:
            tag_data[col_name] = 1

    # Combine all features
    full_features = {**numeric_data, **tag_data}
    feature_df = pd.DataFrame([full_features])

    # Reorder to match training order
    feature_df = feature_df[training_features]

    return feature_df
