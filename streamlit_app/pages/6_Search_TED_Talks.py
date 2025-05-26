import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- Page Setup ----------------
st.set_page_config(page_title="TED Talks Dashboard", layout="wide")
st.title("SpeakScape: TED Talks Insights")

st.markdown("""
Explore TED Talks data by year, speaker, tags, and duration.  
Discover patterns in engagement, presentation length, and more.
""")

# ---------------- Load Data ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/combined_dataset.csv")
    df['year'] = pd.to_datetime(df['recorded_date'], errors='coerce').dt.year
    df['tags'] = df['tags'].apply(lambda x: eval(x) if isinstance(x, str) and x.startswith("[") else [])
    return df

df = load_data()

# ---------------- Sidebar Filters ----------------
st.sidebar.header("Filter Options")

# Year filter
years = sorted(df['year'].dropna().unique())
selected_years = st.sidebar.multiselect("Select Year(s)", years)

# Speaker filter
speakers = sorted(df['speaker'].dropna().unique())
selected_speaker = st.sidebar.selectbox("Select Speaker", ["All"] + speakers)

# Duration filter
min_duration, max_duration = int(df['duration'].min()), int(df['duration'].max())
duration_range = st.sidebar.slider("Select Duration Range (seconds)", min_value=min_duration, max_value=max_duration, value=(min_duration, max_duration))

# Tag keyword filter
tag_keyword = st.sidebar.text_input("Search Tags (Keyword Match)")

# ---------------- Apply Filters ----------------
filtered_df = df.copy()

if selected_years:
    filtered_df = filtered_df[filtered_df['year'].isin(selected_years)]

if selected_speaker != "All":
    filtered_df = filtered_df[filtered_df['speaker'] == selected_speaker]

filtered_df = filtered_df[filtered_df['duration'].between(*duration_range)]

if tag_keyword:
    filtered_df = filtered_df[filtered_df['tags'].apply(lambda tags: any(tag_keyword.lower() in tag.lower() for tag in tags))]

# ---------------- Show Data ----------------
st.subheader("Filtered TED Talks")
st.dataframe(filtered_df[['title', 'speaker', 'year', 'duration', 'views', 'tags']].head(20))

# ---------------- Download Button ----------------
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_ted_talks.csv",
    mime="text/csv"
)

# ---------------- Visualizations ----------------

if not filtered_df.empty:
    # --- Views by Year ---
    st.subheader("Average Views by Year")
    views_by_year = filtered_df.groupby("year")["views"].mean().reset_index()
    fig1 = px.line(views_by_year, x="year", y="views", title="Average Views Over Time", markers=True)
    st.plotly_chart(fig1, use_container_width=True)

    # --- Duration Distribution ---
    st.subheader("Talk Duration Distribution")
    fig2 = px.histogram(filtered_df, x="duration", nbins=30, title="Distribution of Talk Durations")
    st.plotly_chart(fig2, use_container_width=True)

    # --- Views Distribution ---
    st.subheader("Views Distribution (Log Scale)")
    fig3 = px.histogram(filtered_df, x="views", nbins=40, log_y=True, title="Distribution of Views (Log Scale)")
    st.plotly_chart(fig3, use_container_width=True)

    # --- Views vs Duration ---
    st.subheader("Views vs Duration")
    fig4 = px.scatter(
        filtered_df,
        x="duration",
        y="views",
        hover_data=["title", "speaker", "year"],
        color="year",
        title="Views vs Duration (Colored by Year)"
    )
    st.plotly_chart(fig4, use_container_width=True)

    # --- Talks per Year ---
    st.subheader("Number of Talks Per Year")
    talks_per_year = filtered_df['year'].value_counts().sort_index().reset_index()
    talks_per_year.columns = ['year', 'count']
    fig5 = px.bar(talks_per_year, x='year', y='count', title='Number of Talks by Year')
    st.plotly_chart(fig5, use_container_width=True)

else:
    st.warning("No results match your filters. Try adjusting the filters in the sidebar.")
