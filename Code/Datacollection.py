

import subprocess
import psutil
import time
import os
import shutil

def create_folders():
    if not os.path.exists("HWiNFO_Logs"):
        os.makedirs("HWiNFO_Logs")
    if not os.path.exists("OpenHardwareMonitor_Logs"):
        os.makedirs("OpenHardwareMonitor_Logs")

def run_hwinfo():
    hwinfo_path = r'C:\Users\Midhun Mathew\Desktop\INTEL\HWiNFO_WINDOWS\HWiNFO64.exe'
    process = subprocess.Popen([hwinfo_path])
    return process

def run_openhardwaremonitor():
    openhardwaremonitor_path = r'C:\Path\To\OpenHardwareMonitor.exe'
    process = subprocess.Popen([openhardwaremonitor_path])
    return process

def save_logs(app_name, battery_percentage):
    source_path = r'C:\Path\To\Log\File.csv'  # Update with the actual path where logs are saved
    if app_name == "HWiNFO":
        destination_folder = "HWiNFO_Logs"
    else:
        destination_folder = "OpenHardwareMonitor_Logs"
    
    destination_path = os.path.join(destination_folder, f"{battery_percentage}%.csv")
    shutil.copyfile(source_path, destination_path)

def main():
    create_folders()
    battery_levels = list(range(100, 0, -5))
    
    for level in battery_levels:
        # Wait until battery level reaches the desired percentage
        while psutil.sensors_battery().percent > level:
            time.sleep(60)  # Check every minute

        # Run HWiNFO and OpenHardwareMonitor
        hwinfo_process = run_hwinfo()
        openhardwaremonitor_process = run_openhardwaremonitor()
        
        # Give some time for the applications to start and log data
        time.sleep(300)  # Log for 5 minutes (adjust as needed)
        
        # Save the logs
        save_logs("HWiNFO", level)
        save_logs("OpenHardwareMonitor", level)
        
        # Terminate the processes
        hwinfo_process.terminate()
        openhardwaremonitor_process.terminate()

if __name__ == "__main__":
    main()


