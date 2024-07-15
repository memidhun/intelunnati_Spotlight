import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Assuming your columns are named "Battery_Percentage" and "Physical Memory Load [%]"
data_file = r"C:\Users\Midhun Mathew\Desktop\Data check\filter2.csv"  # Replace with your actual file path
df = pd.read_csv(data_file)

# Sort the dataframe by Battery_Percentage for correct plotting
df = df.sort_values(by="Battery_Percentage")

# Set up the matplotlib figure
plt.figure(figsize=(7, 5))

# Plot line for Battery Percentage vs Physical Memory Load
sns.lineplot(
    data=df,
    x="Core Temperatures (avg)",
    y="CPU Package Power [W]",
    marker="o",
    markersize=8,
    color="red",
    linewidth=2,
)

# Add labels and title
plt.title("Core Temperatures vs CPU Package Power")
plt.xlabel("Core Temperature [C]")
plt.ylabel("CPU Package Power [W]")

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
