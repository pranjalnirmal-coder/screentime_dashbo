# exp8b.py
import pandas as pd
import plotly.express as px

# ------------------- Load Dataset -------------------
def load_data(path="ScreevsmentalH.csv"):
    df = pd.read_csv(path)
    return df


# ------------------- Filter Data -------------------
def filter_data(df, genders=None, age_range=(0, 100), screen_time_range=(0, 24)):
    filtered_df = df.copy()

    # Apply filters based on real column names
    if genders:
        filtered_df = filtered_df[filtered_df["gender"].isin(genders)]

    filtered_df = filtered_df[
        (filtered_df["age"] >= age_range[0]) & (filtered_df["age"] <= age_range[1])
    ]

    filtered_df = filtered_df[
        (filtered_df["screen_time_hours"] >= screen_time_range[0]) &
        (filtered_df["screen_time_hours"] <= screen_time_range[1])
    ]

    return filtered_df


# ------------------- Summary Statistics -------------------
def get_summary_stats(df):
    return {
        "Avg Screen Time": round(df["screen_time_hours"].mean(), 2),
        "Avg Mental Wellness Score": round(df["mental_wellness_index_0_100"].mean(), 2),
        "Avg Sleep Hours": round(df["sleep_hours"].mean(), 2),
    }


# ------------------- Graph 1: Screen Time vs Mental Wellness -------------------
def graph_screen_vs_wellness(df):
    return px.scatter(
        df,
        x="screen_time_hours",
        y="mental_wellness_index_0_100",
        color="gender",
        size="sleep_hours",
        title="Screen Time vs Mental Wellness (Colored by Gender)",
    )


# ------------------- Graph 2: Sleep vs Mental Wellness -------------------
def graph_sleep_vs_wellness(df):
    return px.line(
        df,
        x="sleep_hours",
        y="mental_wellness_index_0_100",
        color="gender",
        markers=True,
        title="Sleep Hours vs Mental Wellness",
    )


# ------------------- Graph 3: Average Wellness by Gender -------------------
def graph_avg_wellness_by_gender(df):
    avg_wellness = df.groupby("gender")["mental_wellness_index_0_100"].mean().reset_index()
    return px.bar(
        avg_wellness,
        x="gender",
        y="mental_wellness_index_0_100",
        color="gender",
        title="Average Mental Wellness by Gender",
    )


# ------------------- Graph 4: Stress Level vs Mental Wellness -------------------
def graph_stress_vs_wellness(df):
    return px.scatter(
        df,
        x="stress_level_0_10",
        y="mental_wellness_index_0_100",
        color="gender",
        size="sleep_quality_1_5",
        title="Stress Level vs Mental Wellness",
    )


# ------------------- Graph 5: Exercise Minutes vs Mental Wellness -------------------
def graph_exercise_vs_wellness(df):
    return px.scatter(
        df,
        x="exercise_minutes_per_week",
        y="mental_wellness_index_0_100",
        color="gender",
        size="social_hours_per_week",
        title="Exercise Minutes vs Mental Wellness (Bubble = Social Hours)",
    )
