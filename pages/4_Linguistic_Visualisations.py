import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="SpeakScape", layout="wide")

st.title("TED Talk Linguistic Benchmarking")
st.markdown("""
Explore how key linguistic metrics such as sentence length, passive voice usage, rhetorical questions, 
and imperative phrasing vary across TED Talks over time. Use filters to refine your analysis.
""")

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/sentence_metrics.csv")

    # Extract year from URL if missing
    if "year" not in df.columns:
        if "url" in df.columns:
            df["year"] = df["url"].str.extract(r'(\d{4})')[0].astype(float)
        elif "recorded_date" in df.columns:
            df["year"] = pd.to_datetime(df["recorded_date"], errors='coerce').dt.year
        else:
            df["year"] = pd.NA

    # Parse tags
    if "tags" in df.columns:
        df["tags"] = df["tags"].apply(
            lambda x: eval(x) if isinstance(x, str) and x.startswith("[") else [])
    else:
        df["tags"] = [[] for _ in range(len(df))]

    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filter TED Talks")
available_years = sorted(df["year"].dropna().unique())
available_tags = sorted({tag for tags in df["tags"] for tag in tags})

selected_years = st.sidebar.multiselect("Select Year(s)", available_years, default=available_years[-5:])
selected_tag = st.sidebar.selectbox("Select a Tag", ["All"] + available_tags)

# Apply Filters
filtered_df = df[df["year"].isin(selected_years)]
if selected_tag != "All":
    filtered_df = filtered_df[filtered_df["tags"].apply(lambda tags: selected_tag in tags)]

# Debug info
st.write("Filtered rows:", len(filtered_df))
st.write("Years available:", filtered_df["year"].dropna().unique())

# Validate year
if "year" not in filtered_df.columns or filtered_df["year"].dropna().empty:
    st.error("No valid 'year' data available for the selected filters.")
    st.stop()

# Plotting function
def plot_metric_over_time(df, column, ylabel):
    st.subheader(ylabel)
    data = df.groupby("year")[column].mean().reset_index()
    fig, ax = plt.subplots()
    sns.lineplot(data=data, x="year", y=column, marker="o", ax=ax)
    ax.set_ylabel(ylabel)
    ax.set_xlabel("Year")
    ax.grid(True)
    st.pyplot(fig)

# Plots
plot_metric_over_time(filtered_df, "avg_sentence_length", "Average Sentence Length (words)")
plot_metric_over_time(filtered_df, "passive_voice_percentage", "Passive Voice Usage (%)")
plot_metric_over_time(filtered_df, "rhetorical_question_count", "Rhetorical Questions per Talk")

if "imperative_percentage" in filtered_df.columns:
    plot_metric_over_time(filtered_df, "imperative_percentage", "Imperative Usage (%)")

st.markdown("Data source: TED Talk transcripts processed and analyzed by SpeakScape.")


st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle")
