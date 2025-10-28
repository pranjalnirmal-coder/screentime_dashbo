import streamlit as st
import plotly.express as px
from exp8b import load_data, filter_data

st.set_page_config(
    page_title="📱 Screen Time vs Mental Wellness Dashboard",
    page_icon="🧠",
    layout="wide",
)

df = load_data()

st.title("📱 Screen Time vs Mental Wellness Insights")
st.markdown("Analyze how screen time, sleep, and lifestyle factors affect mental wellness scores.")

st.sidebar.header("🔍 Filters")

if 'Gender' in df.columns:
    genders = sorted(df['Gender'].dropna().unique())
    selected_genders = st.sidebar.multiselect("Select Gender", options=genders, default=genders)
else:
    selected_genders = None

if 'Age' in df.columns:
    min_age = int(df['Age'].min())
    max_age = int(df['Age'].max())
    selected_age = st.sidebar.slider("Select Age Range", min_age, max_age, (min_age, max_age))
else:
    selected_age = None

if 'ScreenTime' in df.columns:
    min_screen = int(df['ScreenTime'].min())
    max_screen = int(df['ScreenTime'].max())
    selected_screen = st.sidebar.slider("Select Screen Time Range (hours)", min_screen, max_screen, (min_screen, max_screen))
else:
    selected_screen = None

filtered_df = filter_data(df, gender=selected_genders, age_range=selected_age, screen_range=selected_screen)

st.subheader("📊 Key Insights")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Screen Time (hrs)", round(filtered_df['ScreenTime'].mean(), 2))
col2.metric("Avg Mental Wellness Score", round(filtered_df['MentalWellness'].mean(), 2))
col3.metric("Avg Sleep Hours", round(filtered_df['SleepHours'].mean(), 2))

st.divider()

st.subheader("📱 Screen Time vs Mental Wellness")
fig1 = px.scatter(
    filtered_df,
    x="ScreenTime",
    y="MentalWellness",
    color="Gender" if "Gender" in filtered_df.columns else None,
    trendline="ols",
    title="Relationship between Screen Time and Mental Wellness",
)
st.plotly_chart(fig1, use_container_width=True)

if "SleepHours" in filtered_df.columns:
    st.subheader("😴 Sleep Hours vs Mental Wellness")
    fig2 = px.scatter(
        filtered_df,
        x="SleepHours",
        y="MentalWellness",
        color="Gender" if "Gender" in filtered_df.columns else None,
        trendline="ols",
        title="Sleep Impact on Mental Wellness"
    )
    st.plotly_chart(fig2, use_container_width=True)

if "Age" in filtered_df.columns:
    st.subheader("📊 Average Screen Time by Age")
    age_df = filtered_df.groupby('Age')['ScreenTime'].mean().reset_index()
    fig3 = px.bar(age_df, x='Age', y='ScreenTime', color='ScreenTime', text='ScreenTime')
    st.plotly_chart(fig3, use_container_width=True)

st.success("✅ Dashboard loaded successfully!")
