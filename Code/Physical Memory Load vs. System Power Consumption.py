# Plotting Physical Memory Load vs. System Power Consumption

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your columns are named "Battery_Percentage", "Physical Memory Load [%]", and "Total System Power [W]"
data_file = r"C:\Users\Midhun Mathew\Desktop\Data check\filter2.csv"  # Replace with your actual file path
df = pd.read_csv(data_file)

# Group by battery percentage and calculate average statistics for memory load and power
grouped_data = (
    df.groupby("Battery_Percentage")
    .agg(
        avg_memory_load=("Physical Memory Load [%]", "mean"),
        avg_power=("Total System Power [W]", "mean"),
    )
    .reset_index()
)

# Set up the matplotlib figure
plt.figure(figsize=(7, 5))

# Plot average memory load vs average system power
sns.lineplot(
    data=grouped_data,
    x="avg_memory_load",
    y="avg_power",
    marker="o",
    label="System Power Cosumption",
    color="blue",
)
plt.title("Physical Memory Usage vs. System Power Consumption")
plt.xlabel("Physical Memory Usage (%)")
plt.ylabel("Average System Power (W)")
plt.grid(True)
plt.legend()

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
