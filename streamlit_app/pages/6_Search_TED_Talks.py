# streamlit_app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- Page Setup ----------------
st.set_page_config(page_title="TED Talks Dashboard", layout="wide")
st.title("SpeakScape: TED Talks Insights")

st.markdown("""
This simple dashboard lets you explore TED Talks data by year, speaker, and view count.
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
years = sorted(df['year'].dropna().unique())
speakers = sorted(df['speaker'].dropna().unique())

selected_years = st.sidebar.multiselect("Select Year(s)", years)
selected_speaker = st.sidebar.selectbox("Select Speaker", ["All"] + speakers)

filtered_df = df.copy()

# Apply filters
if selected_years:
    filtered_df = filtered_df[filtered_df['year'].isin(selected_years)]

if selected_speaker != "All":
    filtered_df = filtered_df[filtered_df['speaker'] == selected_speaker]

# ---------------- Show Data ----------------
st.subheader("Filtered TED Talks")
st.dataframe(filtered_df[['title', 'speaker', 'year', 'views', 'duration']].head(20))

# ---------------- Simple Chart ----------------
st.subheader("Average Views by Year")
views_by_year = filtered_df.groupby("year")["views"].mean().reset_index()
fig = px.line(views_by_year, x="year", y="views", title="Average Views Over Time", markers=True)
st.plotly_chart(fig, use_container_width=True)
