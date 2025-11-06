"""
exp8b.py — Backend plot generator
Generates 5 visualizations from ScreevsmentalH.csv and saves to 'exp8_plots/'
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_plots(csv_path="ScreevsmentalH.csv", out_dir="exp8_plots"):
    os.makedirs(out_dir, exist_ok=True)
    df = pd.read_csv(csv_path)

    # 1️⃣ Line plot: age vs stress_level_0_10
    plt.figure(figsize=(8,5))
    plt.scatter(df['age'], df['stress_level_0_10'], alpha=0.7)
    z = np.polyfit(df['age'], df['stress_level_0_10'], 1)
    p = np.poly1d(z)
    xseq = np.linspace(df['age'].min(), df['age'].max(), 100)
    plt.plot(xseq, p(xseq))
    plt.title("Age vs Stress Level (0–10)")
    plt.xlabel("Age")
    plt.ylabel("Stress Level (0–10)")
    plt.grid(True, linestyle=':', linewidth=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "line_age_vs_stress.png"))
    plt.close()

    # 2️⃣ Bar chart: occupation vs stress_level_0_10
    occ_mean = df.groupby('occupation')['stress_level_0_10'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10,6))
    occ_mean.plot(kind='bar', edgecolor='black')
    plt.title("Average Stress Level by Occupation")
    plt.xlabel("Occupation")
    plt.ylabel("Avg Stress Level (0–10)")
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle=':', linewidth=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "bar_occupation_vs_stress.png"))
    plt.close()

    # 3️⃣ Box plot: stress_level_0_10 by work_mode
    plt.figure(figsize=(8,5))
    work_modes = df['work_mode'].unique()
    data_to_plot = [df.loc[df['work_mode']==wm, 'stress_level_0_10'].values for wm in work_modes]
    plt.boxplot(data_to_plot, labels=work_modes, patch_artist=True)
    plt.title("Stress Level by Work Mode")
    plt.xlabel("Work Mode")
    plt.ylabel("Stress Level (0–10)")
    plt.grid(axis='y', linestyle=':', linewidth=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "box_stress_by_workmode.png"))
    plt.close()

    # 4️⃣ Scatter plot: screen_time_hours vs mental_wellness_index_0_100
    plt.figure(figsize=(8,6))
    plt.scatter(df['screen_time_hours'], df['mental_wellness_index_0_100'], alpha=0.7)
    mask = ~np.isnan(df['screen_time_hours']) & ~np.isnan(df['mental_wellness_index_0_100'])
    z2 = np.polyfit(df.loc[mask, 'screen_time_hours'], df.loc[mask, 'mental_wellness_index_0_100'], 1)
    p2 = np.poly1d(z2)
    xs = np.linspace(df['screen_t_]()
