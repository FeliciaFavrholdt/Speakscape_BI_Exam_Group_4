# SpeakScape Analysis Summary

## 1. Problem Understanding and Setup
- Project goal: provide data-driven, linguistically grounded feedback to speakers.
- Hypothesis: impactful linguistic patterns in TED Talks can predict audience engagement.
- Dataset: combined TED_2017 and TED_2020 transcripts and metadata.
- Setup: aligned schemas, prepared Python-based data pipelines in Jupyter Notebooks.

---

## 2. Data Cleaning and Overview
- Dropped non-relevant, noisy, or incomplete columns.
- Removed records with missing or very short transcripts.
- Retained: 2,453 talks (TED_2017) and 4,076 talks (TED_2020).
- Standardized column names across datasets for consistency.

---

## 3. Data Loading and Preprocessing
- Consolidated datasets into one structured DataFrame.
- Applied NLP preprocessing: lowercasing, stopword removal, lemmatization.
- Transformed `views` with log normalization to reduce skew.
- Encoded `tags` with multi-hot encoding.
- Converted `recorded_date` into datetime for temporal analysis.

---

## 4. Exploratory Data Analysis (EDA)
- High engagement topics: "inspiration", "psychology", "technology".
- Optimal talk durations: 10–18 minutes.
- Positive correlation between lexical richness and view counts.
- Visualized trends using `matplotlib` and `seaborn`.

---

## 5. Feature Engineering and Model Training
- Engineered features: `word_count`, `sentence_count`, `lexical_diversity`, sentiment scores (VADER).
- Trained models: Linear Regression, Ridge Regression, Random Forest Regressor.
- Best performing model: Random Forest with highest R² in cross-validation.

---

## 6. Predictive Model Development
- Built XGBoost Regressor for enhanced prediction performance.
- Tuned hyperparameters via GridSearchCV: tree depth, learning rate, estimators.
- Achieved final test R² score ~0.72.
- Developed classification model for engagement tiers: low, medium, high.

---

## 7. Model Explainability and Insights
- Used SHAP for interpretability of predictions.
- Top features: `word_count`, sentiment polarity, tags like "inspiration", "courage".
- Confirmed importance of linguistic and emotional factors in engagement.
- Results inform feedback generation for presentation improvement.

---
