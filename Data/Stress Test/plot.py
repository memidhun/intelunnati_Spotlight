import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data into a DataFrame
file_path = r"C:\Users\Midhun Mathew\Desktop\INTEL\HWiNFO_WINDOWS\OUTPUTS\Special Cases\50normal.CSV"  # Replace with your actual file path
df = pd.read_csv(file_path)

# Filter data for 50% battery level
battery_50_df = df[df["Battery"] == 50]

# Extract relevant columns for analysis
relevant_cols = [
    "Date",
    "Time",
    "Total System Power [W]",
    "Memory Clock [MHz]",
    "Current cTDP Level []",
]
data = battery_50_df[relevant_cols]

# Plotting
plt.figure(figsize=(12, 6))

# Plot Total System Power
plt.subplot(2, 2, 1)
plt.plot(
    data["Time"], data["Total System Power [W]"], marker="o", linestyle="-", color="b"
)
plt.xlabel("Time")
plt.ylabel("Total System Power [W]")
plt.title("Total System Power [W] vs Time")

# Plot Memory Clock
plt.subplot(2, 2, 2)
plt.plot(data["Time"], data["Memory Clock [MHz]"], marker="o", linestyle="-", color="g")
plt.xlabel("Time")
plt.ylabel("Memory Clock [MHz]")
plt.title("Memory Clock [MHz] vs Time")

# Plot Current cTDP Level
plt.subplot(2, 2, 3)
plt.plot(
    data["Time"], data["Current cTDP Level []"], marker="o", linestyle="-", color="r"
)
plt.xlabel("Time")
plt.ylabel("Current cTDP Level []")
plt.title("Current cTDP Level [] vs Time")

plt.tight_layout()
plt.show()
