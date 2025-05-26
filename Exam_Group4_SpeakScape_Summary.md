SpeakScape – Project Analysis Summary
Project Title
SpeakScape – Enhancing Presentation Skills with Data-Driven Feedback

Team Members
Group 4 (l25dat4bi1f):

Alberte Mary Wahlstrøm Vallentin

Felicia Favrholdt

Fatima Majid Shamcizadh

Problem Statement
How can SpeakScape provide actionable, data-driven feedback to users by analyzing their presentation text against TED Talk benchmarks to identify impactful linguistic patterns?

Project Objective
The project aims to develop an intelligent tool that evaluates user-uploaded presentation transcripts by comparing them to TED Talks. The focus is on extracting linguistic insights and offering feedback that enhances clarity, engagement, and communication quality.

Methodology Overview
1. Data Preparation
Sources Used: TED Talk transcripts from TED_2017 and TED_2020 datasets.

Cleaning Strategy: Removed:

Irrelevant metadata (e.g., media URLs)

Noisy or incomplete entries

Redundant fields

Final Dataset: Cleaned and unified schema with the following essential columns:

title, transcript, description, speaker, tags, views, recorded_date, event, duration

2. Exploratory Data Analysis (EDA)
Examined linguistic features and correlations with engagement (views).

Visualized patterns such as:

Word count vs. views

Topic tags vs. average viewership

Temporal trends in popular talks

3. Feature Engineering
Extracted NLP-based features:

Word count

Readability scores (e.g., Flesch-Kincaid)

Sentiment polarity

Use of rhetorical devices (e.g., metaphors, repetition)

4. Predictive Modeling
Target: Engagement score (views) as a proxy for presentation effectiveness.

Models Tested:

Linear Regression

Random Forest

Support Vector Regression

Evaluation Metrics:

R² Score

Mean Absolute Error (MAE)

Cross-validation results

5. Streamlit Application
Purpose: Make feedback accessible to non-technical users.

Features:

Transcript upload

Engagement prediction

Key linguistic metrics dashboard

Visual comparison to TED Talk benchmarks

Key Insights
Engaging talks often have:

Moderate duration (~10–18 minutes)

High readability

Positive and assertive tone

Talks using storytelling and strong openings show higher view counts.

Clear linguistic markers correlate with success, validating the NLP approach.

Outcomes
A working prototype of a feedback system that:

Accepts user transcripts

Evaluates and scores linguistic quality

Predicts potential engagement

Suggests improvements using TED Talk data

Conclusions
SpeakScape effectively demonstrates how BI and AI can be combined to assist users in improving public speaking. By comparing transcripts with successful TED Talks, the tool empowers users to receive feedback grounded in real-world data patterns.

Future Work
Expand to video/audio input with speech-to-text

Refine models with more engagement indicators (likes, shares)

Personalized speaker profiles with tailored suggestions

Language support beyond English

