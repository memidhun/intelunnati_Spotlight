import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your columns are named "Battery_Percentage" and "Total System Power [W]"
data_file = r"C:\Users\Midhun Mathew\Desktop\Data check\filter2.csv"  # Replace with your actual file path
df = pd.read_csv(data_file)

# Group by battery percentage and calculate average/median/other statistics for power
grouped_data = (
    df.groupby("Battery_Percentage")
    .agg(
        avg_power=("Total System Power [W]", "mean"),
        median_power=("Total System Power [W]", "median"),
    )
    .reset_index()
)

# Set up the matplotlib figure
plt.figure(figsize=(7, 5))

# Plot average and median system power
sns.lineplot(
    data=grouped_data,
    x="Battery_Percentage",
    y="avg_power",
    marker="o",
    label="Average System Power",
    color="green",
)
sns.lineplot(
    data=grouped_data,
    x="Battery_Percentage",
    y="median_power",
    marker="o",
    color="red",
    label="Median System Power",
)

plt.title("System Power vs. Battery Percentage")
plt.xlabel("Battery Percentage (%)")
plt.ylabel("System Power (W)")
plt.grid(True)
plt.legend()

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
