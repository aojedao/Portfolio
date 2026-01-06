#!/usr/bin/env python3
"""
Create interactive plots from Speed Controller and Accel Tests CSV files
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# Load CSV files
speed_csv = r"C:\Users\Alejandro\Documents\Documents\MESGRO\assets\data\advancedmechatronics\speed-controller.csv"
accel_csv = r"C:\Users\Alejandro\Documents\Documents\MESGRO\assets\data\advancedmechatronics\accel-tests.csv"

print("=" * 60)
print("SPEED CONTROLLER DATA")
print("=" * 60)

try:
    df_speed = pd.read_csv(speed_csv)
    print(f"Columns: {df_speed.columns.tolist()}")
    print(f"Data shape: {df_speed.shape}")
    print(f"\nFirst few rows:")
    print(df_speed.head())
    
    # Create speed controller plot
    fig_speed = go.Figure()
    
    for col in df_speed.columns:
        fig_speed.add_trace(
            go.Scatter(y=df_speed[col], mode='lines', name=col)
        )
    
    fig_speed.update_layout(
        title="Speed Controller - All Columns",
        xaxis_title="Sample",
        yaxis_title="Value",
        hovermode='x unified',
        template='plotly_white',
        height=600,
        width=1000
    )
    
    output_speed = r"C:\Users\Alejandro\Documents\Documents\MESGRO\assets\images\projects\advancedmechatronics\speed-controller-plot.html"
    fig_speed.write_html(output_speed)
    print(f"\n✓ Saved: speed-controller-plot.html")
    
except Exception as e:
    print(f"Error with speed controller: {e}")

print("\n" + "=" * 60)
print("ACCEL TESTS DATA")
print("=" * 60)

try:
    df_accel = pd.read_csv(accel_csv)
    print(f"Columns: {df_accel.columns.tolist()}")
    print(f"Data shape: {df_accel.shape}")
    print(f"\nFirst few rows:")
    print(df_accel.head())
    
    # Create accel tests plot
    fig_accel = go.Figure()
    
    for col in df_accel.columns:
        fig_accel.add_trace(
            go.Scatter(y=df_accel[col], mode='lines', name=col)
        )
    
    fig_accel.update_layout(
        title="Acceleration Tests - All Columns",
        xaxis_title="Sample",
        yaxis_title="Value",
        hovermode='x unified',
        template='plotly_white',
        height=600,
        width=1000
    )
    
    output_accel = r"C:\Users\Alejandro\Documents\Documents\MESGRO\assets\images\projects\advancedmechatronics\accel-tests-plot.html"
    fig_accel.write_html(output_accel)
    print(f"\n✓ Saved: accel-tests-plot.html")
    
except Exception as e:
    print(f"Error with accel tests: {e}")

print("\n" + "=" * 60)
print("✓ All plots created successfully!")
print("=" * 60)
