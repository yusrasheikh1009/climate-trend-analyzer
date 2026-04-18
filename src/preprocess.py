import pandas as pd

def clean_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    # handle missing values
    df['Temperature'] = df['Temperature'].fillna(df['Temperature'].mean())
    df['Rainfall'] = df['Rainfall'].fillna(df['Rainfall'].mean())

    return df