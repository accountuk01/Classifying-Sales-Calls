import os
import time

# List of files with desired dates
files_with_dates = [
        {'file':'BazeleyMikiko_Capstone1_Springboard_SlidePresentation.pdf', "date": '2023-01-04 01:15:40'},
        {'file':'Capstone Project 1_Final Report.pdf', "date": '2023-01-04 01:15:40'},
        {'file':'Detailed Milestone Notebooks', "date": '2023-01-04 01:15:40'},
        {'file':'Detailed Milestone Reports', "date": '2023-01-04 01:15:40'},
        {'file':'README.md', "date": '2023-01-04 01:15:40'},
        {'file':'XLSX Worksheet.xlsx', "date": '2023-01-04 01:15:40'},
]

for entry in files_with_dates:
    file_path = entry["file"]
    date_str = entry["date"]

    # Convert date string to timestamp
    timestamp = time.mktime(time.strptime(date_str, "%Y-%m-%d %H:%M:%S"))

    # Set last modified time
    os.utime(file_path, (timestamp, timestamp))
    print(f"Updated {file_path} to {date_str}")
