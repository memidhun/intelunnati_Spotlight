import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your columns are named "Battery_Percentage", "Total CPU Usage [%]", and "Total System Power [W]"
data_file = r"C:\Users\Midhun Mathew\Desktop\Data check\filter2.csv"  # Replace with your actual file path
df = pd.read_csv(data_file)

# Group by battery percentage and calculate average/median/other statistics for CPU usage and power
grouped_data = (
    df.groupby("Battery_Percentage")
    .agg(
        avg_cpu_usage=("Total CPU Usage [%]", "mean"),
        median_cpu_usage=("Total CPU Usage [%]", "median"),
        avg_power=("Total System Power [W]", "mean"),
        median_power=("Total System Power [W]", "median"),
    )
    .reset_index()
)

# Set up the matplotlib figure
plt.figure(figsize=(7, 5))

# Plot average CPU usage
plt.subplot(2, 2, 1)
sns.lineplot(data=grouped_data, x="Battery_Percentage", y="avg_cpu_usage", marker="o")
plt.title("Average CPU Usage vs. Battery Percentage")
plt.xlabel("Battery Percentage (%)")
plt.ylabel("Average CPU Usage (%)")
plt.grid(True)

# Plot median CPU usage
plt.subplot(2, 2, 2)
sns.lineplot(
    data=grouped_data,
    x="Battery_Percentage",
    y="median_cpu_usage",
    marker="o",
    color="orange",
)
plt.title("Median CPU Usage vs. Battery Percentage")
plt.xlabel("Battery Percentage (%)")
plt.ylabel("Median CPU Usage (%)")
plt.grid(True)

# Plot average system power
plt.subplot(2, 2, 3)
sns.lineplot(
    data=grouped_data, x="Battery_Percentage", y="avg_power", marker="o", color="green"
)
plt.title("Average System Power vs. Battery Percentage")
plt.xlabel("Battery Percentage (%)")
plt.ylabel("Average System Power (W)")
plt.grid(True)

# Plot median system power
plt.subplot(2, 2, 4)
sns.lineplot(
    data=grouped_data, x="Battery_Percentage", y="median_power", marker="o", color="red"
)
plt.title("Median System Power vs. Battery Percentage")
plt.xlabel("Battery Percentage (%)")
plt.ylabel("Median System Power (W)")
plt.grid(True)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
