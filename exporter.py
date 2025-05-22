# exporter.py

import csv
from db import get_all_errors


def export_to_csv(file_path):
    """Export all error logs to a CSV file at the given path."""
    logs = get_all_errors()
    
    with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(["ID", "Timestamp", "Error Code", "Message", "Severity"])
        # Write rows
        for log in logs:
            writer.writerow(log)
