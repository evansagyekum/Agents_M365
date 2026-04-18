import pandas as pd
import numpy as np
from xgboost import XGBRegressor

def create_features(df, window_size=20):
    # Remove constant sensors (flatliners)
    drop_sensors = ['s1', 's5', 's6', 's10', 's16', 's18', 's19']
    df = df.drop(columns=drop_sensors)
    
    # Calculate rolling statistics
    sensor_cols = [c for c in df.columns if c.startswith('s')]
    for col in sensor_cols:
        df[f'{col}_roll_mean'] = df.groupby('engine_id')[col].transform(lambda x: x.rolling(window_size).mean())
        df[f'{col}_roll_std'] = df.groupby('engine_id')[col].transform(lambda x: x.rolling(window_size).std())
    
    # Labeling: Piecewise Linear RUL (clipped at 125)
    df['rul_clipped'] = df['rul'].apply(lambda x: min(x, 125))
    
    return df.dropna()

def train_prediction_agent(X_train, y_train):
    model = XGBRegressor(
        n_estimators=500,
        max_depth=6,
        learning_rate=0.05,
        objective='reg:squarederror'
    )
    model.fit(X_train, y_train)
    return model
