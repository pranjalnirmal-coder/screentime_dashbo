import pandas as pd

def load_data(path="ScreevsmentalH.csv"):
    """Load and clean dataset"""
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Dataset not found at path: {path}")

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-', '_')

    # Rename key columns
    rename_map = {
        'screen_time_hours': 'ScreenTime',
        'mental_wellness_index_0_100': 'MentalWellness',
        'sleep_hours': 'SleepHours',
        'gender': 'Gender',
        'age': 'Age',
        'stress_level_0_10': 'StressLevel',
        'occupation': 'Occupation',
        'work_mode': 'WorkMode'
    }
    df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns}, inplace=True)

    # Drop rows missing critical columns
    df.dropna(subset=['ScreenTime', 'MentalWellness'], inplace=True)

    # Convert numeric columns
    for col in ['ScreenTime', 'MentalWellness', 'SleepHours', 'Age', 'StressLevel']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df


def filter_data(df, gender=None, age_range=None, screen_range=None):
    """Filter dataset based on sidebar selections"""
    dff = df.copy()

    if gender and 'Gender' in dff.columns:
        dff = dff[dff['Gender'].isin(gender)]

    if age_range and 'Age' in dff.columns:
        dff = dff[(dff['Age'] >= age_range[0]) & (dff['Age'] <= age_range[1])]

    if screen_range and 'ScreenTime' in dff.columns:
        dff = dff[(dff['ScreenTime'] >= screen_range[0]) & (dff['ScreenTime'] <= screen_range[1])]

    return dff
