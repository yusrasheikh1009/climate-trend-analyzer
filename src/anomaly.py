import numpy as np

def detect_anomalies(df):
    mean = df['Temperature'].mean()
    std = df['Temperature'].std()

    df['Z_score'] = (df['Temperature'] - mean) / std
    df['Anomaly'] = df['Z_score'].apply(lambda x: 1 if abs(x) > 2 else 0)

    return df