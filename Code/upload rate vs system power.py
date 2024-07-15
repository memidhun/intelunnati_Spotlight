# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Replace with your actual file path where your data is located
# data_file = r"C:\Users\Midhun Mathew\Desktop\Data check\filter2.csv"
# df = pd.read_csv(data_file)

# # Convert Current Download rate from KB/s to MB/s
# df["Current DL rate [MB/s]"] = df["Current DL rate [KB/s]"] * 0.001

# # Calculate NIC usage (average of Current DL rate [MB/s] and Current UP rate [KB/s])
# df["NIC Usage [MB/s]"] = (
#     df["Current DL rate [MB/s]"] + df["Current UP rate [KB/s]"]
# ) / 2

# # Calculate Total Network Usage (sum of Total DL [MB] and Total UP [MB])
# df["Total Network Usage [MB]"] = df["Total DL [MB]"] + df["Total UP [MB]"]

# # Set up the matplotlib figure
# plt.figure(figsize=(10, 7))

# # Plot line for NIC Usage vs System Power with transparency
# sns.lineplot(
#     data=df,
#     x="NIC Usage [MB/s]",
#     y="Total System Power [W]",  # Replace with your actual column name for System Power
#     marker="o",
#     markersize=8,
#     color="orange",
#     linewidth=2,
#     alpha=1,  # Adding transparency to the line
# )

# # Add labels and title
# plt.title("NIC Usage vs. System Power Consumption")
# plt.xlabel("NIC Usage [MB/s]")
# plt.ylabel("System Power (W)")

# # Adjust layout
# plt.tight_layout()

# # Show plot
# plt.show()
# -------------------------------------------------------------------------------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Replace with your actual file path where your data is located
# data_file = r"C:\Users\Midhun Mathew\Desktop\Data check\filter2.csv"
# df = pd.read_csv(data_file)

# # Set up the matplotlib figure
# plt.figure(figsize=(10, 7))

# # Plot line for Download Rate vs System Power
# sns.lineplot(
#     data=df,
#     x="Current DL rate [KB/s]",  # Replace with your actual column for Download rate
#     y="Total System Power [W]",  # Replace with your actual column for System Power
#     marker="o",
#     markersize=8,
#     color="blue",
#     linewidth=2,
#     alpha=0.7,  # Adding transparency to the line
# )

# # Plot line for Upload Rate vs System Power
# sns.lineplot(
#     data=df,
#     x="Current UP rate [KB/s]",  # Replace with your actual column for Upload rate
#     y="Total System Power [W]",  # Replace with your actual column for System Power
#     marker="o",
#     markersize=8,
#     color="green",
#     linewidth=2,
#     alpha=0.7,  # Adding transparency to the line
# )

# # Add labels and title
# plt.title("Download and Upload Rate vs. System Power Consumption")
# plt.xlabel("Rate [KB/s]")
# plt.ylabel("System Power (W)")

# # Add legend
# plt.legend(["Download Rate", "Upload Rate"])

# # Adjust layout
# plt.tight_layout()

# # Show plot
# plt.show()

# -----------------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your actual file path where your data is located
data_file = r"C:\Users\Midhun Mathew\Desktop\Data check\filter2.csv"
df = pd.read_csv(data_file)

# Set up the matplotlib figures
plt.figure(figsize=(7, 5))

# Plot for Download Rate vs System Power
plt.subplot(2, 1, 1)
sns.lineplot(
    data=df,
    # x="Current DL rate [KB/s]",  # Replace with your actual column for Download rate
    # y="Total System Power [W]",  # Replace with your actual column for System Power
    x="Total DL [MB]",
    y="Total System Power [W]",
    marker="o",
    markersize=8,
    color="blue",
    linewidth=2,
)
plt.title("NIC - Download Rate vs System Power")
plt.xlabel("Download Rate [KB/s]")
plt.ylabel("System Power (W)")

# Plot for Upload Rate vs System Power
plt.subplot(2, 1, 2)
sns.lineplot(
    data=df,
    # x="Current UP rate [KB/s]",  # Replace with your actual column for Upload rate
    # y="Total System Power [W]",  # Replace with your actual column for System Power
    x="Total UP [MB]",
    y="Total System Power [W]",
    marker="o",
    markersize=8,
    color="green",
    linewidth=2,
)
plt.title("NIC - Upload Rate vs System Power")
plt.xlabel("Upload Rate [KB/s]")
plt.ylabel("System Power (W)")

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()
