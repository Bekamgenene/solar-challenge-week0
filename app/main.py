
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from io import BytesIO
from app.utils import load_country_data, summary_statistics, get_country_metrics


st.set_page_config(
    page_title="Solar Insights Dashboard 🌞",
    layout="wide",
    initial_sidebar_state="expanded"
)
sns.set_style("whitegrid")

DATA_DIR = os.path.join(os.getcwd(), "data")


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Overview", "Country Comparison", "Explore Country", "Analytics Lab"])


if page == "Overview":
    st.title("☀️ Solar Insights Dashboard")
    st.markdown("""
    Welcome to the **Solar Data Discovery Dashboard** developed for **10 Academy Week 0**.
    
    This app enables dynamic exploration of solar radiation datasets across **Benin**, **Sierra Leone**, and **Togo**.

    ---
    **Features:**
    - Compare GHI, DNI, and DHI across countries
    - Explore trends within each dataset
    - Generate correlation heatmaps and statistical summaries
    - Download results interactively
    """)

    df_summary = get_country_metrics(DATA_DIR)
    st.subheader("Average Solar Irradiance per Country")
    st.dataframe(df_summary.set_index("country"))

    fig, ax = plt.subplots(figsize=(7,5))
    sns.barplot(data=df_summary, x="country", y="GHI", palette="viridis")
    ax.set_title("Average GHI by Country", fontsize=13)
    st.pyplot(fig)


elif page == "Country Comparison":
    st.title("🌍 Cross-Country Comparison")
    st.markdown("Compare irradiance metrics across selected countries.")

    # Select countries and metric
    countries = st.multiselect(
        "Select countries to compare:",
        ["Benin", "Sierra Leone", "Togo"],
        default=["Benin", "Sierra Leone", "Togo"]
    )
    metric = st.selectbox("Select metric:", ["GHI", "DNI", "DHI"])

    dfs = []
    for c in countries:
        df = load_country_data(c, DATA_DIR)
        df["country"] = c
        dfs.append(df)
    df_all = pd.concat(dfs, ignore_index=True)

    # Boxplot
    fig, ax = plt.subplots(figsize=(10,6))
    sns.boxplot(data=df_all, x="country", y=metric, palette="viridis")
    ax.set_title(f"{metric} Distribution by Country")
    st.pyplot(fig)

    # Summary statistics
    st.subheader("📊 Summary Table")
    summary = df_all.groupby("country")[metric].agg(["mean", "median", "std"]).round(2)
    st.dataframe(summary)

    # Download summary
    csv = summary.to_csv().encode("utf-8")
    st.download_button("⬇️ Download Summary CSV", csv, file_name="comparison_summary.csv", mime="text/csv")


elif page == "Explore Country":
    st.title("📈 Explore Country Data")

    country = st.selectbox("Choose a country:", ["Benin", "Sierra Leone", "Togo"])
    df = load_country_data(country, DATA_DIR)
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

    metric = st.selectbox("Select Metric to visualize:", ["GHI", "DNI", "DHI", "Tamb", "RH"])

    # Filter by date range
    if "Timestamp" in df.columns:
        min_date, max_date = df["Timestamp"].min(), df["Timestamp"].max()
        date_range = st.slider(
            "Select date range:",
            min_value=min_date.to_pydatetime(),
            max_value=max_date.to_pydatetime(),
            value=(min_date.to_pydatetime(), max_date.to_pydatetime())
        )
        df = df[(df["Timestamp"] >= date_range[0]) & (df["Timestamp"] <= date_range[1])]

    # Plot
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(df["Timestamp"], df[metric], color="darkorange", alpha=0.8)
    ax.set_title(f"{metric} over Time - {country}")
    ax.set_xlabel("Time")
    ax.set_ylabel(metric)
    st.pyplot(fig)

  
    st.subheader("Summary Statistics")
    st.dataframe(summary_statistics(df))

   
    st.subheader("Correlation Heatmap")
    corr_cols = [c for c in ["GHI","DNI","DHI","Tamb","RH","WS"] if c in df.columns]
    fig, ax = plt.subplots(figsize=(7,5))
    sns.heatmap(df[corr_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
    ax.set_title(f"Correlation Matrix - {country}")
    st.pyplot(fig)


elif page == "Analytics Lab":
    st.title("🧠 Analytics Lab")
    st.markdown("""
    Dive deeper into the data — visualize relationships and compare performance.
    """)

    countries = ["Benin", "Sierra Leone", "Togo"]
    metric_x = st.selectbox("Select X-axis Metric:", ["GHI", "DNI", "DHI", "Tamb"])
    metric_y = st.selectbox("Select Y-axis Metric:", ["Tamb", "RH", "WS", "DHI"])

    dfs = []
    for c in countries:
        df = load_country_data(c, DATA_DIR)
        df["country"] = c
        dfs.append(df)
    df_all = pd.concat(dfs, ignore_index=True)

    # Scatter plot with color by country
    fig, ax = plt.subplots(figsize=(8,6))
    sns.scatterplot(data=df_all, x=metric_x, y=metric_y, hue="country", alpha=0.7)
    ax.set_title(f"{metric_x} vs {metric_y} by Country")
    st.pyplot(fig)

    # Correlation heatmap (combined)
    st.subheader("Global Correlation Heatmap (All Countries Combined)")
    corr_cols = [c for c in ["GHI","DNI","DHI","Tamb","RH","WS","BP"] if c in df_all.columns]
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(df_all[corr_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
    st.pyplot(fig)

    
    csv_data = df_all.sample(min(1000, len(df_all)), random_state=42).to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download Sample Combined Data", csv_data, file_name="combined_sample.csv")


st.markdown("""
---
Developed by **Bekam Genene** for **10 Academy Solar Challenge Week 0**  
🌞 *"Turning sunlight into insight!"*  
🔗 [GitHub Repository](https://github.com/Bekamgenene/solar-challenge-week0)
""")
