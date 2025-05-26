# SpeakScape – Project Analysis Summary

## Project Title
**SpeakScape** – Enhancing Presentation Skills with Data-Driven Feedback

## Team Members
**Group 4 (l25dat4bi1f):**
- Alberte Mary Wahlstrøm Vallentin  
- Felicia Favrholdt  
- Fatima Majid Shamcizadh  

---

## Problem Statement
**How can SpeakScape provide actionable, data-driven feedback to users by analyzing their presentation text against TED Talk benchmarks to identify impactful linguistic patterns?**

---

## Project Objective
The objective of the project is to develop an intelligent tool that evaluates user-uploaded presentation transcripts by comparing them with successful TED Talks. The focus is on uncovering linguistic insights and providing constructive, data-driven feedback to enhance clarity, engagement, and communication effectiveness.

---

## Methodology Overview

### 1. Data Preparation
- **Sources**: TED_2017 and TED_2020 transcript datasets.
- **Cleaning Strategy**:
  - Removed metadata and URLs irrelevant to textual analysis.
  - Dropped incomplete and noisy records.
  - Unified schemas between datasets.
- **Final Dataset Includes**:
  - `title`, `transcript`, `description`, `speaker`, `tags`, `views`, `recorded_date`, `event`, `duration`

### 2. Exploratory Data Analysis (EDA)
- Explored relationships between linguistic features and viewership.
- Created visualizations:
  - Word count vs. views
  - Popular tags vs. average views
  - Temporal changes in engagement trends

### 3. Feature Engineering
- NLP-based feature extraction:
  - Word count
  - Readability scores (e.g., Flesch-Kincaid)
  - Sentiment polarity
  - Detection of rhetorical patterns

### 4. Predictive Modeling
- **Goal**: Predict engagement (views) as a proxy for effectiveness.
- **Models Applied**:
  - Linear Regression
  - Random Forest Regressor
  - Support Vector Regression
- **Performance Metrics**:
  - R² Score
  - Mean Absolute Error (MAE)
  - Cross-validation for robustness

### 5. Streamlit Application
- **Purpose**: Deliver results via a user-friendly interface.
- **Features**:
  - Transcript upload and feedback generation
  - Visual metrics dashboard
  - Engagement prediction
  - Benchmarking against TED Talks

---

## Key Insights
- Successful presentations typically:
  - Fall within a 10–18 minute range
  - Maintain a high readability level
  - Use a confident and positive tone
  - Feature storytelling and strong openings

- Linguistic signals strongly correlate with engagement levels, supporting the data-driven approach.

---

## Outcomes
- Created a functional BI solution for automated presentation feedback.
- Users can receive real-time insights on how to improve their communication.
- The application uses real-world TED Talk data to suggest enhancements.

---

## Conclusions
SpeakScape demonstrates how Business Intelligence and Natural Language Processing can be applied to help users improve public speaking. The feedback system is grounded in TED Talk benchmarks and offers accessible, insightful analysis for non-technical users.

---

## Future Work
- Extend functionality to audio/video input with transcription.
- Use additional engagement metrics like likes, comments, and shares.
- Provide user-specific feedback profiles.
- Add multi-language support for non-English presentations.

---
