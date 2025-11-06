# exp8b_frontend.py
import streamlit as st
import plotly.express as px
from exp8b import load_data, filter_data, get_summary_stats

# Page Config
st.set_page_config(page_title="🧠 Screen Time & Mental Wellness Dashboard", layout="wide")

# Title and Description
st.title("Screen Time vs Mental Wellness Insights")
st.markdown("Analyze how screen time, sleep, and lifestyle factors affect mental wellness scores.")

# Load Dataset
df = load_data()

# ---------------- Sidebar Filters ----------------
st.sidebar.header("🔍 Filters")

gender_options = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=list(df["Gender"].unique())
)

age_min, age_max = int(df["Age"].min()), int(df["Age"].max())
age_range = st.sidebar.slider("Select Age Range", age_min, age_max, (age_min, age_max))

screen_min, screen_max = int(df["Screen Time (hours)"].min()), int(df["Screen Time (hours)"].max())
screen_range = st.sidebar.slider("Select Screen Time Range (hours)", screen_min, screen_max, (screen_min, screen_max))

# Apply filters
filtered_df = filter_data(df, genders=gender_options, age_range=age_range, screen_time_range=screen_range)

# ---------------- Key Insights ----------------
st.subheader("📊 Key Insights")
stats = get_summary_stats(filtered_df)

col1, col2, col3 = st.columns(3)
col1.metric("Avg Screen Time (hrs)", stats["Avg Screen Time"])
col2.metric("Avg Mental Wellness Score", stats["Avg Mental Wellness Score"])
col3.metric("Avg Sleep Hours", stats["Avg Sleep Hours"])

st.markdown("---")

# ---------------- Graph 1: Screen Time vs Wellness ----------------
st.subheader("Screen Time vs Mental Wellness")
fig1 = px.scatter(filtered_df, x="Screen Time (hours)", y="Mental Wellness Score",
                  color="Gender", size="Sleep Hours",
                  title="Screen Time vs Mental Wellness")
st.plotly_chart(fig1, use_container_width=True)

# ---------------- Graph 2: Sleep vs Wellness ----------------
st.subheader("Sleep Hours vs Mental Wellness")
fig2 = px.line(filtered_df, x="Sleep Hours", y="Mental Wellness Score",
               color="Gender", markers=True, title="Sleep vs Wellness")
st.plotly_chart(fig2, use_container_width=True)

# ---------------- Graph 3: Average Wellness by Gender ----------------
st.subheader("Average Mental Wellness by Gender")
avg_wellness = filtered_df.groupby("Gender")["Mental Wellness Score"].mean().reset_index()
fig3 = px.bar(avg_wellness, x="Gender", y="Mental Wellness Score", color="Gender",
              title="Average Wellness by Gender")
st.plotly_chart(fig3, use_container_width=True)


