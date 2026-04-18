import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def run_forecast(df, steps=12):
    """
    Fixed forecasting with duplicate handling + proper time index
    """

    df = df.copy()

    # -----------------------------
    # CLEAN + PREPARE
    # -----------------------------
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values("Date")

    # 🚨 FIX: REMOVE DUPLICATES BY AGGREGATION
    # Take mean temperature for same date
    df = df.groupby('Date').mean(numeric_only=True).reset_index()

    # Set index
    df.set_index("Date", inplace=True)

    # Set frequency
    df = df.asfreq("ME")

    # Fill missing values
    df['Temperature'] = df['Temperature'].interpolate()

    # -----------------------------
    # MODEL
    # -----------------------------
    model = ARIMA(df['Temperature'], order=(2, 1, 2))
    model_fit = model.fit()

    # -----------------------------
    # FORECAST
    # -----------------------------
    forecast = model_fit.forecast(steps=steps)

    future_dates = pd.date_range(
        start=df.index[-1],
        periods=steps,
        freq='ME'
    )

    forecast_df = pd.DataFrame({
        "Date": future_dates,
        "Forecast_Temperature": forecast.values
    })

    return forecast_df