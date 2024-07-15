import psutil
import csv
import os
import time
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd


def log_stats(duration=60):
    """Logs CPU, memory, power (if available), and NIC usage to a CSV file.

    Args:
        duration (int, optional): The duration (in seconds) to log data. Defaults to 60.
    """

    fields = [
        "timestamp",
        "cpu_usage",
        "memory_usage",
        "power_usage",
        "bytes_sent",
        "bytes_received",
    ]

    # Get the desktop path using platform-specific methods
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Create the filename with timestamp for uniqueness
    filename = f"system_usage_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    filepath = os.path.join(desktop_path, filename)

    with open(filepath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)

        start_time = time.time()
        while time.time() - start_time < duration:
            timestamp = datetime.now().strftime("%H:%M:%S")
            cpu_usage = psutil.cpu_percent()
            memory_usage = psutil.virtual_memory().percent

            try:
                # Attempt to get power usage using psutil.sensors_battery()
                power_usage = psutil.sensors_battery().percent
            except AttributeError:
                # Handle the case where psutil.sensors_battery() is not available (e.g., non-battery system)
                power_usage = "N/A"

            # Get NIC usage (bytes sent and received)
            net_io_counters = psutil.net_io_counters(
                pernic=False
            )  # Get total NIC usage
            bytes_sent = net_io_counters.bytes_sent
            bytes_received = net_io_counters.bytes_recv

            writer.writerow(
                [
                    timestamp,
                    cpu_usage,
                    memory_usage,
                    power_usage,
                    bytes_sent,
                    bytes_received,
                ]
            )
            csvfile.flush()

    print(f"Logging finished. Data saved to {filepath}")
    return filepath


def plot_data(filepath):
    data = pd.read_csv(filepath)
    timestamps = data["timestamp"]

    # Convert non-numeric columns to numeric
    data["power_usage"] = pd.to_numeric(data["power_usage"], errors="coerce")

    columns = [
        "cpu_usage",
        "memory_usage",
        "power_usage",
        "bytes_sent",
        "bytes_received",
    ]
    window_size = 5  # Window size for rolling average

    for column in columns:
        plt.figure(figsize=(10, 5))
        if column in ["bytes_sent", "bytes_received"]:
            # Scale NIC data for better visualization
            plt.plot(
                timestamps, data[column] / 1e6, label=column, alpha=0.5
            )  # Convert to MB
            plt.ylabel(f"{column} (MB)")
        else:
            # Smooth the values using a rolling average
            smoothed_values = (
                data[column].rolling(window=window_size, min_periods=1).mean()
            )
            plt.plot(
                timestamps, smoothed_values, label=f"{column} (smoothed)", alpha=0.5
            )
            plt.ylabel(column)

        plt.xlabel("Time")
        plt.title(f"{column} over Time")
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    log_filepath = log_stats(duration=60)
    plot_data(log_filepath)
