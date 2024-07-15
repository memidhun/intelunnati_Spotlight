import pandas as pd
import glob

# Load Data
files = glob.glob(r"C:\Users\Midhun Mathew\Desktop\Data check\combined_data.csv")
data_list = [pd.read_csv(file) for file in files]
data = pd.concat(data_list, ignore_index=True)

# Data Cleaning
data.drop_duplicates(inplace=True)

# Handle missing values (example: fill with mean)
data.fillna(data.mean(), inplace=True)

# Convert Date Time column to datetime
data["Date Time"] = pd.to_datetime(data["Date Time"])

# Extract Relevant Columns
relevant_columns = [
    "Date Time",
    "Total CPU Usage [%]",
    "Core Usage (avg) [%]",
    "CPU Package Power [W]",
    "Physical Memory Used [MB]",
    "Physical Memory Load [%]",
    "Current DL rate [KB/s]",
    "Current UP rate [KB/s]",
    "GPU D3D Usage [%]",
    "GT Cores Power [W]",
    "Core Temperatures (avg) [°C]",
    "CPU Package [°C]",
]

# Assume Battery Percentage column is added here, you can replace it with your actual data source
data["Battery_Percentage"] = 100  # Replace with your actual data source

# Reorder columns with Battery_Percentage included
relevant_columns_with_battery = ["Battery_Percentage"] + relevant_columns

data = data[relevant_columns_with_battery]

# Save the cleaned and filtered data
output_path = r"C:\Users\Midhun Mathew\Desktop\Data check/Filtered_Data.csv"
data.to_csv(output_path, index=False)

print(f"Filtered data saved to: {output_path}")
