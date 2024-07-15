import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your actual file path where your data is located
data_file = r"C:\Users\Midhun Mathew\Desktop\Data check\combined_data.csv"
df = pd.read_csv(data_file)

# Set up the matplotlib figures
plt.figure(figsize=(7, 5))

# Plot for Download Rate vs System Power
plt.subplot(2, 1, 1)
sns.lineplot(
    data=df,
    # x="Current DL rate [KB/s]",  # Replace with your actual column for Download rate
    # y="Total System Power [W]",  # Replace with your actual column for System Power
    x="CPU Package [C]",
    y="CPU Package Power [W]",
    marker="o",
    markersize=8,
    color="blue",
    linewidth=2,
)
plt.title("TDP - CPU Package Temperature vs CPU Package Power ")
plt.xlabel("CPU Package Temperature [C]")
plt.ylabel("CPU Package Power [W]")

# Plot for Upload Rate vs System Power
plt.subplot(2, 1, 2)
sns.lineplot(
    data=df,
    # x="Current UP rate [KB/s]",  # Replace with your actual column for Upload rate
    # y="Total System Power [W]",  # Replace with your actual column for System Power
    x="Core Temperatures (avg) [C]",
    y="Total System Power [W]",
    marker="o",
    markersize=8,
    color="green",
    linewidth=2,
)
plt.title("TDP - Core Temperature vs Total System Power")
plt.xlabel("Core Temperature [C]")
plt.ylabel("Total System Power [W]")

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()
