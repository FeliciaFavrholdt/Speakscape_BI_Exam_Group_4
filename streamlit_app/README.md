# SpeakScape

SpeakScape is a data-driven platform that analyzes linguistic patterns in TED Talks to provide presenters with actionable feedback. By leveraging Natural Language Processing (NLP) and Machine Learning (ML), we compare user presentation transcripts against TED Talk benchmarks to identify impactful communication strategies.

## Contributors

- **Felicia Favrholdt** – [GitHub](https://github.com/FeliciaFavrholdt), [cph-ff62@cphbusiness.dk](mailto:cph-ff62@cphbusiness.dk)
- **Alberte Mary Vallentin** – [GitHub](https://github.com/AlberteVallentin), [cph-av169@cphbusiness.dk](mailto:cph-av169@cphbusiness.dk)
- **Fatima Majid Shamcizadh** – [GitHub](https://github.com/Fati01600), [cph-fs156@cphbusiness.dk](mailto:cph-fs156@cphbusiness.dk)

---

## Project Overview

SpeakScape analyzes TED Talk transcripts to extract linguistic and stylistic features, such as rhetorical devices, sentence complexity, and pronoun usage. These are then correlated with engagement metrics (like views) to predict and improve the impact of new presentations.

---

## Problem Statement

**How can SpeakScape provide actionable, data-driven feedback to users by analyzing their presentation text against TED Talk benchmarks to identify impactful linguistic patterns?**

---

## Motivation

Effective communication is critical in professional and academic settings. TED Talks are exemplary models of engaging presentations. By analyzing them, we aim to:
- Help users understand and improve their linguistic presentation style.
- Bridge the gap between subjective speech feedback and measurable language features.

---

## Theoretical Foundation

This project is grounded in:
- **Natural Language Processing (NLP)**: Tokenization, POS tagging, named entity recognition.
- **Linguistic Theory**: Use of ethos/pathos/logos, rhetorical devices.
- **Statistical Modeling**: Regression and classification models predicting engagement based on linguistic patterns.
- **Machine Learning**: Supervised learning to correlate features with views and identify impactful patterns.

---

## Argumentation of Choices

- Dropped columns: media links, nested metadata, irrelevant tags (see [notes.md](notes.md))
- Selected features: `transcript`, `description`, `tags`, `views`—aligned with goals
- Tools: SpaCy/NLTK for NLP, scikit-learn for modeling, Streamlit for UI
- Dataset cleaning: Ensured only complete, long-enough transcripts were retained

---

## Design

### System Pipeline:
1. **Data Cleaning & Merging** – TED 2017 and 2020 datasets unified, irrelevant fields removed.
2. **Feature Extraction** – NLP used to extract syntax, semantics, sentiment, rhetorical style.
3. **Modeling** – Trained ML models to predict engagement (views).
4. **Streamlit Interface** – Interactive feedback tool with NLP stats and model output.

```text
├── combined_dataset.csv
├── Analysis.ipynb
├── speakscape_appw/
│   └── SPEAKSCAPE.py
├── artefacts/
│   ├── plots/
│   └── models/
└── notes.md
