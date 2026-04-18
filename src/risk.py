def climate_risk_score(df):
    """
    Simple climate risk scoring based on temperature and CO2
    """

    temp_score = df['Temperature'].mean()
    co2_score = df['CO2'].mean()

    score = (temp_score * 0.6) + (co2_score * 0.01)

    if score < 20:
        return "Low Risk 🟢"
    elif score < 30:
        return "Moderate Risk 🟡"
    else:
        return "High Risk 🔴"