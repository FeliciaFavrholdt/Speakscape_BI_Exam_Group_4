# SpeakScape

SpeakScape is a data-driven platform that analyzes the linguistic patterns of TED Talks to provide actionable feedback to presenters. By applying Natural Language Processing (NLP) and Machine Learning (ML), the project correlates language features with audience engagement metrics—helping users improve the effectiveness of their presentation content.

---

## Contributors

- **Felicia Favrholdt**  
  [GitHub](https://github.com/FeliciaFavrholdt) | [Email](mailto:cph-ff62@cphbusiness.dk)

- **Alberte Mary Vallentin**  
  [GitHub](https://github.com/AlberteVallentin) | [Email](mailto:cph-av169@cphbusiness.dk)

- **Fatima Majid Shamcizadh**  
  [GitHub](https://github.com/Fati01600) | [Email](mailto:cph-fs156@cphbusiness.dk)

---

## Project Overview

SpeakScape analyzes TED Talk transcripts to extract linguistic and stylistic features such as rhetorical devices, sentence complexity, and pronoun use. These features are linked to engagement metrics like view counts to predict and enhance the effectiveness of presentations. The project results in a user-facing Streamlit application that provides personalized, actionable feedback based on user-submitted transcripts.

---

## Problem Statement

**How can SpeakScape provide actionable, data-driven feedback to users by analyzing their presentation text against TED Talk benchmarks to identify impactful linguistic patterns?**

---

## Motivation

Public speaking is a critical skill in both professional and academic settings. TED Talks are widely recognized for their quality and audience impact. Our goal was to develop a tool that helps presenters improve their communication skills by learning from high-engagement linguistic patterns found in TED Talks.

---

## Theoretical Foundation

Our approach is grounded in:

- **NLP**: SpaCy and NLTK for extracting syntactic and semantic features, including rhetorical devices.
- **Statistical Modeling**: Scikit-learn for regression and classification models.
- **Linguistic Theory**: Concepts such as ethos/pathos/logos and rhetorical structure.
- **Engagement Metrics**: View counts, tags, and duration used as labels or proxies for measuring presentation success.

---

## Argumentation of Choices

All design choices are detailed in [`notes.md`](notes.md), including:

- Merging TED_2017 and TED_2020 datasets for broader training data.
- Retaining only linguistically relevant and well-populated fields (`transcript`, `description`, `views`, etc.).
- Dropping noisy or incomplete data to improve model accuracy and reduce overfitting.
- Mapping and cleaning operations to ensure consistent schema and quality.

---

## Design

### Key System Components:

1. **Data Collection & Cleaning**  
   Unified and filtered TED datasets for transcript completeness and consistency.

2. **Feature Extraction (NLP)**  
   Analysis of rhetorical device use, pronoun frequency, sentence length, and syntactic variation.

3. **Machine Learning Modeling**  
   Predictive models to estimate engagement metrics based on linguistic features.

4. **Streamlit Application**  
   User interface that accepts presentation transcripts and provides structured feedback.

### Project Directory Structure:
```text
├── combined_dataset.csv
├── SpeakScape_Analysis/
│   ├── Analysis.ipynb
│   └── modeling_notebooks/
├── streamlit_app/
│   └── SPEAKSCAPE.py
├── artefacts/
│   ├── cleaned_data/
│   ├── plots/
│   └── models/
├── notes.md
├── Exam_Group4_SpeakScape_Summary.md
├── requirements.txt
└── README.md

## Research Questions

- What linguistic features are most strongly associated with high audience engagement?
- Can we predict the success of a presentation using only textual features?
- How can we provide interpretable, constructive feedback on speech writing?

---

## Hypothesis

Talks that include rhetorical diversity, moderate sentence complexity, and emotional appeal are likely to achieve higher engagement scores—such as more views or favorable tags.

---

## Outcomes

- A cleaned, combined dataset of TED Talks with engineered NLP features.
- Machine learning models to predict engagement based on textual attributes.
- A fully functional Streamlit app that provides users with real-time feedback on their presentation content.

---

## Future Work

- Extend the platform to include multimodal analysis (voice, video).
- Provide dynamic, personalized suggestions based on user proficiency.
- Improve model precision using more granular engagement metrics (e.g., likes, watch time, audience retention).

---

## Implementation Instructions

### 1. Clone the Repository

git clone https://github.com/FeliciaFavrholdt/Speakscape_BI_Exam_Group_4.git
cd Speakscape_BI_Exam_Group_4

2. Install Dependencies

pip install -r requirements.txt
3. Run the Analysis Notebook

cd SpeakScape_Analysis
jupyter notebook
Then open and execute Analysis.ipynb or other modeling notebooks to review data preparation and model training.

4. Launch the Streamlit App

cd ../streamlit_app
streamlit run SPEAKSCAPE.py
vbnet


Let me know if you also want a section on troubleshooting common errors or instructions for deploying the app online (e.g., using Streamlit Cloud or Heroku).