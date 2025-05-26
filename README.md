# SpeakScape
SpeakScape is a data-driven platform for analyzing the linguistic patterns of TED Talks and providing actionable feedback to presenters. This README provides instructions for setting up the project environment and understanding the core components of the analysis.

---

## Contributors
**Group 4, l25dat4bi1f**  
Business Intelligence 2025  
Copenhagen Business Academy, Lyngby  

GitHub Repository: [Speakscape_BI_Exam_Group_4](https://github.com/FeliciaFavrholdt/Speakscape_BI_Exam_Group_4/tree/main)

### Felicia Favrholdt
- Email: [cph-ff62@cphbusiness.dk](mailto:cph-ff62@cphbusiness.dk)  
- GitHub: [https://github.com/FeliciaFavrholdt](https://github.com/FeliciaFavrholdt)

### Alberte Mary Vallentin
- Email: [cph-av169@cphbusiness.dk](mailto:cph-av169@cphbusiness.dk)  
- GitHub: [https://github.com/AlberteVallentin](https://github.com/AlberteVallentin)

### Fatima Majid Shamcizadh
- Email: [cph-fs156@cphbusiness.dk](mailto:cph-fs156@cphbusiness.dk)  
- GitHub: [https://github.com/Fati01600](https://github.com/Fati01600)

---

## Streamlit App - Run Locally

1. **Install Python**  
   Download and install Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Clone the Repository**
   ```bash
   git clone git@github.com:FeliciaFavrholdt/Speakscape_BI_Exam_Group_4.git
   cd streamlit_app
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the App**
   ```bash
   streamlit run SPEAKSCAPE.py
   ```

---

## Objective
To develop an intelligent feedback system that evaluates the linguistic quality and engagement potential of user-submitted presentation transcripts by comparing them against successful TED Talks.

---

## Problem Statement
**How can SpeakScape provide actionable, data-driven feedback to users by analyzing their presentation text against TED Talk benchmarks to identify impactful linguistic patterns?**

---

## Dataset
This project is based on two TED Talk datasets from Kaggle: TED_2017 and TED_2020.  
A combined, cleaned dataset was curated and used for final analysis:  
[combined_dataset.csv](https://github.com/AlberteVallentin/SpeakScape/blob/url2/data/processed/combined_dataset.csv)

Key attributes retained:
- `title`, `transcript`, `description`, `speaker`, `tags`, `views`, `recorded_date`, `event`, `duration`

---

## Tasks Completed
- Data collection, cleaning, and schema alignment
- Exploratory data analysis (EDA) on linguistic and engagement metrics
- Feature engineering with NLP techniques
- Supervised ML modeling to predict talk engagement (views)
- Developed a Streamlit app to allow users to upload transcripts and receive analysis

---

## Technologies Used
- Python (Jupyter Notebook, Streamlit)
- Data manipulation: Pandas, NumPy
- NLP: NLTK, TextBlob
- Visualization: Matplotlib, Seaborn
- Machine Learning: Scikit-learn
- Deployment: Streamlit

---

## Directory Structure
```
Speakscape_BI_Exam_Group_4/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── combined_dataset.csv
│
├── notebooks/
│   └── Analysis.ipynb
│
├── streamlit_app/
│   ├── SPEAKSCAPE.py
│   └── requirements.txt
│
├── outputs/
│   ├── models/
│   └── visualizations/
│
├── README.md
└── notes.md
```

---

## Project Summary
SpeakScape provides data-driven insights into the linguistic effectiveness of presentation transcripts. By analyzing TED Talks, the platform identifies patterns that contribute to audience engagement and applies machine learning models to score and give actionable feedback to new presentation texts.

---

## Key Findings
- Talks with higher engagement tend to:
  - Be between 10–18 minutes long
  - Use simpler, readable language (Flesch-Kincaid readability)
  - Convey positive and assertive sentiment
  - Include narrative elements and rhetorical questions

- NLP-derived features such as sentiment polarity and sentence complexity significantly correlate with viewership statistics.

---

## Project Analysis and Reflections
- **Strengths**: Integrated NLP and ML to derive actionable feedback from real-world data; created a user-friendly interface via Streamlit.
- **Challenges**: Balancing feature richness with model interpretability and cleaning inconsistent TED metadata.
- **Future Work**:
  - Integrate speech-to-text for live presentation uploads
  - Add multilingual support
  - Provide personalized feedback based on speaker profile

---
