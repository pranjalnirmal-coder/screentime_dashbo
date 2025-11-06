import streamlit as st
import plotly.express as px
from exp8b import load_data, filter_data

st.set_page_config(
    page_title="Screen Time & Stress Dashboard",
    page_icon="",
    layout="wide",
)

df = load_data()

st.title("📊 Screen Time, Stress & Mental Wellness Dashboard")
st.markdown("Analyze relationships between screen time, stress levels, work mode, and mental wellness.")

# Sidebar filters
st.sidebar.header("🔍 Filters")

if 'Gender' in df.columns:
    genders = sorted(df['Gender'].dropna().unique())
    selected_genders = st.sidebar.multiselect("Select Gender", options=genders, default=genders)
else:
    selected_genders = None

if 'Age' in df.columns:
    min_age, max_age = int(df['Age'].min()), int(df['Age'].max())
    selected_age = st.sidebar.slider("Select Age Range", min_age, max_age, (min_age, max_age))
else:
    selected_age = None

if 'ScreenTime' in df.columns:
    min_screen, max_screen = int(df['ScreenTime'].min()), int(df['ScreenTime'].max())
    selected_screen = st.sidebar.slider("Select Screen Time Range (hours)", min_screen, max_screen, (min_screen, max_screen))
else:
    selected_screen = None

filtered_df = filter_data(df, gender=selected_genders, age_range=selected_age, screen_range=selected_screen)

# --- Line Plot: Age vs Stress Level ---
if 'Age' in filtered_df.columns and 'StressLevel' in filtered_df.columns:
    st.subheader("Line Plot: Age vs Stress Level (0–10)")
    fig1 = px.line(
        filtered_df.sort_values("Age"),
        x="Age",
        y="StressLevel",
        markers=True,
        title="📈 Age vs Stress Level (0–10)"
    )
    st.plotly_chart(fig1, use_container_width=True)

# --- Bar Chart: Occupation vs Stress Level ---
if 'Occupation' in filtered_df.columns and 'StressLevel' in filtered_df.columns:
    st.subheader("Bar Chart: Average Stress Level by Occupation")
    bar_df = filtered_df.groupby('Occupation')['StressLevel'].mean().reset_index()
    fig2 = px.bar(
        bar_df,
        x='Occupation',
        y='StressLevel',
        color='StressLevel',
        text_auto=True,
        title="🏢 Average Stress Level by Occupation"
    )
    fig2.update_layout(xaxis_title="Occupation", yaxis_title="Average Stress Level (0–10)")
    st.plotly_chart(fig2, use_container_width=True)

# --- Box Plot: Stress Level by Work Mode ---
if 'WorkMode' in filtered_df.columns and 'StressLevel' in filtered_df.columns:
    st.subheader("Box Plot: Stress Level Distribution by Work Mode")
    fig3 = px.box(
        filtered_df,
        x='WorkMode',
        y='StressLevel',
        color='WorkMode',
        title="💼 Stress Level Distribution by Work Mode"
    )
    fig3.update_layout(xaxis_title="Work Mode", yaxis_title="Stress Level (0–10)")
    st.plotly_chart(fig3, use_container_width=True)

# --- Scatter Plot: Screen Time vs Mental Wellness ---
if 'ScreenTime' in filtered_df.columns and 'MentalWellness' in filtered_df.columns:
    st.subheader("Scatter Plot: Screen Time vs Mental Wellness")
    fig4 = px.scatter(
        filtered_df,
        x='ScreenTime',
        y='MentalWellness',
        color='Gender' if 'Gender' in filtered_df.columns else None,
        trendline='ols',
        title="📱 Relationship Between Screen Time and Mental Wellness"
    )
    fig4.update_layout(xaxis_title="Screen Time (hours per day)", yaxis_title="Mental Wellness Index (0–100)")
    st.plotly_chart(fig4, use_container_width=True)

# --- Histogram: Sleep Hours ---
if 'SleepHours' in filtered_df.columns:
    st.subheader("Histogram: Distribution of Sleep Hours")
    fig5 = px.histogram(
        filtered_df,
        x='SleepHours',
        nbins=12,
        color_discrete_sequence=['skyblue'],
        title="😴 Distribution of Sleep Hours"
    )
    fig5.update_layout(xaxis_title="Sleep Hours (per day)", yaxis_title="Number of People")
    st.plotly_chart(fig5, use_container_width=True)

st.success("✅ All 5 visualizations loaded successfully!")


