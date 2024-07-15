# Plotting CPU Usage vs. System Power Consumption

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your columns are named "Battery_Percentage", "Total CPU Usage [%]", and "Total System Power [W]"
data_file = r"C:\Users\Midhun Mathew\Desktop\Data check\filter2.csv"  # Replace with your actual file path
df = pd.read_csv(data_file)

# Group by battery percentage and calculate average statistics for CPU usage and power
grouped_data = (
    df.groupby("Battery_Percentage")
    .agg(
        avg_cpu_usage=("Total CPU Usage [%]", "mean"),
        avg_power=("Total System Power [W]", "mean"),
    )
    .reset_index()
)

# Set up the matplotlib figure
plt.figure(figsize=(7, 5))

# Plot average CPU usage vs average system power
sns.lineplot(
    data=grouped_data,
    x="avg_cpu_usage",
    y="avg_power",
    marker="o",
    label="Average System Power",
    color="blue",
)
plt.title("CPU Usage vs. System Power Consumption")
plt.xlabel("Average CPU Usage (%)")
plt.ylabel("Average System Power (W)")
plt.grid(True)
plt.legend()

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
