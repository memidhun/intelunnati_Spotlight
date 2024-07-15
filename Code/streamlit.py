import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Custom CSS to center the title
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        font-weight: bold;
        font-size: 50px;
    }
    .text {
        padding-top: 50px;
        margin-bottom: 50px;
        font-size: 20px;
        font-style: italic;
        font-weight: 500;
        justify-text: center;
        align-text: center;

        }
    /* Custom button styles */
    .stButton>button {
        border: 2px solid #4CAF50; 
        color: #FF7D29; 
        font-size: 200px; 
        font-family: 'Arial Black', Gadget, sans-serif;
        font-weight: 700 !important; 
        font-style: bold;
        padding: 10px 24px; 
        cursor: pointer;
        border-radius: 8px; 
        margin: 5px 0 10px 0;
    }
    .stButton>button:hover {
        background-color: #FA7070;
        color: black; 
    }
    /* Change text color on click */
    
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<h1 class="centered-title">Power Manager Telemetry</h1>', unsafe_allow_html=True)
st.write('<div class="text">This project aims on analyzing the telemetry data collected from the power manager system.It plots the relationship between different parameters and system power consumption.The power cosumption statistics of CPU,NIC Memory and TDP are analaysed for efffiecient management of power resources.Below are the plotted graphs.</div>', unsafe_allow_html=True)

# Replace with your actual file path where your data is located
data_file = r"C:\Users\HP\Desktop\Ashly S6\intelunnati\power manager\streamlit\filter2.csv"
df = pd.read_csv(data_file, encoding='ISO-8859-1')  # You can also try encoding='ISO-8859-1' or encoding='cp1252'

    # Button to show the plot for Temperature vs System Power (TDP)
if st.button("TDP vs System Power ", key="tdp"):
    # Set up the matplotlib figure
    plt.figure(figsize=(7, 5))

    # Plot for CPU Package Temperature vs CPU Package Power
    plt.subplot(2, 1, 1)
    sns.lineplot(
        data=df,
        x="CPU Package [°C]",
        y="CPU Package Power [W]",
        marker="o",
        markersize=8,
        color="blue",
        linewidth=2,
    )
    plt.title("TDP - CPU Package Temperature vs CPU Package Power")
    plt.xlabel("CPU Package Temperature [°C]")
    plt.ylabel("CPU Package Power [W]")

    # Plot for Core Temperature vs Total System Power
    plt.subplot(2, 1, 2)
    sns.lineplot(
        data=df,
        x="Core Temperatures (avg) [°C]",
        y="Total System Power [W]",
        marker="o",
        markersize=8,
        color="green",
        linewidth=2,
    )
    plt.title("TDP - Core Temperature vs Total System Power")
    plt.xlabel("Core Temperature [°C]")
    plt.ylabel("Total System Power [W]")
    # Display the plots
    st.pyplot(plt)
 # Button to show NIC (Network Interface Card) vs System Power
if st.button(" NIC usage vs System Power", key="nic"):
        # Set up the matplotlib figure
        plt.figure(figsize=(7, 5))  # Increase height for two vertically stacked subplots

        # Plot for Download Rate vs System Power
        plt.subplot(2, 1, 1)
        sns.lineplot(
            data=df,
            x="Total DL [MB]",  # Replace with your actual column for Download rate
            y="Total System Power [W]",  # Replace with your actual column for System Power
            marker="o",
            markersize=8,
            color="blue",
            linewidth=2,
        )
        plt.title("NIC - Download Rate vs System Power")
        plt.xlabel("Download Rate [MB]")
        plt.ylabel("System Power (W)")

        # Plot for Upload Rate vs System Power
        plt.subplot(2, 1, 2)
        sns.lineplot(
            data=df,
            x="Total UP [MB]",  # Replace with your actual column for Upload rate
            y="Total System Power [W]",  # Replace with your actual column for System Power
            marker="o",
            markersize=8,
            color="green",
            linewidth=2,
        )
        plt.title("NIC - Upload Rate vs System Power")
        plt.xlabel("Upload Rate [MB]")
        plt.ylabel("System Power (W)")

        # Adjust layout
        plt.tight_layout()

        # Show plots
        st.pyplot(plt)   

# Group by battery percentage and calculate average statistics for memory load and power
grouped_data_memory = (
    df.groupby("Battery_Percentage")
    .agg(
        avg_memory_load=("Physical Memory Load [%]", "mean"),
        avg_power=("Total System Power [W]", "mean"),
    )
    .reset_index()
)

    # Button to show Memory Load vs System Power
if st.button(" Memory Load vs System Power", key="mem"):
        plt.figure(figsize=(7, 5))

        # Plot average memory load vs average system power
        sns.lineplot(
            data=grouped_data_memory,
            x="avg_memory_load",
            y="avg_power",
            marker="o",
            label="System Power Consumption",
            color="blue",
        )
        plt.title("Physical Memory Usage vs System Power Consumption")
        plt.xlabel("Physical Memory Usage (%)")
        plt.ylabel("Average System Power (W)")
        plt.grid(True)
        plt.legend()

        # Adjust layout
        plt.tight_layout()

        # Show plot
        st.pyplot(plt)

# Group by battery percentage and calculate average statistics for CPU usage and power
grouped_data_cpu = (
    df.groupby("Battery_Percentage")
    .agg(
        avg_cpu_usage=("Total CPU Usage [%]", "mean"),
        avg_power=("Total System Power [W]", "mean"),
    )
    .reset_index()
)

    # Button to show CPU Usage vs System Power
if st.button("CPU Usage vs System Power", key="cpu"):
        plt.figure(figsize=(7, 5))

        # Plot average CPU usage vs average system power
        sns.lineplot(
            data=grouped_data_cpu,
            x="avg_cpu_usage",
            y="avg_power",
            marker="o",
            label="Average System Power",
            color="blue",
        )
        plt.title("CPU Usage vs System Power Consumption")
        plt.xlabel("Average CPU Usage (%)")
        plt.ylabel("Average System Power (W)")
        plt.grid(True)
        plt.legend()

        # Adjust layout
        plt.tight_layout()

        # Show plot
        st.pyplot(plt)
# User input for system utilization
st.sidebar.header('System Utilization Input')
cpu_util = st.sidebar.number_input('CPU Utilization (%)', min_value=0, max_value=100, value=50)
mem_util = st.sidebar.number_input('Memory Utilization (%)', min_value=0, max_value=100, value=50)
nic_util = st.sidebar.number_input('NIC Utilization (%)', min_value=0, max_value=100, value=50)

# Calculate average power consumption based on input utilization
avg_cpu_power = grouped_data_cpu['avg_power'].iloc[int(cpu_util/100 * (len(grouped_data_cpu)-1))]
avg_memory_power = grouped_data_memory['avg_power'].iloc[int(mem_util/100 * (len(grouped_data_memory)-1))]
avg_nic_power = df['Total System Power [W]'].mean() * (nic_util / 100)  # Estimate based on overall average

# Calculate total system power
total_system_power = avg_cpu_power + avg_memory_power + avg_nic_power

# Display average power consumption
st.write(f"System Utilization: CPU {cpu_util}%, Memory {mem_util}%, NIC {nic_util}%")
st.write(f"Average Power Consumption:")
st.write(f"CPU: {avg_cpu_power:.2f} W")
st.write(f"Memory: {avg_memory_power:.2f} W")
st.write(f"NIC: {avg_nic_power:.2f} W")
st.write(f"Total System Power: {total_system_power:.2f} W")