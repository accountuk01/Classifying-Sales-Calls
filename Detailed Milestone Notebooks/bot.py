import os
import time

# List of files with desired dates
files_with_dates = [
    {'file':'Capstone 1 - Part 1A - Data Storytelling.ipynb','date':'2023-01-02 04:56:41'},
    {'file':'Capstone 1 - Part 1B - Exploratory Data Analysis.ipynb','date':'2023-01-02 04:56:41'},
    {'file':'Capstone 1 - Part 3 - InDepthAnalysis.ipynb','date':'2023-01-02 04:56:41'},
    {'file':'d.txt','date':'2023-01-02 04:56:41'}

]

for entry in files_with_dates:
    file_path = entry["file"]
    date_str = entry["date"]

    # Convert date string to timestamp
    timestamp = time.mktime(time.strptime(date_str, "%Y-%m-%d %H:%M:%S"))

    # Set last modified time
    os.utime(file_path, (timestamp, timestamp))
    print(f"Updated {file_path} to {date_str}")
