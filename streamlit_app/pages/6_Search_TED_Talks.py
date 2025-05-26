import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib

# ---------------- Page Setup ----------------
st.set_page_config(page_title="SpeakScape TED Talk Dashboard", layout="wide")
st.title("TED Talk Dashboard")

st.markdown("""
Explore TED Talks by year, speaker, duration, tags, and keywords.  
This dashboard includes trend detection, tag content search, K-Means clustering, and predictive view modeling.
""")

# ---------------- Load and Cache Data ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/combined_dataset.csv")
    df['year'] = pd.to_datetime(df['recorded_date'], errors='coerce').dt.year
    df['tags'] = df['tags'].apply(lambda x: eval(x) if isinstance(x, str) and x.startswith("[") else [])
    return df

@st.cache_resource
def load_model():
    try:
        return joblib.load("random_forest_model.pkl")  # saved as a tuple: (model, selected_features)
    except Exception as e:
        st.error(f"Failed to load model or features: {e}")
        return None, None

df_main = load_data()
model, selected_features = load_model()

if model is None:
    st.stop()

# ---------------- Sidebar Filters ----------------
st.sidebar.header("Filter TED Talks")

if st.sidebar.button("Clear All Filters"):
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

# ---------------- Predict Views ----------------
if all(feature in filtered_df.columns for feature in selected_features):
    X_pred = filtered_df[selected_features].copy()
    filtered_df['predicted_views'] = model.predict(X_pred)
else:
    st.warning("Some required features for prediction are missing from the filtered dataset.")

# ---------------- Display Filtered Data ----------------
st.subheader("Filtered Dataset Preview")
columns_to_display = ['title', 'speaker', 'views', 'year', 'duration', 'tags']
if 'predicted_views' in filtered_df.columns:
    columns_to_display.append('predicted_views')
st.dataframe(filtered_df[columns_to_display].head(20))

# ---------------- Download Button ----------------
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_ted_talks.csv",
    mime="text/csv"
)

if not filtered_df.empty:
    # --- Top Tags ---
    st.subheader("Top 20 Tags in Filtered Data")
    top_tags = filtered_df['tags'].explode().value_counts().head(20)
    st.bar_chart(top_tags)

    # --- Views Trend ---
    st.subheader("Average Views by Year (Trend Detection)")
    trend = filtered_df.groupby("year")["views"].mean().reset_index()
    fig_trend = px.line(trend, x="year", y="views", markers=True, title="Trend: Average Views Over Time")
    st.plotly_chart(fig_trend, use_container_width=True)

    # --- Duration Distribution ---
    st.subheader("Talk Duration Distribution")
    fig_duration = px.histogram(
        filtered_df,
        x="duration",
        nbins=30,
        title="Histogram: Talk Duration",
        labels={"duration": "Duration (seconds)"},
        opacity=0.75
    )
    fig_duration.update_layout(bargap=0.1)
    st.plotly_chart(fig_duration, use_container_width=True)

    # --- Views Distribution ---
    st.subheader("Views Distribution (Log Scale)")
    fig_views = px.histogram(
        filtered_df,
        x="views",
        nbins=50,
        log_y=True,
        title="Histogram: Views (Log Scale)",
        labels={"views": "Views"},
        opacity=0.75
    )
    fig_views.update_layout(bargap=0.1)
    st.plotly_chart(fig_views, use_container_width=True)

    # --- Talks Per Year ---
    st.subheader("Number of Talks Per Year")
    talks_per_year = filtered_df['year'].value_counts().sort_index()
    st.bar_chart(talks_per_year)

    # --- 2D Scatter Plot ---
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

    # --- K-Means Clustering ---
    st.subheader(f"K-Means Clustering: Views vs Duration ({num_clusters} Clusters)")
    clustering_data = filtered_df[['views', 'duration']].dropna()
    scaler = StandardScaler()
    clustering_scaled = scaler.fit_transform(clustering_data)

    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
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

    # --- Actual vs Predicted Views ---
    if 'predicted_views' in filtered_df.columns:
        st.subheader("Actual vs Predicted Views")
        fig_pred = px.scatter(
            filtered_df,
            x='views',
            y='predicted_views',
            hover_data=['title', 'speaker'],
            title="Actual vs Predicted Views",
            labels={'views': 'Actual Views', 'predicted_views': 'Predicted Views'}
        )
        fig_pred.add_shape(
            type='line',
            x0=0, y0=0,
            x1=filtered_df['views'].max(), y1=filtered_df['views'].max(),
            line=dict(color='red', dash='dash')
        )
        st.plotly_chart(fig_pred, use_container_width=True)

else:
    st.warning("No results match your filters. Try adjusting the filters above.")

# ---------------- Footer ----------------
st.markdown("Data source: TED Talk transcripts processed and analyzed by SpeakScape.")
st.markdown("---")
st.caption("Built using Streamlit | Powered by TED Talks | Data from Kaggle | Stock images from Unsplash")
