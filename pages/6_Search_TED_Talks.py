import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ---------------- Page Setup ----------------
st.set_page_config(page_title="SpeakScape TED Talk Dashboard", layout="wide")
st.title("TED Talk Dashboard")

st.markdown("""
Explore TED Talks by year, speaker, duration, tags, and keywords.  
This dashboard includes trend detection, tag content search, and K-Means clustering with adjustable cluster count.
""")

# ---------------- Load and Cache Data ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/combined_dataset.csv")
    df['year'] = pd.to_datetime(df['recorded_date'], errors='coerce').dt.year
    df['tags'] = df['tags'].apply(lambda x: eval(x) if isinstance(x, str) and x.startswith("[") else [])
    return df

df_main = load_data()

# ---------------- Sidebar Filters ----------------
st.sidebar.header("Filter TED Talks")

# Clear filters
if st.sidebar.button("🔁 Clear All Filters"):
    st.session_state.clear()

years = sorted(df_main['year'].dropna().unique())
tags_list = sorted({tag for tag_list in df_main['tags'] for tag in tag_list})
speakers = sorted(df_main['speaker'].dropna().unique())
min_duration, max_duration = int(df_main['duration'].min()), int(df_main['duration'].max())

selected_years = st.sidebar.multiselect("Select Year(s)", years, key="year_filter")
selected_tag = st.sidebar.selectbox("Select a Tag", ["All"] + tags_list, key="tag_filter")
tag_search = st.sidebar.text_input("Search Tags by Keyword", key="tag_search")
selected_speakers = st.sidebar.multiselect("Select Speaker(s)", speakers, key="speaker_filter")
duration_range = st.sidebar.slider("Select Duration Range (seconds)", min_duration, max_duration, (min_duration, max_duration), key="duration_filter")
keyword = st.sidebar.text_input("Search Title Keywords", key="keyword_filter")
num_clusters = st.sidebar.slider("K-Means: Number of Clusters", 2, 10, 3)

# ---------------- Apply Filters ----------------
filtered_df = df_main.copy()

if selected_years:
    filtered_df = filtered_df[filtered_df['year'].isin(selected_years)]

if selected_tag != "All":
    filtered_df = filtered_df[filtered_df['tags'].apply(lambda tags: selected_tag in tags)]

if tag_search:
    filtered_df = filtered_df[filtered_df['tags'].apply(lambda tags: any(tag_search.lower() in tag.lower() for tag in tags))]

if selected_speakers:
    filtered_df = filtered_df[filtered_df['speaker'].isin(selected_speakers)]

if keyword:
    filtered_df = filtered_df[filtered_df['title'].str.contains(keyword, case=False, na=False)]

filtered_df = filtered_df[filtered_df['duration'].between(*duration_range)]

# ---------------- Display Filtered Data ----------------
st.subheader("Filtered Dataset Preview")
st.dataframe(filtered_df[['title', 'speaker', 'views', 'year', 'duration', 'tags']].head(20))

# ---------------- Download Filtered Data ----------------
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_ted_talks.csv",
    mime="text/csv"
)

if not filtered_df.empty:
    # Top Tags
    st.subheader("Top 20 Tags in Filtered Data")
    top_tags = filtered_df['tags'].explode().value_counts().head(20)
    st.bar_chart(top_tags)

    # Views trend
    st.subheader("Average Views by Year (Trend Detection)")
    trend = filtered_df.groupby("year")["views"].mean().reset_index()
    fig_trend = px.line(trend, x="year", y="views", markers=True, title="Trend: Average Views Over Time")
    st.plotly_chart(fig_trend, use_container_width=True)

    # Duration distribution
    st.subheader("Talk Duration Distribution")
    fig1, ax1 = plt.subplots()
    sns.histplot(filtered_df['duration'], bins=30, kde=True, ax=ax1)
    ax1.set_xlabel("Duration (seconds)")
    ax1.set_ylabel("Number of Talks")
    st.pyplot(fig1)

    # Views distribution
    st.subheader("Views Distribution (Log Scale)")
    fig2, ax2 = plt.subplots()
    sns.histplot(filtered_df['views'], bins=50, log_scale=True, ax=ax2)
    ax2.set_xlabel("Views")
    ax2.set_ylabel("Frequency")
    st.pyplot(fig2)

    # Talks per year
    st.subheader("Number of Talks Per Year")
    talks_per_year = filtered_df['year'].value_counts().sort_index()
    st.bar_chart(talks_per_year)

    # 2D scatter plot
    st.subheader("Scatter Plot: Views vs Duration")
    fig_scatter = px.scatter(
        filtered_df,
        x='duration',
        y='views',
        color='year',
        hover_data=['title', 'speaker'],
        title="Views vs Duration Colored by Year"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    # K-Means Clustering
    st.subheader(f"K-Means Clustering: Views vs Duration ({num_clusters} Clusters)")
    clustering_data = filtered_df[['views', 'duration']].dropna()
    scaler = StandardScaler()
    clustering_scaled = scaler.fit_transform(clustering_data)

    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    clustering_data['cluster'] = kmeans.fit_predict(clustering_scaled)

    fig_cluster = px.scatter(
        clustering_data,
        x='duration',
        y='views',
        color='cluster',
        title="K-Means Clustering",
        labels={"cluster": "Cluster"},
        opacity=0.7
    )
    st.plotly_chart(fig_cluster, use_container_width=True)

else:
    st.warning("No results match your filters. Try adjusting the filters above.")

# ---------------- Footer ----------------
st.markdown("Data source: TED Talk transcripts processed and analyzed by SpeakScape.")
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle | Stock images from Unsplash")
