import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_trends(df):
    """
    Advanced multi-panel interactive dashboard
    """

    df = df.copy()
    df['Date'] = pd.to_datetime(df['Date'])

    # Remove duplicates
    df = df.groupby('Date').mean(numeric_only=True).reset_index()

    # Rolling averages (smooth trends)
    df['Temp_Rolling'] = df['Temperature'].rolling(12).mean()

    if 'Rainfall' in df.columns:
        df['Rain_Rolling'] = df['Rainfall'].rolling(12).mean()

    if 'CO2' in df.columns:
        df['CO2_Rolling'] = df['CO2'].rolling(12).mean()

    # -----------------------------
    # CREATE SUBPLOTS (3 PANELS)
    # -----------------------------
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=("🌡 Temperature Trend", "🌧 Rainfall Trend", "🌍 CO2 Trend"),
        vertical_spacing=0.1
    )

    # -----------------------------
    # TEMPERATURE
    # -----------------------------
    fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['Temperature'],
            mode='lines',
            name='Temperature',
            line=dict(width=2)
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['Temp_Rolling'],
            mode='lines',
            name='Temp Trend',
            line=dict(width=3, dash='dash')
        ),
        row=1, col=1
    )

    # -----------------------------
    # RAINFALL
    # -----------------------------
    if 'Rainfall' in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df['Date'],
                y=df['Rainfall'],
                mode='lines',
                name='Rainfall',
                line=dict(width=2)
            ),
            row=2, col=1
        )

        fig.add_trace(
            go.Scatter(
                x=df['Date'],
                y=df['Rain_Rolling'],
                mode='lines',
                name='Rain Trend',
                line=dict(width=3, dash='dash')
            ),
            row=2, col=1
        )

    # -----------------------------
    # CO2
    # -----------------------------
    if 'CO2' in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df['Date'],
                y=df['CO2'],
                mode='lines',
                name='CO2',
                line=dict(width=2)
            ),
            row=3, col=1
        )

        fig.add_trace(
            go.Scatter(
                x=df['Date'],
                y=df['CO2_Rolling'],
                mode='lines',
                name='CO2 Trend',
                line=dict(width=3, dash='dash')
            ),
            row=3, col=1
        )

    # -----------------------------
    # LAYOUT (THIS MAKES IT LOOK PRO)
    # -----------------------------
    fig.update_layout(
        title="📊 Climate Trend Dashboard (Advanced)",
        height=900,
        template="plotly_dark",
        hovermode="x unified"
    )

    # Show interactive graph
    fig.show()