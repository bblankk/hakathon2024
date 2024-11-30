import os
import platform
import psutil
import subprocess
import csv
from datetime import datetime

# Function to get the system's basic info
def get_system_info():
    system_info = {}
    
    # Operating system information
    system_info['OS Name'] = platform.system()
    system_info['OS Version'] = platform.version()
    system_info['OS Release'] = platform.release()
    system_info['Architecture'] = platform.architecture()[0]
    
    # Memory information
    system_info['Total Memory (GB)'] = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    system_info['Available Memory (GB)'] = round(psutil.virtual_memory().available / (1024 ** 3), 2)
    
    # CPU information
    system_info['CPU Cores'] = psutil.cpu_count(logical=False)
    system_info['Logical CPUs'] = psutil.cpu_count(logical=True)
    system_info['CPU Frequency (MHz)'] = psutil.cpu_freq().current
    
    # Disk information
    disk_usage = psutil.disk_usage('/')
    system_info['Total Disk Space (GB)'] = round(disk_usage.total / (1024 ** 3), 2)
    system_info['Used Disk Space (GB)'] = round(disk_usage.used / (1024 ** 3), 2)
    system_info['Free Disk Space (GB)'] = round(disk_usage.free / (1024 ** 3), 2)
    system_info['Disk Usage (%)'] = disk_usage.percent
    
    # Drive letter and type (for Windows)
    if platform.system() == "Windows":
        drives = subprocess.check_output("wmic logicaldisk get caption, drivetype", shell=True).decode("utf-8").splitlines()
        drives = [drive.split() for drive in drives[1:] if drive.strip()]
        system_info['Drives'] = "; ".join([f"{drive[0]} - {drive[1]}" for drive in drives])
    
    # Time of collection
    system_info['Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return system_info

# Function to write the system information to a CSV file with 'key' and 'value' columns
def write_to_csv(system_info, filename="system_info.csv"):
    headers = ['key', 'value']  # Ensure these are the column names we expect
    
    # Check if the file exists and if not, create it with headers
    file_exists = os.path.isfile(filename)
    
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(headers)  # Write header if file is being created
        
        # Write each key-value pair as a row in the CSV (now in 'key' and 'value' columns)
        for key, value in system_info.items():
            writer.writerow([key, value])
    
    print(f"System information has been saved to {filename}")

# Main function to run the script
def main():
    system_info = get_system_info()
    write_to_csv(system_info)

if __name__ == "__main__":
    main()
