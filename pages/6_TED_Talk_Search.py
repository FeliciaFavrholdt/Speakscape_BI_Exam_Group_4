import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(page_title="SpeakScape", layout="wide")

st.title("TED Talk Search Dashboard")

st.markdown("""
This page allows you to search and filter TED Talks based on various criteria such as year, tags, and more. 
You can explore the dataset to find talks that match your interests or analyze trends in public speaking.
""")

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/combined_dataset.csv")
    df['year'] = pd.to_datetime(df['recorded_date'], errors='coerce').dt.year
    df['tags'] = df['tags'].apply(lambda x: eval(x) if isinstance(x, str) and x.startswith("[") else [])
    return df

df_main = load_data()

# Sidebar filters
st.sidebar.header("Filter Data")
years = sorted(df_main['year'].dropna().unique())
tags_list = sorted({tag for tag_list in df_main['tags'] for tag in tag_list})

selected_years = st.sidebar.multiselect("Select Year(s)", years, default=years[-5:])
selected_tag = st.sidebar.selectbox("Select a Tag", ["All"] + tags_list)

# Apply filters
filtered_df = df_main[df_main['year'].isin(selected_years)]
if selected_tag != "All":
    filtered_df = filtered_df[filtered_df['tags'].apply(lambda tags: selected_tag in tags)]

st.subheader("Filtered Dataset Preview")
st.dataframe(filtered_df[['title', 'speaker', 'views', 'year', 'tags']].head(20))

# Top Tags
st.subheader("Top 20 Tags in Filtered Data")
top_tags = filtered_df['tags'].explode().value_counts().head(20)
st.bar_chart(top_tags)

# Views by Year
st.subheader("Average Views by Year (Filtered)")
views_by_year = filtered_df.groupby("year")["views"].mean()
st.line_chart(views_by_year)

# Duration Distribution
st.subheader("Talk Duration Distribution (Filtered)")
fig, ax = plt.subplots()
sns.histplot(filtered_df['duration'], bins=30, kde=True, ax=ax)
ax.set_xlabel("Duration (seconds)")
ax.set_ylabel("Number of Talks")
st.pyplot(fig)

# Views Distribution
st.subheader("Views Distribution (Log Scale, Filtered)")
fig2, ax2 = plt.subplots()
sns.histplot(filtered_df['views'], bins=50, log_scale=True, ax=ax2)
ax2.set_xlabel("Views")
ax2.set_ylabel("Frequency")
st.pyplot(fig2)

# Talks Per Year
st.subheader("Number of Talks Published Per Year (Filtered)")
talks_per_year = filtered_df['year'].value_counts().sort_index()
st.bar_chart(talks_per_year)


st.markdown("Data source: TED Talk transcripts processed and analyzed by SpeakScape.")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle | Stock images from Unsplash")