# Tools to Collect Power Telemetry Data

This folder contains the open-source tools researched and used in the Power Manager Telemetry project. Below is a brief overview of the contents:

## Tools Used
### Windows
- **Speccy**: For detailed system information and hardware monitoring.
- **OpenHardware Monitor**: Monitors various hardware parameters, including temperature and power consumption.
- **HWinfo**: Provides detailed diagnostics and power metrics for the system.
- **CPU-Z**: Gathers detailed CPU information and real-time monitoring.
- **PowerShell Scripts**: Used for automation and running tasks in Windows environments.

### Linux
- **vmstat**: Provides information about processes, memory, paging, block I/O, traps, and CPU activity.
- **turbostat**: Reports CPU frequency and idle state statistics.
- **psutil**: A Python library for retrieving information on system utilization (CPU, memory, disks, etc.).
- **powertop**: A tool for diagnosing issues with power consumption and power management.
- **powerstat**: Monitors power consumption of processes.
- **cpux**: Monitors CPU utilization.
- **cpupower**: A tool for managing CPU frequency and power settings.

## Main Tools for Data Collection
The primary tools used for data collection were:
- **Windows**: 
  - **HWinfo** and **OpenHardware Monitor**: These provided us with all the important power knobs and detailed diagnostics.
- **Linux**:
  - **powertop**, **psutil**, and **turbostat**: These tools were used to collect data on power consumption and system utilization.

## Data Processing and Analysis
The collected data were filtered, cleaned, analyzed, and plotted to understand the various power consumption patterns by different knobs.

These tools were selected based on their effectiveness for power telemetry and system monitoring across both operating systems. Refer to the main project [README.md](../README.md) for a comprehensive overview of the project and its objectives.
