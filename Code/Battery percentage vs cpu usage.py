# Plotting Battery Percentage vs. CPU Usage

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Assuming your columns are named "Battery_Percentage" and "Total CPU Usage [%]"
data_file = r"C:\Users\Midhun Mathew\Desktop\Data check\filter2.csv"  # Replace with your actual file path
df = pd.read_csv(data_file)

# Sort the dataframe by Battery_Percentage for correct plotting
df = df.sort_values(by="Battery_Percentage")

# Set up the matplotlib figure
plt.figure(figsize=(7, 5))

# Plot line for Battery Percentage vs CPU Usage
sns.lineplot(
    data=df,
    x="Battery_Percentage",
    y="Total CPU Usage [%]",
    marker="o",
    markersize=8,
    color="green",
    linewidth=2,
)

# Add labels and title
plt.title("Battery Usage vs. CPU Usage")
plt.xlabel("Battery Usage (%)")
plt.ylabel("CPU Usage (%)")

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
