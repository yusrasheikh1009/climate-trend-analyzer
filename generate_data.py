import pandas as pd
import numpy as np

dates = pd.date_range(start='2000-01-01', periods=300, freq='ME')

regions = ['North', 'South', 'East']

data_list = []

for region in regions:
    df = pd.DataFrame({
        'Date': dates,
        'Region': region,
        'Temperature': 25 + np.sin(np.arange(300)/12) + np.random.randn(300),
        'Rainfall': 100 + np.random.randn(300)*10,
        'CO2': 380 + np.linspace(0, 50, 300) + np.random.randn(300)*2
    })
    data_list.append(df)

data = pd.concat(data_list)

data.to_csv('data/climate_data.csv', index=False)