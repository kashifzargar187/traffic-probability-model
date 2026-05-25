import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample traffic data
data = {
    'Hour': list(range(24)),
    'Traffic_Count': [
        20, 15, 10, 8, 5, 12,
        30, 60, 90, 85, 70, 65,
        55, 50, 45, 60, 80, 95,
        100, 85, 70, 50, 35, 25
    ]
}

df = pd.DataFrame(data)

# Calculate congestion probability
max_traffic = df['Traffic_Count'].max()
df['Congestion_Probability'] = (
    df['Traffic_Count'] / max_traffic
) * 100

# Display data
print(df)

# Plot graph
plt.figure(figsize=(10, 5))
plt.plot(
    df['Hour'],
    df['Congestion_Probability'],
    marker='o'
)

plt.title('Traffic Congestion Probability by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Congestion Probability (%)')
plt.grid(True)

# Save graph
plt.savefig('graphs/traffic_probability_graph.png')

plt.show()
