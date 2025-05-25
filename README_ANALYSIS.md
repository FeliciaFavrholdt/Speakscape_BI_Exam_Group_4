# SpeakScape 
# SpeakScape 

SpeakScape is a data-driven platform for analyzing the linguistic patterns of TED Talks and providing actionable feedback to presenters. This README provides instructions for setting up the project environment.

## Project Overview

SpeakScape analyzes TED Talk transcripts to identify linguistic patterns associated with audience engagement. The platform extracts features like sentence complexity, pronoun usage, and rhetorical devices, correlating them with engagement metrics to provide personalized feedback for presentations.

## Environment Setup with Anaconda

### 1. Create a new Conda environment

```bash
# Create a new environment with Python 3.11
conda create -n speakscape python=3.11

# Activate the environment
conda activate speakscape
```

### 2. Install the Git LFS protection hook

Run the following setup script from the root of your project.

```bash
chmod +x setup_git_lfs_protection.sh
./setup_git_lfs_protection.sh
```

This script will automatically configure .gitignore and install a pre-commit hook that prevents large or blocked files from being committed.
Once installed, Git will automatically run the hook every time you commit. You don’t need to run the hook manually — just make sure it is executable:

```bash
chmod +x .git/hooks/pre-commit
```


> If any blocked or large files are detected during `git commit`, the pre-commit hook will unstage them and cancel the commit.  
> Simply run `git commit` again to commit the remaining allowed files.


### 3. Install dependencies using requirements.txt

Once your Conda environment is activated, you can install all the required packages from the requirements.txt file:

```bash
# Install packages using pip (within your conda environment)
pip install -r requirements.txt
```

This approach combines Anaconda's robust environment management with pip's package specifications.

### 4. Install additional dependencies

Some packages require additional setup:

```bash
# Download the spaCy language model
python -m spacy download en_core_web_sm

# Register the conda environment with Jupyter
python -m ipykernel install --user --name speakscape --display-name "Python (speakscape)"
```

This last command creates a Jupyter kernel specifically for your speakscape environment, which makes it easy to select this environment directly from the Jupyter notebook interface.

## Project Directory Structure

The project follows this directory structure:

```
SpeakScape/
│
├── data/                          # Data storage directory
│   ├── raw/                       # Original, immutable data files
│   ├── interim/                   # Intermediate data files
│   └── processed/                 # Final, canonical datasets
│
├── notebooks/                     # Jupyter notebooks
│   ├── 01_data_loading_and_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── ...                        # Additional notebooks
│
├── reports/                       # Generated analysis reports
│   └── figures/                   # Generated graphics and figures
│
├── app/                           # Streamlit web application
│   ├── app.py                     # Main application entry point
│   └── ...                        # Components and pages
│
├── src/                           # Source code for use in this project
│   ├── __init__.py
│   ├── data/                      # Data processing scripts
│   ├── features/                  # Feature extraction modules
│   ├── models/                    # Machine learning modules
│   ├── ai/                        # AI integration modules
│   └── visualization/             # Visualization scripts
│
├── requirements.txt               # Package dependencies
└── README.md                      # This file
```

## Data Files

To run the notebooks, you'll need to download the TED Talk datasets and place them in the `data/raw/` directory:

- `ted_main.csv` - Main TED talk metadata (2017)
- `transcripts.csv` - Transcript data for TED talks
- `TED_2020.csv` - Complete TED 2020 dataset

## Running the Notebooks

Make sure your Conda environment is activated, then start Jupyter:

```bash
# Start Jupyter Notebook
jupyter notebook
```

Open the notebooks in the recommended sequence (starting with `01_data_loading_and_exploration.ipynb`).

## Running the Streamlit App

After processing the data and training models, you can run the Streamlit application:

```bash
# Navigate to the app directory
cd app

# Run the Streamlit app
streamlit run app.py
```

The app will be available at `http://localhost:8501`.

## Deploying the Streamlit App

Instructions for deployment will be added in a future update.

## Contributors

- Alberte 
- Felicia Favrholdt
- Fatima


