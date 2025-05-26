import streamlit as st

st.set_page_config(page_title="SpeakScape", layout="wide")

st.title("SpeakScape: Notebook Summaries")

st.markdown("""
This page provides a comprehensive summary of the analytical pipeline used in the SpeakScape project. Each notebook represents a stage in processing, analyzing, and interpreting TED Talk transcripts. Below you'll find notebook-specific objectives, key findings, strategic evaluations, and links to the full notebooks on GitHub.
""")

notebooks = {
    "01 - Data Loading and Exploration": {
        "link": "https://github.com/AlberteVallentin/SpeakScape/blob/main/notebooks/01_data_loading_and_exploration.ipynb",
        "summary": """
**Objective:** Establish comprehensive understanding of TED Talk datasets and create foundation for analysis.  
**Achievements:** Characterized 3 datasets (TED_main 2017: 2,550 talks, transcripts: 2,467, TED_2020: 4,609 talks). Identified missing transcripts, column inconsistencies, and data quality issues. Established view count distributions and tag analysis with 403 common tags. Discovered 1,660 overlapping talks requiring deduplication.  
**Strategic Value:** High – provided essential foundation for all subsequent work and established data quality standards.
"""
    },
    "02 - Data Cleaning and Standardization": {
        "link": "https://github.com/AlberteVallentin/SpeakScape/blob/main/notebooks/02_data_cleaning.ipynb",
        "summary": """
**Objective:** Transform raw datasets into clean, analysis-ready data while preserving valuable information.  
**Achievements:** Extracted 45,000+ audience reactions while cleaning transcripts. Standardized URL formats for reliable duplicate detection. Converted Unix timestamps and ensured consistent numeric types. Removed talks with missing or short transcripts. Recovered 43% of missing transcripts in TED_2017.  
**Strategic Value:** High – created clean, reliable datasets essential for subsequent analysis with innovative audience reaction extraction.
"""
    },
    "03 - Dataset Integration and Normalization": {
        "link": "https://github.com/AlberteVallentin/SpeakScape/blob/main/notebooks/03_dataset_integration.ipynb",
        "summary": """
**Objective:** Merge datasets into unified, normalized dataset with intelligent duplicate handling.  
**Achievements:** Identified 2,434 overlapping talks and merged. Reduced 460 unique raw tags to 456 normalized tags. Created dataset of 4,095 unique talks with 100% data completeness.  
**Strategic Value:** High – created the largest clean TED Talk dataset with novel features, enabling subsequent analysis.
"""
    },
    "04 - Exploratory Analysis": {
        "link": "https://github.com/AlberteVallentin/SpeakScape/blob/main/notebooks/04_exploratory_analysis.ipynb",
        "summary": """
**Objective:** Conduct comprehensive analysis to understand content patterns, engagement drivers, and temporal trends.  
**Achievements:** Identified optimal talk length (12–18 mins). Analyzed shifting topic trends, created tag co-occurrence networks, and observed seasonal patterns.  
**Strategic Value:** Medium – offers useful descriptive insights but limited direct impact on actionability.
"""
    },
    "05 - Feature Extraction": {
        "link": "https://github.com/AlberteVallentin/SpeakScape/blob/main/notebooks/05_feature_extraction.ipynb",
        "summary": """
**Objective:** Extract basic features from TED Talk transcripts to create structured feature matrix.  
**Achievements:** Created feature matrix with 66 features across structure, readability, and speech rate.  
**Strategic Value:** Medium – good foundation for modeling; correlations with success were weak.
"""
    },
    "06 - Advanced Metrics Extraction": {
        "link": "https://github.com/AlberteVallentin/SpeakScape/blob/main/notebooks/06_metric_extraction.ipynb",
        "summary": """
**Objective:** Calculate presentation-specific metrics including concreteness, emotional tone, and narrative structure.  
**Achievements:** Extracted 29 advanced metrics. Identified patterns in concreteness (mean=3.14) and emotional engagement (mean intensity=0.548).  
**Strategic Value:** Medium – novel metrics added depth, but real-world impact on presentation improvement is unclear.
"""
    },
    "07 - Sentence Structure Analysis": {
        "link": "https://github.com/AlberteVallentin/SpeakScape/blob/main/notebooks/07_sentence_structure_analysis.ipynb",
        "summary": """
**Objective:** Analyze sentence-level patterns and rhetorical structures across TED Talks.  
**Achievements:** Computed sentence metrics (e.g., 17.27 avg words/sentence, 10.97% passive voice). Mild correlations found with engagement.  
**Strategic Value:** Low to Medium – insightful but offers limited practical application.
"""
    },
    "08 - Linguistic Feature Analysis": {
        "link": "https://github.com/AlberteVallentin/SpeakScape/blob/main/notebooks/08_linguistic_feature_analysis.ipynb",
        "summary": """
**Objective:** Extract comprehensive linguistic features to test correlation with presentation success.  
**Achievements:** 29 features extracted across 5 categories. Found differences between high/low engagement talks (e.g., 31.5% more rhetorical questions in successful talks).  
**Limitations:** All correlations r < 0.15; text-only approach misses delivery/contextual cues.  
**Strategic Value:** Low for practice, high for proving limits of linguistic feature analysis.
"""
    },
    "09 - Engagement Correlation Analysis": {
        "link": "https://github.com/AlberteVallentin/SpeakScape/blob/main/notebooks/09_engagement_correlation_analysis.ipynb",
        "summary": """
**Objective:** Quantify relationships between linguistic features and engagement to create predictive models.  
**Achievements:** Built models (R² = -0.013) and found optimal ranges for content length/readability.  
**Limitations:** Weak correlations (r = 0.10–0.14), worse-than-average predictions, linguistic style plays minor role.  
**Strategic Value:** Minimal – confirms that predicting engagement via text alone is ineffective.
"""
    }
}

for title, info in notebooks.items():
    st.markdown(f"### {title}")
    st.markdown(f"[📘 View Notebook]({info['link']})")
    st.markdown(info['summary'])

st.markdown("---")
st.markdown("### Overall Assessment")
st.markdown("""
- **Technical Success:** Built a reliable pipeline and extracted robust linguistic features.
- **Research Insight:** Demonstrated that text-only analysis has limited power for predicting talk success.
- **Key Contribution:** Strong negative result that helps redirect future research and practice away from ineffective approaches.
- **Practical Advice:** Prioritize speaker skills, content quality, and audience understanding over linguistic optimization.
""")

st.markdown("### Datasets")
st.markdown("- [TED Talks 2017 Dataset (Kaggle)](https://www.kaggle.com/datasets/rounakbanik/ted-talks/data)")
st.markdown("- [TED Talks 2020 Dataset (Kaggle)](https://www.kaggle.com/datasets/thegupta/ted-talk/data)")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle | Source code on GitHub: [SpeakScape](https://github.com/AlberteVallentin/SpeakScape)")
