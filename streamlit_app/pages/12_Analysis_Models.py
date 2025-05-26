import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Visualizations", layout="wide")
st.title("SpeakScape Visualizations")


plot_dir = Path("../SpeakScape_Analysis/plots")  

# Define plot filenames and their descriptions
plots = [
    {
        "file": "missing_values.png",
        "title": "Missing Values Heatmap",
        "desc": "Visualizes missing values across features to assess data completeness and cleaning needs."
    },
    {
        "file": "data_completeness_heatmap.png",
        "title": "Data Completeness Heatmap",
        "desc": "Shows the completeness across TED datasets after preprocessing."
    },
    {
        "file": "feature_correlation_views.png",
        "title": "Feature Correlation with Views",
        "desc": "Highlights how different features (like word count, duration) correlate with engagement (views)."
    },
    {
        "file": "linguistic_feature_distributions.png",
        "title": "Linguistic Feature Distributions",
        "desc": "Distributions of linguistic metrics such as readability, word complexity, etc."
    },
    {
        "file": "rf_feature_importances.png",
        "title": "Random Forest Feature Importances",
        "desc": "Which features contributed most to predicting views using a Random Forest model."
    },
    {
        "file": "model_comparison_barplot.png",
        "title": "Model Comparison",
        "desc": "Evaluation of different regression models based on R² and RMSE."
    },
    {
        "file": "regression_actual_vs_predicted.png",
        "title": "Regression Predictions vs Actual",
        "desc": "Scatterplot comparing model predictions with actual view counts."
    },
    {
        "file": "logreg_confusion_matrix.png",
        "title": "Logistic Regression Confusion Matrix",
        "desc": "Performance of logistic regression for classifying high vs low engagement."
    },
    {
        "file": "readability_by_event_barplot.png",
        "title": "Readability by Event",
        "desc": "Barplot showing how presentation readability varies by event."
    }
]

# Display all plots
for plot in plots:
    st.subheader(plot["title"])
    st.markdown(plot["desc"])
    
    img_path = plot_dir / plot["file"]
    
    if img_path.exists():
        image = Image.open(img_path)
        st.image(image, use_column_width=True)
    else:
        st.warning(f"Image not found: {img_path}")

    st.markdown("---")