## Problem Formulation

How can SpeakScape provide actionable, data-driven feedback to users by analyzing their presentation text against TED Talk benchmarks to identify impactful linguistic patterns?

### Sub-Questions
1. What specific linguistic features—such as sentence complexity, pronoun usage, and rhetorical devices—are most predictive of audience engagement in TED Talks?

2. How can we effectively correlate these linguistic features with engagement metrics (views, ratings, comments) to identify successful presentation strategies?

3. How can we establish personalized benchmarks that provide tailored feedback to users based on successful talks in similar categories?

## Context and Purpose

SpeakScape addresses a critical gap in presentation development by replacing vague, subjective feedback with accessible, personalized, and evidence-based recommendations. Traditional methods often depend on costly coaching or generalized advice that fails to account for topic-specific nuances.

### The Challenge

While various presentation feedback tools exist, most focus primarily on delivery mechanics (eye contact, gestures) or slide design rather than content structure. Those that do analyze content typically offer generic recommendations without context-specific benchmarks or data-driven insights. This leaves presenters without clear guidance on how their specific content could be improved for their particular audience and purpose.

### Our Approach

SpeakScape utilizes a large-scale dataset of TED Talk transcripts and their corresponding engagement metrics — such as views, likes, and comments — to identify the linguistic patterns associated with successful public speaking. By applying natural language processing and business intelligence techniques, we extract actionable insights that go beyond conventional presentation advice.

Users submit their presentation text to the platform, which analyzes it for linguistic structure, emotional language, and rhetorical strategies. The system then compares these elements against benchmarks derived from high-performing TED Talks in similar thematic categories (e.g., Technology, Education, Motivation). Based on statistically significant patterns, SpeakScape delivers targeted suggestions for improvement and recommends similar top-rated talks for reference.

### Beyond Text Analysis

While our initial focus is on text-based elements, we recognize that successful presentations incorporate multiple dimensions of communication. Future iterations will explore:

- Analysis of speech pacing, pauses, and emphasis patterns
- Integration with slide content analysis
- Optional audio input for tone and delivery assessment

## Research Questions

1. **Success Correlation**: Which linguistic patterns and structural elements in TED Talk transcripts are most strongly associated with high engagement (e.g., views, ratings, comments), controlling for confounding variables like speaker fame, topic popularity, and publication timing?
2. **Metric Extraction**: What key linguistic features—such as sentence complexity, pronoun usage, rhetorical devices, emotional tone, and narrative flow—can predict audience response across different presentation categories?
3. **Personalized Benchmarks**: How can machine learning methods such as clustering and classification be used to establish topic-specific benchmarks that provide tailored, actionable feedback for different presentation contexts (academic, business, educational)?

## Hypothesis

By applying natural language processing and business intelligence techniques to TED Talk transcripts and their associated engagement metrics, we can identify repeatable linguistic and structural patterns that strongly correlate with presentation success, while accounting for confounding variables.

These patterns can then inform a recommendation system that provides domain-specific, data-driven feedback, helping users improve the clarity, emotional resonance, and overall impact of their presentations across various contexts and purposes.

## 

### Differentiation from Existing Solutions

Unlike existing solutions that:

- Focus primarily on delivery mechanics rather than content (Presentation Coach, Orai)
- Provide generic writing feedback without presentation-specific insights (Grammarly, Hemingway)
- Offer subjective reviews without data-driven benchmarks (peer review platforms)

SpeakScape uniquely combines:

- Domain-specific benchmarking against successful presentations in similar categories
- Evidence-based recommendations derived from statistical analysis of audience engagement
- Contextual adaptation to different presentation purposes and settings
- Integration of linguistic analysis with rhetorical strategy assessment

## Project Annotation

SpeakScape offers a scalable, data-driven approach to presentation coaching by analyzing TED Talk transcripts to uncover linguistic and rhetorical features linked to audience engagement. By correlating these features with success indicators such as views, likes, and comments, the platform provides personalized, actionable feedback grounded in real-world data.
