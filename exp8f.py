import os
import streamlit as st
import subprocess

st.set_page_config(page_title="Experiment 8 - Data Visualizations", layout="wide")

st.title("📊 Experiment 8 — Data Visualization Dashboard")
st.markdown("This app shows 5 different plots generated from `ScreevsmentalH.csv`.")

plots_dir = "exp8_plots"
csv_path = "ScreevsmentalH.csv"

if not os.path.exists(plots_dir):
    st.warning("⚠️ Plots not found! Running backend script (exp8b.py) to generate them...")
    if os.path.exists(csv_path):
        try:
            subprocess.run(["python", "exp8b.py"], check=True)
            st.success("✅ Plots generated successfully!")
        except Exception as e:
            st.error(f"Error running backend: {e}")
    else:
        st.error("❌ CSV file 'ScreevsmentalH.csv' not found. Please upload or add it to the repo.")

# --- Display plots ---
if os.path.exists(plots_dir):
    images = [f for f in os.listdir(plots_dir) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    if images:
        cols = st.columns(2)
        for i, img in enumerate(sorted(images)):
            with cols[i % 2]:
                st.image(os.path.join(plots_dir, img), caption=img.replace("_", " ").replace(".png", ""), use_container_width=True)
    else:
        st.info("No plot images found yet. Run `exp8b.py` to generate them.")
