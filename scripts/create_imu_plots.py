#!/usr/bin/env python3
"""
Create interactive plots from IMU data (ax, ay, az, gx, gy, gz)
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# Load CSV file
csv_path = r"C:\Users\Alejandro\Documents\Documents\MESGRO\assets\data\advancedmechatronics\imu-data.csv"

print(f"Loading CSV: {csv_path}")
df = pd.read_csv(csv_path)

print(f"Columns: {df.columns.tolist()}")
print(f"Data shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())

# Check for relevant columns
relevant_cols = [col for col in df.columns if any(x in col.lower() for x in ['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'accel', 'gyro'])]
print(f"\nRelevant columns found: {relevant_cols}")

# Create acceleration plot (ax, ay, az)
print("\nCreating acceleration plot...")
fig1 = make_subplots(specs=[[{"secondary_y": False}]])

accel_cols = [col for col in df.columns if 'a' in col.lower() and any(x in col.lower() for x in ['x', 'y', 'z'])]
color_map = {'x': 'red', 'y': 'green', 'z': 'blue'}

for col in accel_cols:
    axis_name = col.split('_')[-1].lower() if '_' in col else col[-1].lower()
    color = color_map.get(axis_name, 'black')
    fig1.add_trace(
        go.Scatter(y=df[col], mode='lines', name=col, line=dict(color=color))
    )

fig1.update_layout(
    title="Acceleration Data (ax, ay, az)",
    xaxis_title="Sample",
    yaxis_title="Acceleration (m/s²)",
    hovermode='x unified',
    template='plotly_white',
    height=600,
    width=1000
)

# Save acceleration plot
output_path1 = r"C:\Users\Alejandro\Documents\Documents\MESGRO\assets\images\projects\advancedmechatronics\acceleration-plot.html"
fig1.write_html(output_path1)
print(f"✓ Saved: {output_path1}")

# Create gyroscope plot (gx, gy, gz)
print("Creating gyroscope plot...")
fig2 = make_subplots(specs=[[{"secondary_y": False}]])

gyro_cols = [col for col in df.columns if 'g' in col.lower() and any(x in col.lower() for x in ['x', 'y', 'z'])]

for col in gyro_cols:
    axis_name = col.split('_')[-1].lower() if '_' in col else col[-1].lower()
    color = color_map.get(axis_name, 'black')
    fig2.add_trace(
        go.Scatter(y=df[col], mode='lines', name=col, line=dict(color=color))
    )

fig2.update_layout(
    title="Gyroscope Data (gx, gy, gz)",
    xaxis_title="Sample",
    yaxis_title="Angular Velocity (°/s)",
    hovermode='x unified',
    template='plotly_white',
    height=600,
    width=1000
)

# Save gyroscope plot
output_path2 = r"C:\Users\Alejandro\Documents\Documents\MESGRO\assets\images\projects\advancedmechatronics\gyroscope-plot.html"
fig2.write_html(output_path2)
print(f"✓ Saved: {output_path2}")

print(f"\n✓ Interactive plots created successfully!")
print(f"  - Acceleration plot: {output_path1}")
print(f"  - Gyroscope plot: {output_path2}")
