import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# =====================================================
# TRAFFIC PROBABILITY MODEL
# =====================================================

print("=" * 50)
print("TRAFFIC PROBABILITY MODEL")
print("=" * 50)

# -----------------------------------------------------
# Sample Traffic Dataset
# -----------------------------------------------------

data = {
    'Hour': list(range(24)),
    'Traffic_Count': [
        20, 15, 10, 8, 5, 12,
        30, 60, 90, 85, 70, 65,
        55, 50, 45, 60, 80, 95,
        100, 85, 70, 50, 35, 25
    ]
}

# -----------------------------------------------------
# Create DataFrame
# -----------------------------------------------------

df = pd.DataFrame(data)

print("\nOriginal Dataset")
print(df)

# -----------------------------------------------------
# Basic Statistics
# -----------------------------------------------------

max_traffic = df['Traffic_Count'].max()
min_traffic = df['Traffic_Count'].min()
avg_traffic = df['Traffic_Count'].mean()

print("\nTraffic Statistics")
print("Maximum Traffic:", max_traffic)
print("Minimum Traffic:", min_traffic)
print("Average Traffic:", round(avg_traffic, 2))

# -----------------------------------------------------
# Congestion Probability
# -----------------------------------------------------

df['Congestion_Probability'] = (
    df['Traffic_Count'] / max_traffic
) * 100

# -----------------------------------------------------
# Traffic Category
# -----------------------------------------------------

def classify_traffic(probability):

    if probability < 30:
        return "Low"

    elif probability < 60:
        return "Moderate"

    elif probability < 80:
        return "High"

    else:
        return "Severe"


df['Traffic_Category'] = df[
    'Congestion_Probability'
].apply(classify_traffic)

# -----------------------------------------------------
# Peak Hour Detection
# -----------------------------------------------------

peak_hours = df[
    df['Congestion_Probability'] >= 80
]

print("\nPeak Traffic Hours")
print(peak_hours[['Hour',
                  'Traffic_Count',
                  'Congestion_Probability']])

# -----------------------------------------------------
# Non Peak Hours
# -----------------------------------------------------

non_peak_hours = df[
    df['Congestion_Probability'] < 30
]

print("\nLow Traffic Hours")
print(non_peak_hours[['Hour',
                      'Traffic_Count']])

# -----------------------------------------------------
# Morning Rush Analysis
# -----------------------------------------------------

morning_rush = df[
    (df['Hour'] >= 7) &
    (df['Hour'] <= 10)
]

print("\nMorning Rush Hours")
print(morning_rush)

# -----------------------------------------------------
# Evening Rush Analysis
# -----------------------------------------------------

evening_rush = df[
    (df['Hour'] >= 16) &
    (df['Hour'] <= 19)
]

print("\nEvening Rush Hours")
print(evening_rush)

# -----------------------------------------------------
# Summary Information
# -----------------------------------------------------

total_traffic = df['Traffic_Count'].sum()

print("\nSummary")
print("Total Vehicles:", total_traffic)

print(
    "Average Congestion Probability:",
    round(
        df['Congestion_Probability'].mean(),
        2
    )
)

# -----------------------------------------------------
# Save Dataset
# -----------------------------------------------------

df.to_csv(
    "traffic_analysis_output.csv",
    index=False
)

print("\nCSV file exported successfully.")

# -----------------------------------------------------
# Line Graph
# -----------------------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    df['Hour'],
    df['Congestion_Probability'],
    marker='o',
    linewidth=2
)

plt.title(
    'Traffic Congestion Probability by Hour'
)

plt.xlabel('Hour of Day')

plt.ylabel(
    'Congestion Probability (%)'
)

plt.grid(True)

plt.savefig(
    'traffic_probability_line_graph.png'
)

# -----------------------------------------------------
# Bar Graph
# -----------------------------------------------------

plt.figure(figsize=(12, 6))

plt.bar(
    df['Hour'],
    df['Traffic_Count']
)

plt.title(
    'Hourly Traffic Count'
)

plt.xlabel('Hour')

plt.ylabel('Traffic Count')

plt.grid(True)

plt.savefig(
    'traffic_count_bar_graph.png'
)

# -----------------------------------------------------
# Peak Hour Report
# -----------------------------------------------------

print("\nPeak Hour Report")

for index, row in peak_hours.iterrows():

    print(
        f"Hour {row['Hour']} -> "
        f"{row['Traffic_Count']} vehicles "
        f"({row['Congestion_Probability']:.2f}%)"
    )

# -----------------------------------------------------
# Category Counts
# -----------------------------------------------------

print("\nTraffic Category Summary")

category_count = (
    df['Traffic_Category']
    .value_counts()
)

print(category_count)

# -----------------------------------------------------
# Detailed Hourly Report
# -----------------------------------------------------

print("\nHourly Analysis")

for index, row in df.iterrows():

    print(
        f"Hour {row['Hour']:02d}:00 "
        f"| Traffic={row['Traffic_Count']} "
        f"| Probability={row['Congestion_Probability']:.2f}% "
        f"| Category={row['Traffic_Category']}"
    )

# -----------------------------------------------------
# Highest Traffic Hour
# -----------------------------------------------------

highest_hour = df.loc[
    df['Traffic_Count'].idxmax()
]

print("\nHighest Traffic Hour")
print(highest_hour)

# -----------------------------------------------------
# Lowest Traffic Hour
# -----------------------------------------------------

lowest_hour = df.loc[
    df['Traffic_Count'].idxmin()
]

print("\nLowest Traffic Hour")
print(lowest_hour)

# -----------------------------------------------------
# Probability Distribution
# -----------------------------------------------------

plt.figure(figsize=(10, 5))

plt.hist(
    df['Congestion_Probability'],
    bins=8
)

plt.title(
    'Congestion Probability Distribution'
)

plt.xlabel(
    'Probability (%)'
)

plt.ylabel(
    'Frequency'
)

plt.grid(True)

plt.savefig(
    'probability_distribution.png'
)

# -----------------------------------------------------
# Final Dataset
# -----------------------------------------------------

print("\nFinal Dataset")
print(df)

# -----------------------------------------------------
# Completion Message
# -----------------------------------------------------

print("\nProject Completed Successfully")
print(
    "Generated:"
)
print(
    "1. CSV Output"
)
print(
    "2. Line Graph"
)
print(
    "3. Bar Graph"
)
print(
    "4. Histogram"
)
print(
    "5. Traffic Reports"
)

plt.show()
