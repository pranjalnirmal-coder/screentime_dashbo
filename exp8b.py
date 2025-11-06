# exp8b_backend.py
import pandas as pd

# Function to load dataset
def load_data(path="ScreevsmentalH.csv"):
    df = pd.read_csv(path)
    return df

# Function to filter dataset
def filter_data(df, genders=None, age_range=(0, 100), screen_time_range=(0, 24)):
    filtered_df = df.copy()

    # Apply filters
    if genders:
        filtered_df = filtered_df[filtered_df["Gender"].isin(genders)]

    if "Age" in df.columns:
        filtered_df = filtered_df[
            (filtered_df["Age"] >= age_range[0]) & (filtered_df["Age"] <= age_range[1])
        ]

    if "Screen Time (hours)" in df.columns:
        filtered_df = filtered_df[
            (filtered_df["Screen Time (hours)"] >= screen_time_range[0]) &
            (filtered_df["Screen Time (hours)"] <= screen_time_range[1])
        ]

    return filtered_df

# Function to compute key insights
def get_summary_stats(df):
    return {
        "Avg Screen Time": round(df["Screen Time (hours)"].mean(), 2),
        "Avg Mental Wellness Score": round(df["Mental Wellness Score"].mean(), 2),
        "Avg Sleep Hours": round(df["Sleep Hours"].mean(), 2),
    }
