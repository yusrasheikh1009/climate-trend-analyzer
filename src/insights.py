def generate_insights(df):
    insights = []

    temp_change = df['Temperature'].iloc[-1] - df['Temperature'].iloc[0]
    co2_change = df['CO2'].iloc[-1] - df['CO2'].iloc[0]

    if temp_change > 0:
        insights.append(f"🌡 Temperature increased by {temp_change:.2f}°C")

    if co2_change > 0:
        insights.append(f"🌍 CO₂ increased by {co2_change:.2f} ppm")

    if df['Rainfall'].mean() > 110:
        insights.append("🌧 High rainfall observed")

    return insights