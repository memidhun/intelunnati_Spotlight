import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data into a pandas DataFrame
df = pd.read_csv('powerstat_output.csv')

# Convert 'Time' column to datetime format
df['Time'] = pd.to_datetime(df['Time'])

# Calculate CPU Usage (%) as sum of 'User', 'Nice', 'Sys'
df['CPU_Usage'] = df['User'] + df['Nice'] + df['Sys']

# Plot CPU Usage (%) and Watts over time
plt.figure(figsize=(12, 6))

# Plot CPU Usage (%)
plt.plot(df['Time'], df['CPU_Usage'], label='CPU Usage (%)', color='blue')
plt.xlabel('Time')
plt.ylabel('CPU Usage (%)')
plt.grid(True)
plt.legend()

# Plot Watts (Power Consumption)
plt.twinx()
plt.plot(df['Time'], df['Watts'], label='Power Consumption (W)', color='red')
plt.ylabel('Power Consumption (W)')
plt.legend()

# Title and display the plot
plt.title('CPU Usage vs Power Consumption')
plt.show()
