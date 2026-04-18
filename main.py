from src.data_loader import load_data
from src.preprocess import clean_data
from src.analysis import plot_trends
from src.anomaly import detect_anomalies
from src.forecast import run_forecast

print("📥 Loading data...")
df = load_data("data/climate_data.csv")

print("⚙️ Cleaning data...")
df = clean_data(df)

print("📊 Plotting trends...")
plot_trends(df)

print("🚨 Detecting anomalies...")
anomalies = detect_anomalies(df)

print("\nAnomalies Found:")
print(anomalies[['Date', 'Temperature']])

print("🔮 Forecasting future temperature...")

forecast_df = run_forecast(df)

print("\nForecast Values:")
print(forecast_df)

# Optional: Save forecast
forecast_df.to_csv("outputs/forecast.csv", index=False)

print("\n✅ Forecast saved to outputs/forecast.csv")