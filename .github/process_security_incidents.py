import csv
import pandas as pd

def process_security_incidents(input_file, output_file):
    # Read the CSV file and store the data in a list
    with open(input_file, 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
    
    # Add a new column named Status with a default value of "Pending" for all rows
    new_column_name = 'Status'
    for row in data:
        row.append("Pending")
    
    # Save the modified data to a new CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == "__main__":
    input_file = "security_incidents.csv"
    output_file = "security_incidents_modified.csv"
    process_security_incidents(input_file, output_file)