import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib

# ---------------- Page Setup ----------------
st.set_page_config(page_title="TED Talks Dashboard", layout="wide")
st.title("SpeakScape: TED Talks Insights")

st.markdown("""
Explore TED Talks data by year, speaker, tags, and duration.  
Predict engagement using machine learning and discover clusters with K-Means.
""")

# ---------------- Load Data ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/combined_dataset.csv")
    df['year'] = pd.to_datetime(df['recorded_date'], errors='coerce').dt.year
    df['tags'] = df['tags'].apply(lambda x: eval(x) if isinstance(x, str) and x.startswith("[") else [])
    return df

@st.cache_resource
def load_model():
    try:
        model = joblib.load("files/random_forest_model.pkl")
        feature_df = pd.read_csv("files/scaled_features.csv")
        features = list(feature_df.columns)
        return model, features
    except Exception as e:
        st.warning(f"Model or features could not be loaded: {e}")
        return None, []

df = load_data()
model, selected_features = load_model()

# ---------------- Sidebar Filters ----------------
st.sidebar.header("Filter Options")

years = sorted(df['year'].dropna().unique())
speakers = sorted(df['speaker'].dropna().unique())
min_duration, max_duration = int(df['duration'].min()), int(df['duration'].max())

selected_years = st.sidebar.multiselect("Select Year(s)", years)
selected_speaker = st.sidebar.selectbox("Select Speaker", ["All"] + speakers)
duration_range = st.sidebar.slider("Select Duration Range (seconds)", min_value=min_duration, max_value=max_duration, value=(min_duration, max_duration))
tag_keyword = st.sidebar.text_input("Search Tags (Keyword Match)")
num_clusters = st.sidebar.slider("K-Means Clusters", 2, 10, 3)

# ---------------- Apply Filters ----------------
filtered_df = df.copy()
if selected_years:
    filtered_df = filtered_df[filtered_df['year'].isin(selected_years)]
if selected_speaker != "All":
    filtered_df = filtered_df[filtered_df['speaker'] == selected_speaker]
filtered_df = filtered_df[filtered_df['duration'].between(*duration_range)]
if tag_keyword:
    filtered_df = filtered_df[filtered_df['tags'].apply(lambda tags: any(tag_keyword.lower() in tag.lower() for tag in tags))]

# ---------------- Predict Views ----------------
if model and all(f in filtered_df.columns for f in selected_features):
    try:
        X_pred = filtered_df[selected_features].copy()
        filtered_df['predicted_views'] = model.predict(X_pred)
    except Exception as e:
        st.error(f"Prediction error: {e}")
else:
    st.warning("Model or required features not found in the filtered dataset.")

# ---------------- Display Filtered Data ----------------
st.subheader("Filtered TED Talks")
columns_to_show = ['title', 'speaker', 'year', 'duration', 'views']
if 'predicted_views' in filtered_df.columns:
    columns_to_show.append('predicted_views')
st.dataframe(filtered_df[columns_to_show].head(20))

# ---------------- Download Button ----------------
csv = filtered_df.to_csv(index=False)
st.download_button("Download Filtered Data", csv, "filtered_ted_talks.csv", "text/csv")

# ---------------- Visualizations ----------------
if not filtered_df.empty:

    st.subheader("Average Views by Year")
    views_by_year = filtered_df.groupby("year")["views"].mean().reset_index()
    st.plotly_chart(px.line(views_by_year, x="year", y="views", title="Avg Views by Year", markers=True), use_container_width=True)

    st.subheader("Talk Duration Distribution")
    st.plotly_chart(px.histogram(filtered_df, x="duration", nbins=30, title="Talk Duration Distribution"), use_container_width=True)

    st.subheader("Views Distribution (Log Scale)")
    st.plotly_chart(px.histogram(filtered_df, x="views", nbins=40, log_y=True, title="Views Distribution (Log Scale)"), use_container_width=True)

    st.subheader("Views vs Duration")
    st.plotly_chart(px.scatter(filtered_df, x="duration", y="views", hover_data=['title'], color="year", title="Views vs Duration"), use_container_width=True)

    # Actual vs Predicted
    if 'predicted_views' in filtered_df.columns:
        st.subheader("Actual vs Predicted Views")
        fig_pred = px.scatter(filtered_df, x="views", y="predicted_views", hover_data=['title', 'speaker'], title="Actual vs Predicted")
        fig_pred.add_shape(type="line", x0=0, y0=0, x1=filtered_df['views'].max(), y1=filtered_df['views'].max(), line=dict(color="red", dash="dash"))
        st.plotly_chart(fig_pred, use_container_width=True)

    # ---------------- K-Means Clustering ----------------
    st.subheader(f"K-Means Clustering (Views vs Duration) – {num_clusters} Clusters")
    clustering_data = filtered_df[['views', 'duration']].dropna()
    scaler = StandardScaler()
    scaled = scaler.fit_transform(clustering_data)

    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    clustering_data['cluster'] = kmeans.fit_predict(scaled)

    fig_cluster = px.scatter(
        clustering_data,
        x="duration",
        y="views",
        color="cluster",
        title="K-Means Clustering: TED Talks",
        labels={"cluster": "Cluster"},
        opacity=0.8
    )
    st.plotly_chart(fig_cluster, use_container_width=True)

else:
    st.warning("No talks match your filters. Try adjusting them.")

# ---------- Footer ----------
st.markdown("Data source: TED Talk transcripts processed and analyzed by SpeakScape.")
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Powered by TED Talks | Data from Kaggle | Stock images from Unsplash")