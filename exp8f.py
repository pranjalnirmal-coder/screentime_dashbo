# exp8b_frontend.py
import streamlit as st
from exp8b import (
    load_data, filter_data, get_summary_stats,
    graph_screen_vs_wellness, graph_sleep_vs_wellness,
    graph_avg_wellness_by_gender, graph_stress_vs_wellness,
    graph_exercise_vs_wellness
)

# ---------------- Page Config ----------------
st.set_page_config(page_title="🧠 Screen Time & Mental Wellness Dashboard", layout="wide")

# ---------------- Title ----------------
st.title("📱 Screen Time vs Mental Wellness Insights")
st.markdown("Explore how lifestyle factors like screen time, sleep, exercise, and stress impact mental wellness.")

# ---------------- Load Dataset ----------------
df = load_data()

# ---------------- Sidebar Filters ----------------
st.sidebar.header("🔍 Filters")

gender_options = st.sidebar.multiselect(
    "Select Gender",
    options=df["gender"].unique(),
    default=list(df["gender"].unique())
)

age_min, age_max = int(df["age"].min()), int(df["age"].max())
age_range = st.sidebar.slider("Select Age Range", age_min, age_max, (age_min, age_max))

screen_min, screen_max = int(df["screen_time_hours"].min()), int(df["screen_time_hours"].max())
screen_range = st.sidebar.slider("Select Screen Time Range (hours)", screen_min, screen_max, (screen_min, screen_max))

# ---------------- Apply Filters ----------------
filtered_df = filter_data(df, genders=gender_options, age_range=age_range, screen_time_range=screen_range)

# ---------------- Key Insights ----------------
st.subheader("📊 Key Insights")
stats = get_summary_stats(filtered_df)

col1, col2, col3 = st.columns(3)
col1.metric("Avg Screen Time (hrs)", stats["Avg Screen Time"])
col2.metric("Avg Mental Wellness", stats["Avg Mental Wellness Score"])
col3.metric("Avg Sleep Hours", stats["Avg Sleep Hours"])

st.markdown("---")

# ---------------- 5 Graphs ----------------
st.subheader("📈 Visual Insights")

st.plotly_chart(graph_screen_vs_wellness(filtered_df), use_container_width=True)
st.plotly_chart(graph_sleep_vs_wellness(filtered_df), use_container_width=True)
st.plotly_chart(graph_avg_wellness_by_gender(filtered_df), use_container_width=True)
st.plotly_chart(graph_stress_vs_wellness(filtered_df), use_container_width=True)
st.plotly_chart(graph_exercise_vs_wellness(filtered_df), use_container_width=True)


