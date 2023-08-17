#!/usr/bin/python3

import sys
import re

# Initialize variables
total_size = 0
status_counts = {}

# Define a function to print the statistics
def print_statistics():
    print("Total file size: File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

# Read from stdin line by line
for line_number, line in enumerate(sys.stdin):
    # Parse the line using a regular expression
    match = re.match(r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+|-)$', line)
    if match:
        # Extract the relevant information
        status_code = match.group(3)
        file_size = int(match.group(4))
        # Update the total file size
        total_size += file_size
        # Update the status code count
        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1
    # Print the statistics every 10 lines or on keyboard interruption
    if (line_number + 1) % 10 == 0:
        print_statistics()
try:
    # Print the final statistics
    print_statistics()
except ZeroDivisionError:
    pass
