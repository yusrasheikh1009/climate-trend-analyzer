import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Climate Analyzer Pro", layout="wide")

st.title("🌍 Climate Trend Analyzer (Advanced Dashboard)")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/climate_data.csv")
    df['Date'] = pd.to_datetime(df['Date'])

    # Auto-create Region if missing
    if 'Region' not in df.columns:
        regions = ["India", "USA", "Europe"]
        df['Region'] = [regions[i % 3] for i in range(len(df))]

    # Auto-create CO2 if missing
    if 'CO2' not in df.columns:
        df['CO2'] = 350 + (df.index % 100) * 0.1

    return df

df = load_data()

# -----------------------------
# SIDEBAR FILTER
# -----------------------------
st.sidebar.header("🔍 Filters")
region = st.sidebar.selectbox("Select Region", df['Region'].unique())
df_filtered = df[df['Region'] == region]

# -----------------------------
# KPI CARDS
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("🌡 Avg Temp", f"{df_filtered['Temperature'].mean():.2f} °C")
col2.metric("🌧 Avg Rainfall", f"{df_filtered['Rainfall'].mean():.2f} mm")
col3.metric("🌍 Avg CO2", f"{df_filtered['CO2'].mean():.2f} ppm")

# -----------------------------
# MULTI GRAPHS
# -----------------------------
st.subheader("📈 Climate Trends")

col1, col2 = st.columns(2)

with col1:
    fig_temp = px.line(df_filtered, x="Date", y="Temperature", title="Temperature Trend")
    st.plotly_chart(fig_temp, use_container_width=True)

with col2:
    fig_rain = px.line(df_filtered, x="Date", y="Rainfall", title="Rainfall Trend")
    st.plotly_chart(fig_rain, use_container_width=True)

fig_co2 = px.line(df_filtered, x="Date", y="CO2", title="CO2 Trend")
st.plotly_chart(fig_co2, use_container_width=True)

# -----------------------------
# ANOMALY DETECTION
# -----------------------------
st.subheader("🚨 Temperature Anomalies")

df_filtered = df_filtered.copy()
df_filtered['z_score'] = (
    (df_filtered['Temperature'] - df_filtered['Temperature'].mean()) /
    df_filtered['Temperature'].std()
)

fig_anomaly = px.scatter(
    df_filtered,
    x="Date",
    y="Temperature",
    color=df_filtered['z_score'].abs() > 2,
    title="Anomaly Detection"
)

st.plotly_chart(fig_anomaly, use_container_width=True)

# -----------------------------
# 🌍 ANIMATED MAP WITH MOVEMENT
# -----------------------------
st.subheader("🌍 Climate Change Over Time (Moving Map)")

region_coords = {
    "India": {"lat": 20.5937, "lon": 78.9629},
    "USA": {"lat": 37.0902, "lon": -95.7129},
    "Europe": {"lat": 54.5260, "lon": 15.2551}
}

# Base coordinates
df["Latitude"] = df["Region"].map(lambda x: region_coords.get(x, {}).get("lat", 0))
df["Longitude"] = df["Region"].map(lambda x: region_coords.get(x, {}).get("lon", 0))

# 🔥 ADD MOVEMENT (KEY FIX)
np.random.seed(42)
df["Latitude"] = df["Latitude"] + np.random.normal(0, 1, len(df))
df["Longitude"] = df["Longitude"] + np.random.normal(0, 1, len(df))

# Time for animation
df["YearMonth"] = df["Date"].dt.strftime("%Y-%m")

fig_map = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    color="Temperature",
    size="Temperature",
    hover_name="Region",
    animation_frame="YearMonth",
    title="🌍 Global Climate Evolution (Dynamic)",
    color_continuous_scale="Turbo"
)

fig_map.update_layout(
    geo=dict(
        projection_type="natural earth",
        showland=True,
        showcountries=True,
        showcoastlines=True,
        landcolor="rgb(230, 230, 230)"
    ),
    height=600
)

st.plotly_chart(fig_map, use_container_width=True)

# -----------------------------
# YEARLY ANALYSIS
# -----------------------------
st.subheader("📊 Yearly Temperature Distribution")

df['Year'] = df['Date'].dt.year

fig_year = px.box(
    df,
    x="Year",
    y="Temperature",
    color="Region",
    title="Yearly Comparison"
)

st.plotly_chart(fig_year, use_container_width=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("🚀 Climate Analytics Project | Portfolio Ready")