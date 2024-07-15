import pandas as pd
import os

# Directory containing the CSV files
csv_dir = (
    r"C:\Users\Midhun Mathew\Desktop\Data check\data"  # Replace with your actual path
)

# List to hold all DataFrames
dataframes = []

# Print the list of files in the directory (for debugging)
print(f"Files found in directory '{csv_dir}':")
print(os.listdir(csv_dir))

# Loop through each file in the directory
for filename in os.listdir(csv_dir):
    # Check if the file is a CSV (case insensitive)
    if filename.lower().endswith(".csv"):
        filepath = os.path.join(csv_dir, filename)
        try:
            df = pd.read_csv(filepath)
            # Extract the battery percentage from the filename
            battery_percentage = int(
                filename.replace("dc.CSV", "").replace("dc.csv", "")
            )
            df["Battery_Percentage"] = battery_percentage
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading {filename}: {e}")

# Check if any dataframes were collected
if len(dataframes) == 0:
    print("No CSV files found or error reading files.")
else:
    # Concatenate all DataFrames into a single DataFrame
    all_data = pd.concat(dataframes, ignore_index=True)

    # Save the combined DataFrame to a new CSV file (optional)
    combined_csv_path = os.path.join(csv_dir, "combined_data.csv")
    all_data.to_csv(combined_csv_path, index=False)

    # Display the combined DataFrame
    print(all_data.head())
